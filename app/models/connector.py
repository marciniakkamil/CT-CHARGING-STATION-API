""""SQLAlchemy model for Connector"""
import uuid
from sqlalchemy import Boolean, Column, ForeignKey, String
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID

# imports from project files
from ..database.database import Base


class Connector(Base):
    """Connector SQLAlchemy model"""
    __tablename__ = "connectors"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, unique=True, index=True)
    priority = Column(Boolean, default=False)
    charging_station_id = Column(ForeignKey("charging_stations.id"), index=True)
    charging_station = relationship("ChargingStation", back_populates="connectors")
