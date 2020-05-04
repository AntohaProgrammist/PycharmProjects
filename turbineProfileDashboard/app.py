import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output
from main import Blade
import plotly.graph_objects as go
from random import randint
from flask import Flask

stylesheets = ['https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css']
server = Flask(__name__)
app = dash.Dash(
    __name__,
    external_stylesheets=stylesheets,
    server=server
    # external_stylesheets=[dbc.themes.SKETCHY]
)

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H2("Прекрасный профиль лопатки турбины"),
            html.H5("Курнухин Антон"),
        ], width=True),
    ], align="end"),

    html.Hr(),

    dbc.Row([
        dbc.Col([
            html.H6("Параметры"),
            html.Hr(),
            html.P("Хорда лопатки, [мм]", style={"margin-bottom": "0"}),
            dcc.Input(id='B', value=randint(20, 40), type="number", className="form-control"),
            html.P("Угол в относительном движении в сечении перед рабочей лопаткой, [град.]", style={"margin-bottom": "0"}),
            dcc.Input(id='beta_1', value=randint(15, 50), type="number", className="form-control"),
            html.P("Угол в относительном движении в сечении за рабочей лопаткой, [град.]", style={"margin-bottom": "0"}),
            dcc.Input(id='beta_2', value=randint(15, 50), type="number", className="form-control"),
            html.P("Установочный угол, [град.]", style={"margin-bottom": "0"}),
            dcc.Input(id='beta_y', value=randint(45, 90), type="number", className="form-control"),

            html.P("Угол раскрытия на входе в лопатка, [град.]", style={"margin-bottom": "0"}),
            dcc.Input(id='gamma_1', value=randint(8, 30), type="number", className="form-control"),
            html.P("Угол раскрытия на выходе в лопатка, [град.]", style={"margin-bottom": "0"}),
            dcc.Input(id='gamma_2', value=randint(4, 8), type="number", className="form-control"),
            html.P("Радиус скругления входной кромки, [мм]", style={"margin-bottom": "0"}),
            dcc.Input(id='radius_1', value=1, className="form-control"),
            html.P("Радиус скругления выходной кромки, [мм]", style={"margin-bottom": "0"}),
            dcc.Input(id='radius_2', value=0.5, className="form-control"),
        ], width=4, style={'height': '100%'}),

        dbc.Col([
            html.H6("Лопатка"),
            html.Hr(),
            dcc.Graph(id='display', style={
                'height': '70vh'
            })
        ], width=8, align="top"),

    ], align="top"),

    dbc.Row([
        dbc.Col([
            html.Hr(),
            html.P(["Если хотите смешной анекдот про лопатку, не пишите мне. ",
                    html.A("telegram", href="https://t.me/antonkkkkk")]),
            html.Hr(),
        ], width=True, align="end"),
    ], justify='center'),
], fluid=False)


@app.callback(
    [Output('display', 'figure')],
    [
        Input('B', 'value'), Input('beta_1', 'value'),
        Input('beta_2', 'value'), Input('beta_y', 'value'),
        Input('gamma_1', 'value'), Input('gamma_2', 'value'),
        Input('radius_1', 'value'), Input('radius_2', 'value')
    ]
)
def main_calc(
        B, beta_1, beta_2, beta_y,
        gamma_1, gamma_2, radius_1, radius_2
):
    w_1 = 10
    w_2 = 10
    beta_y = 180 - beta_y
    lopatka = Blade(
        B,
        beta_1,
        beta_2,
        beta_y,
        gamma_1,
        gamma_2,
        w_1,
        w_2,
        float(radius_1),
        float(radius_2)
    )
    lopatka.calc()

    x, y = lopatka.return_coords()

    fig = dict({
        "data": [
            {
                "type": "scatter",
                "x": x.tolist(),
                "y": y.tolist()
            }
        ],
        "layout": {
            # "title": {"text": "A Figure Specified By Python Dictionary"},
            "xaxis": dict(range=[-30, 30]),
            "yaxis": dict(scaleanchor="x", scaleratio=1),  # dict(range=[-30, 30]),
            "autosize": True,
            "source": "https://images.plot.ly/language-icons/api-home/python-logo.png",
        }
    })
    fig = go.Figure(
        data=[
            {
                "type": "scatter",
                "x": x.tolist(),
                "y": y.tolist()
            }
        ],
        layout={
            # "title": {"text": "A Figure Specified By Python Dictionary"},
            "xaxis": dict(range=[-30, 30]),
            "yaxis": dict(scaleanchor="x", scaleratio=1),  # dict(range=[-30, 30]),
            "autosize": True,
            # "source": "https://images.plot.ly/language-icons/api-home/python-logo.png",
        }
    )
    # fig.add_layout_image(
    #     dict(
    #         xref="x",
    #         yref="y",
    #         layer="below",
    #         sizing="stretch",
    #         opacity=.3,
    #         source="images/koteika.jpg"
    #     )
    # )
    # fig.add_layout_image(
    #     dict(
    #         source="images/koteika.png",
    #         xref="x",
    #         yref="y",
    #         x=-5,
    #         y=3,
    #         sizex=1,
    #         sizey=1,
    #         sizing="stretch",
    #         opacity=0.5,
    #         layer="below"
    #     )
    # )
    # fig.update_layout(
    #     template="plotly_white"
    # )

    return [fig]


app.title = 'Лопатка'
# app.run_server()
