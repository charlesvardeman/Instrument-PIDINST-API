from typing import List, Optional, Union
from pydantic import BaseModel, Field, HttpUrl
from enum import Enum

class IdentifierTypeEnum(str, Enum):
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

class AlternateIdentifierTypeEnum(str, Enum):
    SerialNumber = "SerialNumber"
    InventoryNumber = "InventoryNumber"
    Other = "Other"

class RelationTypeEnum(str, Enum):
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

class DateTypeEnum(str, Enum):
    Commissioned = "Commissioned"
    DeCommissioned = "DeCommissioned"

class Identifier(BaseModel):
    identifierValue: str
    identifierType: IdentifierTypeEnum

class Owner(BaseModel):
    ownerName: str
    ownerContact: Optional[str]
    ownerIdentifierValue: Optional[str]
    ownerIdentifierType: Optional[IdentifierTypeEnum]

class Manufacturer(BaseModel):
    manufacturerName: str
    manufacturerIdentifierValue: Optional[str]
    manufacturerIdentifierType: Optional[IdentifierTypeEnum]

class Model(BaseModel):
    modelName: str
    modelIdentifierValue: Optional[str]
    modelIdentifierType: Optional[IdentifierTypeEnum]

class InstrumentType(BaseModel):
    instrumentTypeName: str
    instrumentTypeIdentifierValue: Optional[str]
    instrumentTypeIdentifierType: Optional[IdentifierTypeEnum]

class Date(BaseModel):
    dateValue: str
    dateType: DateTypeEnum

class RelatedIdentifier(BaseModel):
    relatedIdentifierName: Optional[str]
    relationType: RelationTypeEnum
    relatedIdentifierValue: str
    relatedIdentifierType: IdentifierTypeEnum

class AlternateIdentifier(BaseModel):
    alternateIdentifierName: Optional[str]
    alternateIdentifierValue: str
    alternateIdentifierType: AlternateIdentifierTypeEnum

class PIDinst(BaseModel):
    Identifier: Identifier
    SchemaVersion: str = Field(..., const="1.0")
    LandingPage: HttpUrl
    Name: str
    Owner: List[Owner]
    Manufacturer: List[Manufacturer]
    Model: Model
    Description: Optional[str]
    InstrumentType: Optional[List[InstrumentType]]
    MeasuredVariable: Optional[List[str]]
    Date: Optional[List[Date]]
    RelatedIdentifier: Optional[List[RelatedIdentifier]]
    AlternateIdentifier: Optional[List[AlternateIdentifier]]

# Update forward references
PIDinst.update_forward_refs()
