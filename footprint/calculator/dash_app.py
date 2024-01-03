import dash
from dash import dcc, html
from django_plotly_dash import DjangoDash
import plotly.graph_objs as go


def create_dash_app(df):
    app = DjangoDash('SimpleExample')

    # Create a dropdown for year filter
    year_filter = dcc.Dropdown(
        id='year-filter',
        options=[{'label': year, 'value': year} for year in sorted(df['year'].unique())],
        value=df['year'].min(),
        style={'width': '150px', 'font-size': '16px'}
    )

    # Create a bar chart from the DataFrame
    graph = dcc.Graph(
        figure=go.Figure(
            data=[
                go.Bar(
                    x=df.drop(columns=['year', 'Total Emission']).columns,
                    y=df.drop(columns=['year', 'Total Emission']).values[0],
                )
            ]
        )
    )

    # Create a text box to display Total_Emission updated by year filter
    text_box = dcc.Input(
        id='total-emission',
        type='text',
        value=str(df[df['year'] == df['year'].min()]['Total Emission'].values[0]),
        disabled=True,
        style={'width': '200px', 'fontSize': '20px'}
    )

    # Add the dropdown, bar chart, and text box to the app's layout
    app.layout = html.Div(children=[
        year_filter,
        html.Br(), 
        html.Div(children=[
            html.Div(children=[
                text_box,
                html.Label('Total Emission (in ktCO2e)', style={'font-weight': 'bold'})
            ], style={'display': 'flex', 'flex-direction': 'row', 'align-items': 'center'}),
        ], style={'display': 'flex'}),
        graph
    ])

    return app