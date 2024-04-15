# To DO API

This api save your daily tasks.
then you can see all of your task using get request of API or manage your tasks using another methods.

you can see documents of API using "/docs"
![Screenshot from 2024-04-06 01-03-20](https://github.com/Amirfatemi7/pyDeploy/assets/44161833/d1207657-4823-4572-8ea3-99d4264816fb)

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
```
https://todoapp-amir.liara.run/
```