from reporting import get_figure
from pyspark.sql.types import StructType
import columns as c
from plotly.graph_objs import Figure


def test_visualize_results(spark):

    results_df = spark.createDataFrame(
        data=[
            (1, "Alice in Wonderland", 1800, 3, 6.333333333333333),
            (2, "The room", 1990, 3, 3.0),
            (3, "The house", 1996, 2, 9.5),
            (4, "Five dogs", 2020, 1, 6.0),
            (5, "Dracula", 1820, 5, 5.0),
            (6, "Bible", 1980, 2, 6.5),
            (7, "Bubble", 1980, 1, 9.0),
            (8, "The Caramel", 2020, 5, 6.0),
            (9, "The Cellphone", 1996, 5, 5.8),
        ],
        schema=StructType(
            [
                c.book_id,
                c.title,
                c.original_publication_year,
                c.reviews_count,
                c.average_rating,
            ]
        ),
    )

    graph = get_figure(results_df)

    assert isinstance(graph, Figure)
