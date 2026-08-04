from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def main():
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


@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}