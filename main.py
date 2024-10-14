import uvicorn
from fastapi import FastAPI, responses

import src.Utils as Utils
import src.DB as DB
import src.Router as Router


DB.create_tables(drop_existing=True)

app = FastAPI(
    **{
        "title": "THD(c)",
        "summary": "Cryptocurrency trading training application Backend",
        "version": "0.0.0",
        "openapi_tags": [
            {
                "name": "User",
                "description": "User account related endpoints",
            },
        ],
    }
)
app.include_router(Router.user_router)

Utils.OTEL.instrument_fastapi(app)


@app.get("/", response_class=responses.HTMLResponse)
async def base():
    """
    Default Page
    """
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
