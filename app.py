import pandas as pd
from dash import Dash, dcc, html
import plotly.express as px

# Load data
df = pd.read_csv("output.csv")

# Convert date column
df["date"] = pd.to_datetime(df["date"])

# Sort by date
df = df.sort_values("date")

# Line chart
fig = px.line(
    df,
    x="date",
    y="Sales",
    title="Pink Morsel Sales Over Time",
    labels={
        "date": "Date",
        "Sales": "Total Sales ($)"
    }
)

# Price increase marker
price_increase_date = pd.to_datetime("2021-01-15")

fig.add_shape(
    type="line",
    x0=price_increase_date,
    x1=price_increase_date,
    y0=0,
    y1=1,
    xref="x",
    yref="paper",
    line=dict(color="red", dash="dash")
)

fig.add_annotation(
    x=price_increase_date,
    y=1,
    xref="x",
    yref="paper",
    text="Price Increase (15 Jan 2021)",
    showarrow=False,
    yanchor="bottom"
)

# Dash app
app = Dash(__name__)

app.layout = html.Div(
    [
        html.H1(
            "Pink Morsel Sales Visualiser",
            style={"textAlign": "center"}
        ),
        dcc.Graph(figure=fig)
    ]
)

if __name__ == "__main__":
    app.run(debug=True)

