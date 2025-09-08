from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import *
from db import Base, engine
from api.routes import company, stock_price, balance_sheet, news, income_statement, cash_flow, perfomance, earnings

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Allowed origins (frontend URLs)
origins = [
    "http://localhost:5173",  # Vite dev server
    "http://localhost:3000",  # React dev server
]

# include routers
app.include_router(company.router)
app.include_router(stock_price.router)
app.include_router(balance_sheet.router)
app.include_router(news.router)
app.include_router(income_statement.router)
app.include_router(cash_flow.router)
app.include_router(perfomance.router)
app.include_router(earnings.router)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,       # allow these origins
    allow_credentials=True,
    allow_methods=["*"],         # allow GET, POST, PUT, etc.
    allow_headers=["*"],         # allow custom headers
)

@app.get("/")
def root():
    return {"message": "API is running 🚀"}


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
