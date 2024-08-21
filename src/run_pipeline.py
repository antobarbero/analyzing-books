from data_ingestion import ingest_data
from data_cleaning import clean_data
from data_transformation import transform_data
from reporting import visualize_results


def run_pipeline() -> None:
    """"""
    # Data ingestion
    file_path = ".\\datasets"
    raw_data = ingest_data(file_path)

    # Data cleaning
    clean_data_df = clean_data(raw_data)

    # Data transformation
    transformed_data = transform_data(clean_data_df)

    # Visualization and reporting
    visualize_results(transformed_data)


if __name__ == "__main__":
    run_pipeline()
