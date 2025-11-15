CREATE OR REPLACE FUNCTION allowed_connectors_number()
RETURNS TRIGGER AS
$body$
DECLARE
    allowed_plug_count SMALLINT;
    current_plug_count SMALLINT;
BEGIN
    SELECT plug_count FROM charging_station_types JOIN charging_stations 
ON charging_station_types.id = charging_stations.charging_station_type_id JOIN connectors
ON connectors.charging_station_id = charging_stations.id
WHERE charging_stations.id = NEW.charging_station_id INTO allowed_plug_count ;

    SELECT count(*) FROM connectors WHERE charging_station_id = NEW.charging_station_id INTO current_plug_count;
    
    IF current_plug_count >= allowed_plug_count
    THEN 
        RAISE EXCEPTION 'The limit for the number of connectors has been reached';
    END IF;
    RETURN NEW;
END;
$body$
LANGUAGE plpgsql;

CREATE OR REPLACE TRIGGER tr_allowed_connectors_number 
BEFORE INSERT ON connectors
FOR EACH ROW EXECUTE PROCEDURE allowed_connectors_number();

CREATE OR REPLACE FUNCTION allowed_connectors_by_priority()
RETURNS TRIGGER AS
$body$
DECLARE
    connectors_with_prio_count SMALLINT;
BEGIN

    SELECT count(*) FROM connectors JOIN charging_stations 
ON charging_stations.id = connectors.charging_station_id 
WHERE connectors.priority = TRUE INTO connectors_with_prio_count;
    
    IF connectors_with_prio_count > 0 AND NEW.priority = TRUE
    THEN 
        RAISE EXCEPTION 'There schould be only one Connector with priority for one Charging Station.';
    END IF;
    RETURN NEW;
END;
$body$
LANGUAGE plpgsql;

CREATE OR REPLACE TRIGGER tr_allowed_connectors_by_priority
BEFORE INSERT ON connectors
FOR EACH ROW EXECUTE PROCEDURE allowed_connectors_by_priority();

INSERT INTO charging_station_types(id, name, plug_count, efficiency, current_type) VALUES
('a45fc1f6-6a64-4ae3-ab78-4c847d4447ba', 'Type 1', 3, 23.22, 'DC'),
('f45063e6-18f0-45e2-84d3-d29ad94adb5c','Type 2', 1, 25.00, 'AC'),
('607ebaba-5fa5-40cb-a693-7c2016cd8378','Type 3', 2, 23.00, 'DC'),
('61de78ae-c151-4841-af7a-7625d51997e5','Type 4', 1, 3.22, 'AC'),
('4894ada0-2286-4a89-8516-9e32a0cfe979','Type 5', 3, 23.22, 'DC')