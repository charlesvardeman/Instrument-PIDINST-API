from typing import List
from models import PIDinst
from fastapi import FastAPI, HTTPException

app = FastAPI()

# This will act as our database for this example.
instruments = []

@app.post("/api/instruments", response_model=PIDinst)
async def create_instrument(instrument: PIDinst):
    # Assign an ID to the instrument
    instrument.id = len(instruments) + 1
    instruments.append(instrument.dict())
    return instrument

@app.get("/api/instruments/{id}", response_model=PIDinst)
async def read_instrument(id: int):
    for instrument in instruments:
        if instrument['id'] == id:
            return PIDinst(**instrument)
    raise HTTPException(status_code=404, detail="Instrument not found")

@app.put("/api/instruments/{id}", response_model=PIDinst)
async def update_instrument(id: int, instrument: PIDinst):
    for index, existing_instrument in enumerate(instruments):
        if existing_instrument['id'] == id:
            instruments[index] = instrument.dict()
            instruments[index]['id'] = id
            return instruments[index]
    raise HTTPException(status_code=404, detail="Instrument not found")

@app.delete("/api/instruments/{id}")
async def delete_instrument(id: int):
    for index, existing_instrument in enumerate(instruments):
        if existing_instrument['id'] == id:
            del instruments[index]
            return {"message": "Instrument deleted successfully."}
    raise HTTPException(status_code=404, detail="Instrument not found")

@app.get("/api/instruments", response_model=List[PIDinst])
async def read_instruments():
    return [PIDinst(**instrument) for instrument in instruments]

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
    