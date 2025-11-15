"""Pydantic models for Connector"""
import uuid
from pydantic import BaseModel, Field

from ..schemas.charging_station import ChargingStation


class ConnectorBase(BaseModel):
    """Connector parent Pydantic model"""
    name: str
    priority: bool
    charging_station_id: uuid.UUID = Field(default_factory=uuid.uuid4)


class ConnectorCreate(ConnectorBase):
    """Connector model for creation purpose"""
    pass


class Connector(ConnectorBase):
    """Main Connector Pydantic model"""
    id: uuid.UUID = Field(default_factory=uuid.uuid4)
    charging_station: ChargingStation

    class Config:
        from_attributes = True
