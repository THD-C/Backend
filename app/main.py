import uvicorn
from fastapi import FastAPI
import os
from dotenv import load_dotenv

import src.DB as DB
import src.Router as Router

load_dotenv()

DB.create_tables(drop_existing=False)

app = FastAPI()
app.include_router(Router.user_router)


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)