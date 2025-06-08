from pathlib import Path

# Base paths
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
MODEL_DIR = BASE_DIR / "models"

# Create necessary directories
DATA_DIR.mkdir(exist_ok=True)
(DATA_DIR / "raw").mkdir(exist_ok=True)
(DATA_DIR / "processed").mkdir(exist_ok=True)
(DATA_DIR / "embeddings").mkdir(exist_ok=True)
MODEL_DIR.mkdir(exist_ok=True)

# Model settings
EMBEDDING_MODEL = "sentence-transformers/all-mpnet-base-v2"
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200

# API settings
API_HOST = "0.0.0.0"
API_PORT = 8000