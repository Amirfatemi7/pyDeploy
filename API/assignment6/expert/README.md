# FastAPI database expert

Use SQLAlchemy package to connect PostgreSQL database to FastAPI project

you can see documents of API using "/docs"
<!-- ![img](/API/assignment6/expert/Screenshot%20from%202024-04-19%2023-45-06.png) -->


## install requirements
```
pip install -r requirements.txt
```
## RUN API:
```
uvicorn main:app --reload
```

## install docker PostgreSQL:
```
docker pull postgres
docker run -p 5432:5432 --name some-postgres -e POSTGRES_PASSWORD=pass -e POSTGRES_USER=user -e POSTGRES_DB=database_name -d postgres
```