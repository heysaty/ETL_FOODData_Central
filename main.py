from pipeline import run_pipeline

if __name__ == "__main__":
    response = input("Yes! if u want to run scraper seperately else just enter to run scraper along ETL Pipeline : \n")
    if response.lower() == 'yes':
        run_pipeline('scraper')
    else:
        run_pipeline('All')

