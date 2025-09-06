from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import *
from db import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Allowed origins (frontend URLs)
origins = [
    "http://localhost:5173",  # Vite dev server
    "http://localhost:3000",  # React dev server
]

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,       # allow these origins
    allow_credentials=True,
    allow_methods=["*"],         # allow GET, POST, PUT, etc.
    allow_headers=["*"],         # allow custom headers
)

@app.get("/<string:ticker>")
async def get_ticker():
    # Define a ticker
    return {"message": "Hello, FastAPI!"}


@app.get("/tickers/{symbol}")
def get_ticker(symbol: str):
    # Placeholder: fetch ticker data here
    return {
            "symbol": symbol,
            "last_price": 167.02,
            "currency": "USD",
            "change": -4.64,
            "percent_change": 2.7
        }

    

        