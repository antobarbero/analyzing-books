from data_ingestion import ingest_data
from data_cleaning import clean_data
from data_transformation import get_books_popularity_overtime
from reporting import visualize_results
import logging

logging.basicConfig(filename="..\\pipeline.log", level=logging.INFO)
logger = logging.getLogger(__name__)


def run_pipeline(files_path: str = "..\\datasets") -> None:
    logger.info("Pipeline run starting...")

    logger.info(f"Loading data from {files_path}")
    raw_dataset = ingest_data(files_path)

    logger.info("Cleaning data.")
    clean_data_set = clean_data(raw_dataset)

    logger.info("Analyzing data.")
    transformed_data = get_books_popularity_overtime(
        clean_data_set.books_df, clean_data_set.ratings_df
    )

    logger.info("Preparing visualization.")
    visualize_results(transformed_data)


if __name__ == "__main__":
    run_pipeline()
