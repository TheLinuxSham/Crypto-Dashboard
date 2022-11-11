# importieren der libraries
import dash
import plotly.express as px
from dash import dash_table
from dash import dcc
from dash import html
from dash.dependencies import Output, Input

# importieren der anderen *.py
from crypto_api import get_crypto_dataframes
from sentiment_api import get_sentiment_dataframes
from twitter_api import get_twitter_dataframes

# importiert die Pandas-Dateien (pd) von anderen *.py in das Hauptprogramm
dataframe_twitter = get_twitter_dataframes()
dataframe_sentiment = get_sentiment_dataframes()
historical_df, avg_df, crypto_data_df = get_crypto_dataframes()

# Hauptprogramm mit Dashboard

# 6.APP-Layout

app = dash.Dash(__name__)

docker = True
server = app.server

app.layout = html.Div([
    html.H1('Crypto-Info 2022', style={'textAlign': 'center'}),
    dcc.Dropdown(id='Währung', placeholder='Please select Currency',
                 options=[{'label': x, 'value': x}
                          for x in sorted(historical_df.Währung.unique())],
                 style={'width': '40%'}
                 ),
    dash_table.DataTable(
        id='Table-Daten',
        columns=[
            {'name': 'Rank', 'id': 'market_cap_rank'},
            {'name': 'Current Price ($)', 'id': 'current_price'},
            {'name': 'Price Change 24h (%)', 'id': 'price_change_percentage_24h'},
            {'name': '24h High ($)', 'id': 'high_24h'},
            {'name': '24h Low ($)', 'id': 'low_24h'},
            {'name': 'Market-Cap ($)', 'id': 'market_cap'},
            {'name': 'All Time High ($)', 'id': 'ath'},
            {'name': 'All Time High Change (%)', 'id': 'ath_change_percentage'},
            {'name': 'All Time High Timestamp', 'id': 'ath_date', 'type': 'datetime'}

        ],

    ),
    dash_table.DataTable(
        id='Table-Average',
        columns=[
            {'name': 'Price ø each day', 'id': 'USD'},
            {'name': 'Traded Coins ø each day', 'id': 'Volume'},
            {'name': 'Trades ø each day', 'id': 'Count'}

        ],
        style_table={'width': '38%'},

    ),
    html.Div(children=[
        dcc.Graph(id='Preis-Graph',
                  figure={},
                  style={'width': '50%', 'display': 'inline-block'}
                  ),
        dcc.Graph(id='Trend-Graph',
                  figure={},
                  style={'width': '50%', 'display': 'inline-block'}
                  )
    ]),

    html.Div(children=[
        dcc.Graph(id='Volume-Graph',
                  figure={},
                  style={'width': '50%', 'display': 'inline-block'}
                  ),
        dcc.Graph(id='Anzahl-Graph',
                  figure={},
                  style={'width': '50%', 'display': 'inline-block'}
                  )
    ]),
    html.Div([
        html.Div([
            dash_table.DataTable(
                id='Table-Tweets',
                columns=[{'name': 'Tweets', 'id': 'Tweets'}, ],
                style_table={'height': '200', 'overflowX': 'auto'},
                style_cell={'textAlign': 'left'},

            )

        ], style={'width': '49%', 'display': 'inline-block'}),

        html.Div([

            dcc.Graph(id='Sentiment-Bar',
                      figure={})

        ], style={'width': '49%', 'display': 'inline-block'}),

    ], style={'display': 'flex', 'horizontalAlign': 'bottom'}),

])


@app.callback(
    Output(component_id='Table-Daten', component_property='data'),
    Output(component_id='Table-Average', component_property='data'),
    Output(component_id='Preis-Graph', component_property='figure'),
    Output(component_id='Trend-Graph', component_property='figure'),
    Output(component_id='Volume-Graph', component_property='figure'),
    Output(component_id='Anzahl-Graph', component_property='figure'),
    Output(component_id='Table-Tweets', component_property='data'),
    Output(component_id='Sentiment-Bar', component_property='figure'),
    Input(component_id='Währung', component_property='value')
)
def generate(Währung):
    df1 = crypto_data_df[crypto_data_df.Währung == Währung]
    df2 = historical_df[historical_df.Währung == Währung]
    df3 = avg_df[avg_df.Währung == Währung]
    df4 = dataframe_twitter[dataframe_twitter.Währung == Währung]
    df5 = dataframe_sentiment[dataframe_sentiment.Währung == Währung]
    fig = px.line(data_frame=df2, x='Timestamp', y='USD', title='Price in USD', color_discrete_sequence=['black'])
    fig1 = px.bar(data_frame=df2, x='Timestamp', y='Volume', title='Count of traded Coins')
    fig2 = px.bar(data_frame=df2, x='Timestamp', y='Count', title='Count Trades')
    fig3 = px.scatter(df2, x='Timestamp', y='USD', title='Trend', trendline="ols", color_discrete_sequence=['black'],
                      trendline_color_override="blue")
    fig4 = px.bar(df5, x='Währung', y=['Positive', 'Neutral', 'Negative'], barmode='group', title='Twitter Sentiment',
                  color_discrete_map={'Positive': 'green', 'Neutral': 'grey', 'Negative': 'red'})

    return df1.to_dict('records'), df3.to_dict('records'), fig, fig3, fig1, fig2, df4.to_dict('records'), fig4


# Initiierung über Docker
if __name__ == "__main__":
    if docker:
        app.run_server(debug=True, host="0.0.0.0", port=8080, use_reloader=False)
    else:
        app.run_server(host='0.0.0.0', debug=True)
