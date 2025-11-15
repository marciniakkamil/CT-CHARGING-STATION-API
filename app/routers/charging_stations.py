"""Charging Station routes"""
from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session

from app import crud, dependencies
from ..routers.users import get_current_active_user
from ..models.charging_station import ChargingStation as ChargingStationModel
from ..schemas.charging_station import ChargingStation as ChargingStationSchema
from ..schemas.charging_station import (
    ChargingStationCreate as ChargingStationCreateSchema,
)

router = APIRouter(
    tags=["Charging Station"], dependencies=[Depends(get_current_active_user)]
)


@router.get("/charging-stations/", response_model=list[ChargingStationSchema])
async def read_charging_stations(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(dependencies.get_db),
    request: Request = Request,
):
    """Get list of the Charging Stations"""
    # todo apply filtering
    request_params = request.query_params
    print("REQ params >>>>")
    print(dict(request_params))
    return crud.get_items(db=db, model=ChargingStationModel, skip=skip, limit=limit)


@router.get("/charging-stations/{cs_id}", response_model=ChargingStationSchema)
async def read_charging_station(cs_id: str, db: Session = Depends(dependencies.get_db)):
    """Get single Charging Station by providing it's id(UUID)"""
    return crud.get_item(db=db, model=ChargingStationModel, field="id", val=cs_id)


@router.delete("/charging-stations/{cs_id}", status_code=200)
async def delete_charging_station(
    cs_id: str, db: Session = Depends(dependencies.get_db)
):
    """Remove single Charging Station by providing it's id(UUID)"""
    return crud.delete_item(db=db, model=ChargingStationModel, i_id=cs_id)


@router.post("/charging-stations/", response_model=ChargingStationSchema)
async def create_charging_station(
    charging_station: ChargingStationCreateSchema,
    db: Session = Depends(dependencies.get_db),
):
    """Create new Charging Station"""
    return crud.create_item(db=db, model=ChargingStationModel, schema=charging_station)


@router.put("/charging-stations/{cs_id}", response_model=ChargingStationSchema)
async def update_charging_station(
    cs_id: str,
    charging_station: ChargingStationSchema,
    db: Session = Depends(dependencies.get_db),
):
    """Update Charging Station by providing it's id(UUID) and data to update"""
    return crud.update_or_create_item(
        db=db, item_id=cs_id, model=ChargingStationModel, schema=charging_station
    )
