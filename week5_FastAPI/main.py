from fastapi import FastAPI
import uvicorn
from config.settings import APP_NAME, HOST, PORT, DEBUG
from database.database import engine, Base, create_db
from schemas.task import TaskBase

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Hello World"}


@app.get("/about")
def about():
    return {"message": "This is the about page."}

@app.get("/calculator")
def calculator(a: int, b: int):
    return {
        "a": a,
        "b": b,
        "sum": a + b,
        "difference": a - b,
        "product": a * b,
        "division": a / b
    }

@app.post("/users")
def create_user():
    return {"message": "User created."}

@app.post("/tasks")
def create_task(task: TaskBase):

    return {
        "message": "Task received",
        "task": task
    }


def main():
    print(f"Starting {APP_NAME}...")
    create_db()

    uvicorn.run(
        "main:app",
        host=HOST,
        port=PORT,
        reload=DEBUG
    )


if __name__ == "__main__":
    main()