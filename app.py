import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.express as px

# Load data
df = pd.read_csv("output.csv")
df["date"] = pd.to_datetime(df["date"], format="mixed", dayfirst=True)
df = df.sort_values("date")

# Initialize Dash app
app = Dash(__name__)

app.layout = html.Div(
    className="app-container",
    children=[
        html.H1(
            "Pink Morsel Sales Visualiser",
            style={"textAlign": "center"}
        ),

        html.Div(
            className="radio-container",
            children=[
                dcc.RadioItems(
                    id="region-filter",
                    options=[
                        {"label": "All", "value": "all"},
                        {"label": "North", "value": "north"},
                        {"label": "East", "value": "east"},
                        {"label": "South", "value": "south"},
                        {"label": "West", "value": "west"},
                    ],
                    value="all",
                    inline=True
                )
            ]
        ),

        html.Div(
            className="graph-container",
            children=[
                dcc.Graph(id="sales-line-chart")
            ]
        )
    ]
)

@app.callback(
    Output("sales-line-chart", "figure"),
    Input("region-filter", "value")
)
def update_chart(selected_region):
    if selected_region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["region"] == selected_region]

    fig = px.line(
        filtered_df,
        x="date",
        y="Sales",
        labels={
            "date": "Date",
            "Sales": "Total Sales ($)"
        },
        title="Pink Morsel Sales Over Time"
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

    return fig


if __name__ == "__main__":
    app.run(debug=True)
