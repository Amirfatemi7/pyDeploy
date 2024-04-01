from fastapi import FastAPI, File, Form, UploadFile, HTTPException
import sqlite3



app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/tasks")
def read_tasks():
    tasks = read_tasks("tasks")
    return tasks

@app.post("/tasks")
def add_tasks(title: str = Form(),description: str = Form(), time:str = Form(), status:int = Form()):
    create_task("tasks", title, description, time, status)
    task = read_tasks("tasks")
    return task


@app.delete("/tasks/{id}")
def remove_tasks(id: int):
    delete_task("tasks", id)
    return {"msg":"tasks deleted"}

@app.put("/tasks/{id}")
def update_tasks(id:int, title: str = Form(),description: str = Form(), time:str = Form(), status:int = Form()):
    update_task("tasks", id, title, description, time, status)
    task = read_tasks("tasks")
    return task




def connect_db():
    # connect = sqlite3.connect("assignment4/todo.db")
    connect = sqlite3.connect("todo.db")
    return connect

def create_table(table_name:str):
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("create table if not exists {} (id INTEGER PRIMARY KEY AUTOINCREMENT, title text, description text, time text, status integer)".format(table_name))
    connection.commit()
    connection.close()

def create_task(table_name:str, title:str, description:str, time:str, status:int):
    create_table(table_name)
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("insert into {}(title, description, time, status) VALUES (?, ?, ?, ?)".format(table_name), (title, description, time, status))
    connection.commit()
    connection.close()

def read_tasks(table_name:str):
    create_table(table_name)
    connection = connect_db()
    cursor = connection.cursor()
    tasks = cursor.execute("select id, title, description, time, status from {}".format(table_name))
    taskss = tasks.fetchall()
    connection.commit()
    connection.close()
    tasks_dic = {}
    # for task in taskss:
    #     task_dic= {}
    #     task_dic['id'] = task['id']
    #     task_dic['title'] = task['title']
    #     task_dic['description'] = task['description']
    #     task_dic['time'] = task['time']
    #     task_dic['status'] = task['status']
    #     tasks_dic.append(task_dic)

    print(tasks_dic)
    return taskss

def read_task(table_name:str):
    create_table(table_name)
    connection = connect_db()
    cursor = connection.cursor()
    task = cursor.execute("select id, title, description, time, status from {} where id = ?".format(table_name), (id))
    taskk = task.fetchall()
    connection.commit()
    connection.close()
    return taskk

def update_task(table_name:str, id:int, title:str, description:str, time:str, status:int):
    create_table(table_name)
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("update {} set title = ?, description = ?, time = ?, status = ? where id = ?".format(table_name),(title, description, time, status, id))
    connection.commit()
    connection.close()

def delete_task(table_name:str, id):
    create_table(table_name)
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("delete from {} where id = ?".format(table_name), (id))
    connection.commit()
    connection.close()