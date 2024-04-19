# To DO API

Use SQLAlchemy package to connect SQLite database to FastAPI project

you can see documents of API using "/docs"
![img](/API/assignment6/begginer/Screenshot%20from%202024-04-19%2023-45-06.png)

## docker commands
build image:
```
docker build -t "name" .
```
download image:
```
docker pull "image name"
```
create container:
```
docker run -d --name todoapp-a -p 80:80 todoap
```

## install requirements
```
pip install -r requirements.txt
apt-get install --assume-yes sqlite3 libsqlite3-dev
```
## RUN API:
```
uvicorn app.main:app --reload
```
### deployed in Liara
https://todoapp-amir.liara.run/