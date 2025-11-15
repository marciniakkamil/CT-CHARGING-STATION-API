""""SQLAlchemy model for ChargingStationType"""
import uuid
from sqlalchemy import Column, Integer, String, Float, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID

# imports from project files
from ..database.database import Base
from ..utils import enums


class ChargingStationType(Base):
    """ChargingStationType SQLAlchemy model"""
    __tablename__ = "charging_station_types"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, unique=True)
    plug_count = Column(Integer, default=1)
    efficiency = Column(Float)
    current_type = Column(Enum(enums.ChargingStationCurrentTypesEnum), default="AC")
    charging_stations = relationship(
        "ChargingStation", back_populates="charging_station_type"
    )
