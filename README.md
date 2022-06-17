# FastAPI-Postgres-docker-compose
- FastAPI app
- PostgreSQL integration using SQLAlchemy
- Dockerfile and docker-compose integrations

# How to run this with Docker?
- Make sure you have docker & docker-compose are installed and running on your machine
- Make a copy of `env.example` file in the project root, and rename it to `env`:
Set value of **`OPEN_WEATHER_API_KEY`** env-variable, which can be from [here](https://home.openweathermap.org/api_keys)
- Open the terminal to the docker-compose path and hit the following command
```mac
MYCOMPUTER:project user$ docker-compose up --build
```
```linux
docker-compose up --build
```
