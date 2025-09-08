from db import Base, engine
from api.pipeline import DataPipeline
import os
from dotenv import load_dotenv

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

if __name__ == "__main__":
    main()