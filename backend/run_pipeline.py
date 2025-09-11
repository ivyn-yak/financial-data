from db import Base, engine
from api.pipeline import DataPipeline
import os
from dotenv import load_dotenv
from functools import wraps
from db import SessionLocal

load_dotenv()

Base.metadata.create_all(bind=engine)

def main():
    try:
        pipeline = DataPipeline(os.getenv("ALPHA_VANTAGE_API_KEY"))
        print("Starting data pipeline...")
        pipeline.run_all_by_symbol("NVDA") #Retrieves Nvidia's company data, financial statements, and news sentiment 
        quarters = ["2025Q2", "2025Q1", "2024Q4", "2024Q3", "2024Q2", "2024Q1"]
        for quarter in quarters:
            pipeline.run_earnings_call("NVDA", quarter)
    except Exception as e:
        print(f"An error occurred: {e}")

def load_mock_data(filepath):
    import json
    with open(filepath, 'r') as file:
        data = json.load(file)
    return data

def with_session(commit: bool = True):
    """
    Decorator to automatically create a SQLAlchemy session,
    pass it to the decorated function, and close it after.
    If commit=True, it will commit the session.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            session = SessionLocal()
            try:
                # Pass the session as a keyword argument
                result = func(*args, db=session, **kwargs)
                if commit:
                    session.commit()
                return result
            except Exception as e:
                session.rollback()
                raise e
            finally:
                session.close()
        return wrapper
    return decorator

@with_session(commit=True)
def insert_mock_data(db=None):
    from api.transform_data import TransformData
    from api.load_data import LoadData
    from schemas import IncomeStatementInput, BalanceSheetInput, CashFlowStatementInput

    transformer = TransformData()
    loader = LoadData()

    filepaths = {
        "company": "./samples/NVDA_OVERVIEW.json",
        "income_statement": "./samples/NVDA_INCOME_STATEMENT.json",
        "balance_sheet": "./samples/NVDA_BALANCE_SHEET.json",
        "cash_flow": "./samples/NVDA_CASH_FLOW.json",
        "news": "./samples/news_NVDA.json",
        "transcript": ["./samples/NVDA_transcript_q2025Q2.json", "./samples/NVDA_transcript_q2025Q1.json"]
    }

    # Company overview
    company_data = load_mock_data(filepaths["company"])
    processed_company = transformer.get_company_schema(company_data)
    loader.insert_company(db, processed_company)

    # Financials
    income_data = load_mock_data(filepaths["income_statement"])
    processed_income = transformer.get_financials_schema(income_data, IncomeStatementInput)
    loader.batch_insert_income_statement(db, processed_income)

    balance_data = load_mock_data(filepaths["balance_sheet"])
    processed_balance = transformer.get_financials_schema(balance_data, BalanceSheetInput)
    loader.batch_insert_balance_sheet(db, processed_balance)

    cashflow_data = load_mock_data(filepaths["cash_flow"])
    processed_cashflow = transformer.get_financials_schema(cashflow_data, CashFlowStatementInput)
    loader.batch_insert_cash_flow(db, processed_cashflow)

    # News
    news_data = load_mock_data(filepaths["news"])
    processed_news = transformer.get_news_articles_schema(news_data)
    loader.batch_insert_news(db, processed_news)

    # Transcripts
    for transcript_path in filepaths["transcript"]:
        transcript_data = load_mock_data(transcript_path)
        processed_transcript = transformer.get_earnings_call_schema(transcript_data)
        loader.batch_insert_earnings_transcript(db, processed_transcript)

if __name__ == "__main__":
    main()
    # Run this instead of main() to insert mock data into the database
    # insert_mock_data() 