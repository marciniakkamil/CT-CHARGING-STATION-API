# Charging Station - backend API

## Run the project
```console
 docker-compose up -d
```

IMPORTANT !!!

If api container run fails please run this command once again.


Project will be running on http://localhost:8008.

For documentation check you can visit http://localhost:8008/docs#/

## Authentication



User can authenticate using a standard Swagger "Authorize" button with the following credentials:
```
username = "test"
password = "secret"
```

![alt text](image.png)

## Database
Main database is PostgreSQL
- Database will be filled up with 5 dummy Charging Station Types on the project startup.
- Functions & Triggers will be added also during the project startup.

## Logs
Loguru library is used for logging purposes.
https://github.com/Delgan/loguru

Logs are placed also in the app.log file.
