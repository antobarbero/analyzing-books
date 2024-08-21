from data_ingestion import ingest_data
from data_cleaning import clean_data
from data_transformation import transform_data
from reporting import visualize_results
import logging

logging.basicConfig(filename="..\\pipeline.log", level=logging.INFO)
logger = logging.getLogger(__name__)


def run_pipeline() -> None:

    logger.info("Pipeline run starting...")

    file_path = "..\\datasets"
    logger.info(f"Loading data from {file_path}")
    raw_data = ingest_data(file_path)

    logger.info("Cleaning data.")
    clean_data_df = clean_data(raw_data)

    logger.info("Analyzing data.")
    transformed_data = transform_data(clean_data_df)

    logger.info("Preparing visualization.")
    visualize_results(transformed_data)


if __name__ == "__main__":
    run_pipeline()
