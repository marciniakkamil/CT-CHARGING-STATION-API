"""Pydantic models for Charging Station Type"""
import uuid
from pydantic import BaseModel, Field

from ..utils import enums


class ChargingStationTypeBase(BaseModel):
    """Charging Station Type parent Pydantic model"""
    name: str = Field(
        default=None, examples=["Charging Station fancy name"], unique=True
    )
    plug_count: int = Field(default=1, examples=[1])
    efficiency: float = Field(examples=[20.00])
    current_type: enums.ChargingStationCurrentTypesEnum = Field(
        default="AC", examples=["AC"]
    )


class ChargingStationTypeCreate(ChargingStationTypeBase):
    """Charging Station Type Pydantic model for creation purpose"""
    pass


class ChargingStationType(ChargingStationTypeBase):
    """Main Charging Station Type Pydantic model"""
    id: uuid.UUID = Field(default_factory=uuid.uuid4)

    class Config:
        from_attributes = True
