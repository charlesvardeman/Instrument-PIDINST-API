from typing import List
from pydantic import BaseModel, EmailStr, HttpUrl

class Identifier(BaseModel):
    identifierValue: str
    identifierType: str

class Owner(BaseModel):
    ownerName: str
    ownerContact: EmailStr
    ownerIdentifierValue: str
    ownerIdentifierType: str

class Manufacturer(BaseModel):
    manufacturerName: str
    manufacturerIdentifierValue: str
    manufacturerIdentifierType: str

class PIDinst(BaseModel):
    Identifier: Identifier
    SchemaVersion: str
    LandingPage: str
    Name: str
    Owner: List[Owner]
    Manufacturer: List[Manufacturer]from typing import List, Optional, Union
from enum import Enum
from pydantic import BaseModel, EmailStr, HttpUrl

class IdentifierTypeEnum(Enum):
    ARK = "ARK"
    arXiv = "arXiv"
    bibcode = "bibcode"
    DOI = "DOI"
    EAN13 = "EAN13"
    EISSN = "EISSN"
    Handle = "Handle"
    IGSN = "IGSN"
    ISBN = "ISBN"
    ISSN = "ISSN"
    ISTC = "ISTC"
    LISSN = "LISSN"
    LSID = "LSID"
    PMID = "PMID"
    PURL = "PURL"
    UPC = "UPC"
    URL = "URL"
    URN = "URN"
    w3id = "w3id"

class RelatedIdentifierTypeEnum(Enum):
    ARK = "ARK"
    arXiv = "arXiv"
    bibcode = "bibcode"
    DOI = "DOI"
    EAN13 = "EAN13"
    EISSN = "EISSN"
    Handle = "Handle"
    IGSN = "IGSN"
    ISBN = "ISBN"
    ISSN = "ISSN"
    ISTC = "ISTC"
    LISSN = "LISSN"
    LSID = "LSID"
    PMID = "PMID"
    PURL = "PURL"
    UPC = "UPC"
    URL = "URL"
    URN = "URN"
    w3id = "w3id"

class AlternateIdentifierTypeEnum(Enum):
    SerialNumber = "SerialNumber"
    InventoryNumber = "InventoryNumber"
    Other = "Other"

class RelationTypeEnum(Enum):
    IsDescribedBy = "IsDescribedBy"
    HasMetadata = "HasMetadata"
    IsNewVersionOf = "IsNewVersionOf"
    IsPreviousVersionOf = "IsPreviousVersionOf"
    IsComponentOf = "IsComponentOf"
    HasComponent = "HasComponent"
    References = "References"
    IsIdenticalTo = "IsIdenticalTo"
    IsAttachedTo = "IsAttachedTo"
    WasUsedIn = "WasUsedIn"

class DateTypeEnum(Enum):
    Commissioned = "Commissioned"
    DeCommissioned = "DeCommissioned"

class Identifier(BaseModel):
    identifierValue: str
    identifierType: IdentifierTypeEnum

class Owner(BaseModel):
    ownerName: str
    ownerContact: Optional[EmailStr] = None
    ownerIdentifierValue: Optional[str] = None
    ownerIdentifierType: Optional[IdentifierTypeEnum] = None

class Manufacturer(BaseModel):
    manufacturerName: str
    manufacturerIdentifierValue: Optional[str] = None
    manufacturerIdentifierType: Optional[IdentifierTypeEnum] = None

class Model(BaseModel):
    modelName: str
    modelIdentifierValue: Optional[str] = None
    modelIdentifierType: Optional[IdentifierTypeEnum] = None

class InstrumentType(BaseModel):
    instrumentTypeName: str
    instrumentTypeIdentifierValue: Optional[str] = None
    instrumentTypeIdentifierType: Optional[IdentifierTypeEnum] = None

class Date(BaseModel):
    dateValue: str
    dateType: DateTypeEnum

class RelatedIdentifier(BaseModel):
    relatedIdentifierName: Optional[str] = None
    relationType: Optional[RelationTypeEnum] = None
    relatedIdentifierValue: str
    relatedIdentifierType: RelatedIdentifierTypeEnum

class AlternateIdentifier(BaseModel):
    alternateIdentifierName: Optional[str] = None
    alternateIdentifierValue: str
    alternateIdentifierType: AlternateIdentifierTypeEnum

class PIDinst(BaseModel):
    Identifier: Identifier
    SchemaVersion: str
    LandingPage: HttpUrl
    Name: str
    Owner: List[Owner]
    Manufacturer: List[Manufacturer]
    Model: Optional[Model] = None
    Description: Optional[str] = None
    InstrumentType: Optional[List[InstrumentType]] = None
    MeasuredVariable: Optional[List[str]] = None
    Date: Optional[List[Date]] = None
    RelatedIdentifier: Optional[List[RelatedIdentifier]] = None
    AlternateIdentifier: Optional[List[AlternateIdentifier]] = None

    class Config:
        title = 'PIDinst schema 1.0'
        description = 'Describes a schema for metadata conforming to the PIDinst metadata schema 1.0'
