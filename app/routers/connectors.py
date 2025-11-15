"""Connectors routes"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import crud, dependencies
from ..routers.users import get_current_active_user
from ..models.connector import Connector as ConnectorModel
from ..schemas.connector import Connector as ConnectorSchema
from ..schemas.connector import ConnectorCreate as ConnectorCreateSchema

router = APIRouter(tags=["Connector"], dependencies=[Depends(get_current_active_user)])


@router.get("/connectors/", response_model=list[ConnectorSchema])
async def read_connectors(
    skip: int = 0, limit: int = 100, db: Session = Depends(dependencies.get_db)
):
    """Get list of the Connectors"""
    return crud.get_items(db, model=ConnectorModel, skip=skip, limit=limit)


@router.get("/connectors/{c_id}", response_model=ConnectorSchema)
async def read_connector(c_id: str, db: Session = Depends(dependencies.get_db)):
    """Get single Connector by providing it's id(UUID)"""
    return crud.get_item(db, model=ConnectorModel, field="id", val=c_id)


@router.delete("/connectors/{c_id}", status_code=200)
async def delete_connector(c_id: str, db: Session = Depends(dependencies.get_db)):
    """Remove single Conector by providing it's id(UUID)"""
    return crud.delete_item(db, model=ConnectorModel, i_id=c_id)


@router.post("/connectors/", response_model=ConnectorSchema)
async def create_connector(
    connector: ConnectorCreateSchema, db: Session = Depends(dependencies.get_db)
):
    """Create new Connector"""
    return crud.create_item(db=db, model=ConnectorModel, schema=connector)


@router.put("/connectors/{c_id}", response_model=ConnectorSchema)
async def update_connector(
    c_id: str, connector: ConnectorSchema, db: Session = Depends(dependencies.get_db)
):
    """Update Connector by providing it's id(UUID) and data to update"""
    return crud.update_or_create_item(
        db=db, item_id=c_id, model=ConnectorModel, schema=connector
    )
