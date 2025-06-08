import uvicorn
from src.api.endpoints import app
from config import API_HOST, API_PORT

if __name__ == "__main__":
    uvicorn.run(app, host=API_HOST, port=API_PORT)