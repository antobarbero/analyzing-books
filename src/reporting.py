from pyspark.sql import DataFrame
from plotly.graph_objs import Figure
import pandas as pd
import attribute_names as an


def get_figure(transformed_data: DataFrame) -> Figure:
    pd.options.plotting.backend = "plotly"
    fig = transformed_data.toPandas().plot.bar(x=an.TITLE, y=an.AVERAGE_RATING)
    return fig
