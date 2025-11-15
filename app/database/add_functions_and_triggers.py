""""Functions & Triggers needed for PostgereSQL"""
from sqlalchemy import text

allowed_connectors_number_function = text(
    "CREATE OR REPLACE FUNCTION allowed_connectors_number() "
    "RETURNS TRIGGER AS "
    "$body$ "
    "DECLARE "
    "allowed_plug_count SMALLINT; "
    "current_plug_count SMALLINT; "
    "BEGIN "
    "SELECT plug_count FROM charging_station_types JOIN charging_stations "
    "ON charging_station_types.id = charging_stations.charging_station_type_id JOIN connectors "
    "ON connectors.charging_station_id = charging_stations.id "
    "WHERE charging_stations.id = NEW.charging_station_id INTO  allowed_plug_count ; "
    "SELECT count(*) FROM connectors WHERE charging_station_id = NEW.charging_station_id "
    "INTO current_plug_count; "
    "IF current_plug_count >= allowed_plug_count "
    "THEN  "
    "RAISE EXCEPTION 'The limit on the number of connectors for  has been reached'; "
    "END IF; "
    "RETURN NEW; "
    "END; "
    "$body$ "
    "LANGUAGE plpgsql; "
)

allowed_connectors_by_priority_trigger = text(
    "CREATE OR REPLACE TRIGGER tr_allowed_connectors_by_priority "
    "BEFORE INSERT ON connectors "
    "FOR EACH ROW EXECUTE PROCEDURE allowed_connectors_by_priority(); "
)

allowed_connectors_by_priority_function = text(
    "CREATE OR REPLACE FUNCTION allowed_connectors_by_priority() "
    "RETURNS TRIGGER AS "
    "$body$ "
    "DECLARE "
    "connectors_with_prio_count SMALLINT;"
    "BEGIN "
    "SELECT count(*) FROM connectors JOIN charging_stations "
    "ON charging_stations.id = connectors.charging_station_id "
    "WHERE connectors.priority = TRUE INTO connectors_with_prio_count; "
    "IF connectors_with_prio_count > 0 AND NEW.priority = TRUE "
    "THEN "
    "RAISE EXCEPTION 'There schould be only one Connector with priority for one Charging Station.';"
    "END IF; "
    "RETURN NEW; "
    "END; "
    "$body$ "
    "LANGUAGE plpgsql; "
)

allowed_connectors_number_trigger = text(
    "CREATE OR REPLACE TRIGGER tr_allowed_connectors_number "
    "BEFORE INSERT ON connectors "
    "FOR EACH ROW EXECUTE PROCEDURE allowed_connectors_number(); "
)
