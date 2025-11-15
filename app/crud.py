"""General CRUD functions for usage in the the application Routers

"""
from fastapi import HTTPException
from sqlalchemy.orm import Session
from .utils.logger import logger


def get_items(db: Session, model: any, skip: int = 0, limit: int = 100):
    """general function for getting list of items from the database"""
    logger.info(f"Getting list of {model} ...")
    result = []
    try:
        result = db.query(model).offset(skip).limit(limit).all()
    except Exception as e:
        exception_message = f"Bad request. Error: {e}"
        logger.info(exception_message)
        raise HTTPException(status_code=400, detail=exception_message)
    return result


def get_item(db: Session, model: any, field: str, val: str | int | float):
    """general function for getting single item from the database"""
    logger.info(f"Getting single {model} with {field} = {val} ...")
    try:
        query_results = db.query(model).filter_by(**{field: val})
        db_item = query_results.first()
        if db_item is None:
            exception_message = f"{model} where {field} = {val} not found"
            logger.info(exception_message)
            raise HTTPException(status_code=404, detail=exception_message)
    except Exception as e:  # todo: DRY
        exception_message = f"Bad request. Error: {e}"
        logger.info(exception_message)
        raise HTTPException(status_code=400, detail=exception_message)
    logger.info(f"{model} with {field} = {val} successfully received ...")
    return db_item


def delete_item(db: Session, model: any, i_id: str):
    """general function for deleting single item from the database"""
    logger.info(f"Finding item for deletion: {model} with id {i_id} ...")
    try:
        db_item = db.query(model).filter(model.id == i_id).first()
        if db_item is None:
            raise HTTPException(
                status_code=404, detail=f"{model} where id = {i_id} not found"
            )
    except Exception as e:  # todo: DRY
        exception_message = f"Bad request. Error: {e}"
        logger.info(exception_message)
        raise HTTPException(status_code=400, detail=exception_message)
    logger.info(f"Deleting {model} with id {i_id} ...")
    try:
        db.delete(db_item)
        db.commit()
    except Exception as e:
        exception_message = f"DB: Item deletion failed: {model}. Error: {e}"
        logger.info(exception_message)
        raise HTTPException(status_code=400, detail=exception_message)
    logger.info(f"{model} with id {i_id} successfully deleted ...")
    return {"message": f"{model} with id {i_id} successfully deleted"}


def create_item(db: Session, model: any, schema: any):
    """general function for creating single item in the database"""
    logger.info(f"Creating new {model} ...")
    insert_item = model(**schema.model_dump())
    try:
        db.add(insert_item)
        db.commit()
        db.refresh(insert_item)
    except Exception as e:  # todo: DRY
        exception_message = f"DB: Creating new item failed: {model}. Error: {e}"
        logger.info(exception_message)
        raise HTTPException(status_code=400, detail=exception_message)
    logger.info(f"New {model} record successfully created ...")
    return insert_item


def update_or_create_item(db: Session, item_id: str, model: any, schema: any):
    """general function for updating/creating single item in the database"""
    logger.info(f"Finding item to update: {model} with id {item_id} ...")
    try:
        query_results = db.query(model).filter(model.id == item_id)
        stored_item = query_results.first()
        for var, value in vars(schema).items():
            setattr(stored_item, var, value) if value else None
    except Exception as e:  # todo: DRY
        exception_message = f"DB: Item update failed: {model}. Error: {e}"
        logger.info(exception_message)
        raise HTTPException(status_code=400, detail=exception_message)
    logger.info(f"Inserting updated {model} with id {item_id} to the database ...")
    try:
        db.add(stored_item)
        db.commit()
        db.refresh(stored_item)
    except Exception as e:
        exception_message = f"DB: Updating item failed: {model}. Error: {e}"
        logger.info(exception_message)
        raise HTTPException(status_code=400, detail=exception_message)
    logger.info(f"{model} with id {item_id} successfully updated ...")
    return stored_item
