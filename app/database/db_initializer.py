"""Service needed for initial database configuration

temporary solution todo: use Alembic and Poetry"""
from sqlalchemy.dialects.postgresql import insert
from app.database.database import SessionLocal
from app.models.charging_station_type import ChargingStationType
import app.database.add_functions_and_triggers as text_queries


class DBInitializer:
    """Class needed for db initialization on startup"""
    def create_sample_data():
        """creating sample 5 Charging Station Types according to requirements"""
        with SessionLocal() as session:
            session.execute(
                insert(ChargingStationType)
                .values(
                    [
                        {
                            "name": "Type 1",
                            "plug_count": 3,
                            "efficiency": 23.22,
                            "current_type": "DC",
                        },
                        {
                            "name": "Type 2",
                            "plug_count": 2,
                            "efficiency": 50.22,
                            "current_type": "AC",
                        },
                        {
                            "name": "Type 3",
                            "plug_count": 1,
                            "efficiency": 30.00,
                            "current_type": "AC",
                        },
                        {
                            "name": "Type 4",
                            "plug_count": 2,
                            "efficiency": 11.11,
                            "current_type": "DC",
                        },
                        {
                            "name": "Type 5",
                            "plug_count": 1,
                            "efficiency": 21.99,
                            "current_type": "AC",
                        },
                    ]
                )
                .on_conflict_do_nothing()
            )
            session.commit()

    def create_functions_and_triggers():
        """creating DB functions and triggers according to requirements"""
        with SessionLocal() as session:
            session.execute(text_queries.allowed_connectors_by_priority_function)
            session.execute(text_queries.allowed_connectors_by_priority_trigger)
            session.execute(text_queries.allowed_connectors_number_function)
            session.execute(text_queries.allowed_connectors_number_trigger)
            session.commit()


db_initializer = DBInitializer()
