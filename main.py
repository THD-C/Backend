import uvicorn
from fastapi import FastAPI, responses
import os
from dotenv import load_dotenv

import src.DB as DB
import src.Router as Router

load_dotenv()

DB.create_tables(drop_existing=True)

app = FastAPI()
app.include_router(Router.user_router)


@app.get("/", response_class=responses.HTMLResponse)
async def read_items():
    return """
    <html>
        <head>
            <title>THD(c) API</title>
        </head>
        <body>
            <h1>THD(c) API is up and running!</h1>
        </body>
    </html>
    """


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
