from dash import Dash, html, dcc, Input, Output
import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv("formatted_sales_data.csv")

# Convert date column to datetime
df["date"] = pd.to_datetime(df["date"])

# Initialize app
app = Dash(__name__)

# Layout
app.layout = html.Div(
    children=[
        html.H1(
            "Soul Foods Pink Morsel Sales Dashboard",
            style={
                "textAlign": "center",
                "color": "#2c3e50",
                "padding": "20px"
            }
        ),

        html.Div(
            [
                html.Label(
                    "Select Region:",
                    style={
                        "fontSize": "18px",
                        "fontWeight": "bold",
                        "marginRight": "15px"
                    }
                ),

                dcc.RadioItems(
                    id="region-selector",
                    options=[
                        {"label": "All", "value": "all"},
                        {"label": "North", "value": "north"},
                        {"label": "East", "value": "east"},
                        {"label": "South", "value": "south"},
                        {"label": "West", "value": "west"},
                    ],
                    value="all",
                    inline=True,
                ),
            ],
            style={
                "padding": "20px",
                "backgroundColor": "#f8f9fa",
                "borderRadius": "10px",
                "marginBottom": "20px"
            }
        ),

        dcc.Graph(id="sales-chart")
    ],
    style={
        "width": "90%",
        "margin": "auto",
        "fontFamily": "Arial, sans-serif"
    }
)


@app.callback(
    Output("sales-chart", "figure"),
    Input("region-selector", "value")
)
def update_chart(selected_region):

    # Filter by region
    if selected_region == "all":
        filtered_df = df.copy()
    else:
        filtered_df = df[
            df["region"].str.lower() == selected_region
        ]

    # Aggregate sales by date
    sales_by_date = (
        filtered_df.groupby("date")["sales"]
        .sum()
        .reset_index()
        .sort_values("date")
    )

    # Create line chart
    fig = px.line(
        sales_by_date,
        x="date",
        y="sales",
        markers=True,
        title=f"Pink Morsel Sales Trend - {selected_region.title()}"
    )

    fig.update_layout(
        xaxis_title="Date",
        yaxis_title="Sales",
        template="plotly_white",
        title_x=0.5
    )

    return fig


if __name__ == "__main__":
    app.run(debug=True)