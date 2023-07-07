import pytest
from fastapi.testclient import TestClient
from main import app
from models import PIDinst, Identifier, IdentifierTypeEnum, Owner, Manufacturer
from pydantic import EmailStr

client = TestClient(app)

# Define a fixture that will return a sample PIDinst object
@pytest.fixture
def sample_instrument():
    return PIDinst(
        Identifier=Identifier(identifierValue="1234", identifierType=IdentifierTypeEnum.DOI),
        SchemaVersion="1.0",
        LandingPage="http://example.com",
        Name="Instrument1",
        Owner=[Owner(ownerName="Owner1", ownerContact=EmailStr("owner1@example.com"),
            ownerIdentifierValue="O1", ownerIdentifierType=IdentifierTypeEnum.DOI)],
        Manufacturer=[Manufacturer(manufacturerName="Manufacturer1",
            manufacturerIdentifierValue="M1", manufacturerIdentifierType=IdentifierTypeEnum.DOI)],
    )

def test_create_instrument(sample_instrument):
    response = client.post("/api/instruments", json=sample_instrument.dict())
    assert response.status_code == 201
    assert response.json() == {**sample_instrument.dict(), "id": 1}  # Expect an id field in the response

def test_read_instrument(sample_instrument):
    # Create an instrument first
    client.post("/api/instruments", json=sample_instrument.dict())

    response = client.get("/api/instruments/1")
    assert response.status_code == 200
    assert response.json() == {**sample_instrument.dict(), "id": 1}

def test_update_instrument(sample_instrument):
    # Create an instrument first
    client.post("/api/instruments", json=sample_instrument.dict())

    updated_instrument = sample_instrument.copy(update={"Name": "UpdatedInstrument"})
    response = client.put("/api/instruments/1", json=updated_instrument.dict())
    assert response.status_code == 200
    assert response.json() == {**updated_instrument.dict(), "id": 1}

def test_delete_instrument(sample_instrument):
    # Create an instrument first
    client.post("/api/instruments", json=sample_instrument.dict())

    response = client.delete("/api/instruments/1")
    assert response.status_code == 204

# Add new test case
def test_read_instruments(sample_instrument):
    # Create an instrument first
    client.post("/api/instruments", json=sample_instrument.dict())

    response = client.get("/api/instruments")
    assert response.status_code == 200
    assert response.json() == [{**sample_instrument.dict(), "id": 1}]

def test_read_instruments(sample_instrument):
    # Create an instrument first
    client.post("/api/instruments", json=sample_instrument.dict())

    response = client.get("/api/instruments")
    assert response.status_code == 200
    assert response.json() == [{**sample_instrument.dict(), "id": 1}]
