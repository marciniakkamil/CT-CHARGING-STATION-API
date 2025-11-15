"""Pydantic models for Charging Station"""
import uuid
from pydantic import BaseModel, Field

from ..schemas.charging_station_type import ChargingStationType

class ChargingStationBase(BaseModel):
    """Charging Station parent Pydantic model"""
    name: str
    device_id: uuid.UUID = Field(default_factory=uuid.uuid4)
    ip_address: str = Field(default="192.168.1.1", examples=["192.168.1.1"])
    firmware_version: str = Field(default="1.0.0", examples=["1.0.0"])
    charging_station_type_id: uuid.UUID = Field(default_factory=uuid.uuid4)


class ChargingStationCreate(ChargingStationBase):
    """Charging Station Pydantic model for creation purpose"""
    pass


class ChargingStation(ChargingStationBase):
    """Main Charging Station Pydantic model"""
    id: uuid.UUID = Field(default_factory=uuid.uuid4)
    charging_station_type: ChargingStationType

    class Config:
        from_attributes = True
