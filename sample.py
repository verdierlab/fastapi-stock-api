"""
Run the API locally.

Open your browser:

http://127.0.0.1:8000

Swagger UI:

http://127.0.0.1:8000/docs

ReDoc:

http://127.0.0.1:8000/redoc
"""

import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        "stock_api:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
    )
