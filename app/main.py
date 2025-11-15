# pip install python-dotenv
import os

from dotenv import load_dotenv
from fastapi import FastAPI

from anonymous_board.controller.anonymous_board_controller import anonymous_board_controller
from config.mysql_config import Base, engine

load_dotenv()

# pip install fastapi
app = FastAPI()

app.include_router(anonymous_board_controller)

if __name__ == "__main__":
    # pip install uvicorn
    import uvicorn
    host = os.getenv("APP_HOST")
    port = int(os.getenv("APP_PORT"))
    Base.metadata.create_all(bind=engine)
    uvicorn.run(app, host=host, port=port)
