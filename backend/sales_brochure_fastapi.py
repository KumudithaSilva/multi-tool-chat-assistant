from http.client import HTTPException

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI(title="Llama 3 Grocery AI Assistant API")


class URLRequest(BaseModel):
    """
    Request model for providing a base URL.
    """

    base_url: str


@app.post("/send_request")
def get_links(data: URLRequest):
    try:
        return {"request": data}

    except Exception as e:
        # Raise HTTPException to return proper HTTP status code (500)
        raise HTTPException(status_code=500, detail=f"Error fetching links: {str(e)}")


if __name__ == "__main__":
    uvicorn.run(
        host="127.0.0.1", port=8000, app="sales_brochure_fastapi:app", reload=True
    )
