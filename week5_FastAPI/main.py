from fastapi import FastAPI
import uvicorn

from config.settings import APP_NAME, HOST, PORT, DEBUG
from database.database import create_db
from router import router

app = FastAPI()

app.include_router(router)


@app.get("/")
def home():
    return {"message": f"Welcome to {APP_NAME}"}


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