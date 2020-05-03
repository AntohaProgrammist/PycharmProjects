import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html


stylesheets = ['https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css']
app = dash.Dash(external_stylesheets=stylesheets)

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
            html.P("Скорость в относительном движении перед рабочей лопаткой, [м/с]"),
            dcc.Input(id='w_1', value=314, type="number"),
            html.P("Скорость в относительном движении за рабочей лопаткой, [м/с]"),
            dcc.Input(id='w_2', value=371, type="number"),
            html.P("Хорда лопатки, [мм]"),
            dcc.Input(id='B', value=30, type="number"),
            html.P("Угол в относительном движении в сечении перед рабочей лопаткой, [град.]"),
            dcc.Input(id='beta_1', value=38, type="number"),
            html.P("Угол в относительном движении в сечении за рабочей лопаткой, [град.]"),
            dcc.Input(id='beta_2', value=30, type="number"),
            html.P("Установочный угол, [град.]"),
            dcc.Input(id='beta_y', value=80, type="number"),

            html.P("Угол раскрытия на входе в лопатка, [град.]"),
            dcc.Input(id='gamma_1', value=30, type="number"),
            html.P("Угол раскрытия на выходе в лопатка, [град.]"),
            dcc.Input(id='gamma_2', value=4, type="number"),
            html.P("Радиус скругления входной кромки, [мм]"),
            dcc.Input(id='radius_1', value=4, type="number"),
            html.P("Радиус скругления выходной кромки, [мм]"),
            dcc.Input(id='radius_2', value=4, type="number"),
        ], width=4),

        dbc.Col([
            html.H6("Лопатка"),
            # График
        ], width=True),

    ], align="end"),
], fluid=True)

app.run_server()
