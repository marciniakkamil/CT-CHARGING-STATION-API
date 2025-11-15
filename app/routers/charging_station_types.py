"""Charging Station Type routes"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import crud, dependencies
from ..routers.users import get_current_active_user
from ..models.charging_station_type import (
    ChargingStationType as ChargingStationTypeModel,
)
from ..schemas.charging_station_type import (
    ChargingStationType as ChargingStationTypeSchema,
)
from ..schemas.charging_station_type import (
    ChargingStationTypeCreate as ChargingStationTypeCreateSchema,
)

router = APIRouter(
    tags=["Charging Station Type"], dependencies=[Depends(get_current_active_user)]
)


@router.get("/charging-station-types/", response_model=list[ChargingStationTypeSchema])
async def read_charging_station_types(
    skip: int = 0, limit: int = 100, db: Session = Depends(dependencies.get_db)
):
    """Get list of the Charging Station Types"""
    return crud.get_items(db, model=ChargingStationTypeModel, skip=skip, limit=limit)


@router.get(
    "/charging-station-types/{cst_id}", response_model=ChargingStationTypeSchema
)
async def read_charging_station_type(
    cst_id: str, db: Session = Depends(dependencies.get_db)
):
    """Get single Charging Station Type by providing it's id(UUID)"""
    return crud.get_item(db, model=ChargingStationTypeModel, field="id", val=cst_id)


@router.delete("/charging-station-types/{cst_id}", status_code=200)
async def delete_charging_station_type(
    cst_id: str, db: Session = Depends(dependencies.get_db)
):
    """Remove single Charging Station Type by providing it's id(UUID)"""
    return crud.delete_item(db, model=ChargingStationTypeModel, i_id=cst_id)


@router.post("/charging-station-types/", response_model=ChargingStationTypeSchema)
async def create_charging_station_type(
    charging_station_type: ChargingStationTypeCreateSchema,
    db: Session = Depends(dependencies.get_db),
):
    """Create new Charging Station Type"""
    return crud.create_item(
        db=db, model=ChargingStationTypeModel, schema=charging_station_type
    )


@router.put(
    "/charging-station-types/{cst_id}", response_model=ChargingStationTypeSchema
)
async def update_charging_station_type(
    cst_id: str,
    charging_station_type: ChargingStationTypeSchema,
    db: Session = Depends(dependencies.get_db),
):
    """Update Charging Station Type by providing it's id(UUID) and data to update"""
    return crud.update_or_create_item(
        db=db,
        item_id=cst_id,
        model=ChargingStationTypeModel,
        schema=charging_station_type,
    )
