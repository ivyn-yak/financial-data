
# Financial Dashboard

## Project Set Up

### APIs to Retrieve Data 
**Note:** Alpha Vantage API key offers up to 25 requests per day
- [Alpha Vantage Stock Market API](https://www.alphavantage.co/documentation/)  
- [yfinance Python package](https://ranaroussi.github.io/yfinance/)

### Set Up .env
```
    # Postgres
    POSTGRES_USER= <postgres>
    POSTGRES_PASSWORD= <secret>
    POSTGRES_DB= <mydb>

    # Backend
    ALPHA_VANTAGE_API_KEY= <your_alpha_vantage_key>
    DATABASE_URL= <postgres://postgres:secret@postgres_db:5432/mydb>

    # Frontend - Do not edit
    VITE_BACKEND_URL=http://backend:8000

```

### Run on Docker

```
docker-compose up
docker-compose down -v
```

### Run Locally

Git Clone

```bash
  git clone https://github.com/ivyn-yak/financial-data.git
```
    
Run frontend

```bash
  cd frontend
  npm install
  npm run dev
```

Run backend

```bash
  cd backend
  python -m venv venv
  source venv/bin/activate
  pip install -r requirements.txt

  python run_pipeline.py
  uvicorn main:app --reload
```




## Data Retrieved
### Market Data (from yfinance)
- Quote
- Historical Stock Price (3 months)

### Financial Data (from Alpha Vantage)
- Balance Sheet
- Income Statement
- Cash Flow Statement

### Alternative Data (from Alpha Vantage)
- News (with ticker sentiments)

### Company-Related Data (from Alpha Vantage)
- Earnings Calls Transcript (with segment sentiments)

## Features
### Data Pipeline
A data pipeline is executed automatically - retrieve, process, and store data into the PostgreSQL database:

1. **Fetch** raw data from Alpha Vantage APIs (financials, news, transcripts).  
2. **Preprocess** the data (cleaning and normalisation).  
3. **Load** the processed data into the database with proper schemas.  
4. **Serve** the data through FastAPI endpoints for the frontend to consume.  

### Web Application
In addition to historical data, realtime data is fetched via yfinance and visualized across various web pages.

#### Home Page
Historical Price over a period of 3 months. Candlestick chart using `chartjs-chart-financial`.

![onload](/frontend/public/stockchart.png)

Key Statistics 

![onload](/frontend/public/keystats.png)

#### Performance Page
Stock price with S&P 500 as a performance benchmark. Line graph using `chartjs`.

![onload](/frontend/public/performance.png)

#### Financials Page
Balance Sheet, Income Statement and Cash Flow (Quarterly and Annual Data)

![onload](/frontend/public/balance.png)

#### News Page
Relevant news with ticker sentiments. News and sentiments from Alpha Vantage.

![onload](/frontend/public/news.png)

#### Events/Transcript Page
Earnings call transcripts with metrics sidebar. Transcript and segment sentiments from Alpha Vantage.

![onload](/frontend/public/news.png)
