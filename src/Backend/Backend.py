from fastapi import FastAPI

from pydantic import BaseModel

from typing import Optional

app = FastAPI()

@app.get("/")

def index():
    return {"message":"hello"}


todoList ={}

class TodoItem(BaseModel):

    title: Optional[str] = None
    type: Optional[str] = None
    date:Optional[str] = None
    description:Optional[str] = None
    completed:Optional[bool] = None

@app.post("/TodoItem/")

async def create_todoItem(todoItem: TodoItem):
    todo_id = len(todoList) + 1
    todoList[todo_id] = todoItem
    return {"message": "TodoItem created successfully", "TodoId": todo_id, "Title": todoItem.title, "Type" : todoItem.type, "To be done by": todoItem.date,
            "Description":todoItem.description, "Completed": todoItem.completed}


    


@app.get("/TodoItem/{TodoId}")

def get_ToDoItem(TodoId:int):
    return todoList[TodoId]


@app.get("/TodoItem/type/{TodoType}")

def get_todoFromType(TodoType : str):
    matched_items = [todo_item for todo_item in todoList.values() if todo_item.type == TodoType]
    return matched_items

@app.get("/TodoItem/completed/{TodoStatus}")

def get_todoFromStatus(TodoStatus : bool):
    matched_items = [todo_item for todo_item in todoList.values() if todo_item.completed == TodoStatus]

    return matched_items

@app.put("/TodoItem/update/{TodoId}")

def updateItem(id:int, item:TodoItem):
    if id not in todoList:
        return {"error": "task not found"}
    
    if item.title != None:
        todoList[id].title = item.title
    if item.type != None:
        todoList[id].type = item.type
    if item.description != None:
        todoList[id].description = item.description
    if item.completed !=None:
        todoList[id].completed = item.completed

    return {"message": "TodoItem updated successfully", "TodoId": id, "Title": item.title, "Type" : item.type, "To be done by": item.date,
        "Description":item.description, "Completed": item.completed}



@app.delete("/TodoItem/delete/{TodoId}")

def deleteStudent(id:int):
    if id not in todoList:
        return {"error": "no"}
    del todoList[id]
    return {"message":"task successfully deleted!"}


