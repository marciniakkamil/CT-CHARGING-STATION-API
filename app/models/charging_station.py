""""SQLAlchemy model for ChargingStation"""
import uuid
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID, INET

# imports from project files
from ..database.database import Base


# models
class ChargingStation(Base):
    """ChargingStation SQLAlchemy model"""
    __tablename__ = "charging_stations"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, index=True)
    device_id = Column(UUID(as_uuid=True), default=uuid.uuid4, unique=True)
    ip_address = Column(INET, unique=True)
    firmware_version = Column(String)
    charging_station_type_id = Column(
        ForeignKey("charging_station_types.id"), index=True
    )
    charging_station_type = relationship(
        "ChargingStationType", back_populates="charging_stations"
    )
    connectors = relationship("Connector", back_populates="charging_station")
