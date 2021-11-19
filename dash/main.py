'''
        Proyecto 2
        Dashboard

Creado por:

*   María Isabel Montoya Valladares 19169
*   Luis Pedro García Salazar 19344
*   María José Morales Reichenbach 19145
*   Juan Fernando de Leon Quezada  17822

'''
import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
import models

external_stylesheets = [
    'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css',
     dbc.themes.SLATE
]

siDesastre = pd.read_csv('../sd.csv')
noDesastre = pd.read_csv('../nd.csv')

# PRUEBAS  
covid_data_5 = {
        "Lat": [15.783471],
        "Long": [-90.230759]
    }

df = pd.DataFrame(covid_data_5)

fig = go.Figure(data=go.Scattergeo(
    lon=df['Long'],
    lat=df['Lat'],
    mode='markers',
))

# Instanciate the app
app = dash.Dash(__name__, external_stylesheets=external_stylesheets, meta_tags = [{"name": "viewport", "content": "width=device-width"}])

# Build the layout
app.layout = html.Div(
	children = [
		# (First row) Header: Logo - Title - Last updated
		html.Div(
			children = [
				# Logo
				html.Div(
					children = [
						html.Img(
							src = app.get_asset_url("logo.png"),
							id = "logo",
							style = {
								"height": "60px",
								"width": "auto",
								"margin-bottom": "25px"
							}
						)
					],
					className = "one-third column"
				),
				html.Div(
					children = [
						# Title and subtitle
						html.Div(
							children = [
								html.H3(
									children = "Proyecto 2",
									style = {
										"margin-bottom": "0",
										"color": "white"
									}
								),
								html.H5(
									children = "Desastres Naturales y Redes Sociales",
									style = {
										"margin-bottom": "0",
										"color": "white"
									}
								)
							]
						)
					],
					className = "one-half column",
					id = 'title'
				),
				# Last updated
				html.Div(
					children = [
						html.H6(
							children = "19/11/2021",
							style = {
								"color": "orange"
							}
						)
					],
					className = "one-thid column",
					id = "title1"
				)
			],
			id = "header",
			# className = "row flex-display",
			style = {
				"margin-bottom": "25px",
                "display": "flex",
                "flex-direction": "row",
                "justify-content": "center"
			}
		),
        # Title second row
        html.Div(
            children=[
                # Title
                html.H4(
                    children = "Proporción de Tweets",
                    style = {
                        "padding-left": "2rem",
                        "color": "white"
                    }
                )
            ]
        ),
        # (Second row) Cards: Global cases - Global deaths - Global recovered - Global active
		html.Div(
			children = [
				# (Column 1): Global cases
				html.Div(
					children = [
						# Title
						html.H6(
							children = "Tweets Reales",
							style = {
								"textAlign": "center",
								"color": "white"
							}
						),
						# Total value
						html.P(
							children = str(len(siDesastre)),
							style = {
								"textAlign": "center",
								"color": "orange",
								"fontSize": 40
							}
						),
					],
					className = "card_container three columns"
				),
				# (Column 2): Global deaths
				html.Div(
					children = [
						# Title
						html.H6(
							children = "Tweets NO Reales",
							style = {
								"textAlign": "center",
								"color": "white"
							}
						),
						# Total value
						html.P(
							children = str(len(noDesastre)),
							style = {
								"textAlign": "center",
								"color": "#dd1e35",
								"fontSize": 40
							}
						),
					],
					className = "card_container three columns"
				),
            ],
            style = {
                "display": "flex",
                "flex-direction": "row",
            }
        ),
        # Title third row
        html.Div(
            children=[
                # Title
                html.H4(
                    children = "Prediccion de Tweets",
                    style = {
                        "padding-left": "2rem",
                        "color": "white"
                    }
                )
            ]
        ),
        # (Third Row): Predict
        html.Div(
            children=[
                # Input
                html.Div(
                    children=[
                        # (Row 1) Country selector
						html.P(
							children = "Escribe un tweet: ",
							className = "fix_label",
							style = {
								"color": "white"
							}
						),
                        dcc.Input(
                            id="input_text",
                            type="text",
                            placeholder="Escribe algo...",
                            style={
                                "margin": "1rem",
                                "width": "75%"
                            }
                        )
                    ],
                    className = "card_container"
                )
            ]
        ),
        # Title Fourth Row
        html.Div(
            children=[
                # Title
                html.H4(
                    children = "Prediccion de modelos",
                    style = {
                        "padding-left": "2rem",
                        "color": "white"
                    }
                )
            ]
        ),
        # Title Fourth Row
        html.Div(
            children=[
                # Vectorizer + Multinomial NB Prediction Card
                html.Div(
                    children=[
                        html.P(
							children = "Vectorizer + Multinomial NB Prediction: ",
							className = "fix_label",
							style = {
								"color": "white"
							}
						),
                        html.Div(
                            children=[
                                html.I(
                                    id="mnb_check",
                                    className="fa fa-check-circle",
                                    style={
                                        "color": "green",
                                        "font-size": "8rem",
                                        "opacity": "0.25"
                                    }
                                ),
                                html.I(
                                    id="mnb_x",
                                    className="fa fa-times-circle",
                                    style={
                                        "color": "red",
                                        "font-size": "8rem",
                                        "opacity": "0.25"
                                    }
                                ),
                            ],
                            style={
                                "display": "flex",
                                "flex-direction": "row",
                                "justify-content": "space-around",
                                "width": "100%",
                                "padding": "2rem"
                            }
                        ),
                        # This is the label that change (1 Disaster, 0 Not a Disaster)
                        html.P(
                            id="multinomialNBPrediction",
                            style = {
								"textAlign": "center",
								"color": "orange",
								"fontSize": 15,
                                "margin-top": "1rem"
							}   
                        )
                    ],
                    className = "card_container three columns",
                    style={ "width": "50%" }
                ),
                # Vectorizer Tfidf Card
                html.Div(
                    children=[
                        html.P(
							children = "Vectorizer Tfidf: ",
							className = "fix_label",
							style = {
								"color": "white"
							}
						),
                        html.Div(
                            children=[
                                html.I(
                                    id="tfidf_check",
                                    className="fa fa-check-circle",
                                    style={
                                        "color": "green",
                                        "font-size": "8rem",
                                        "opacity": "0.25"
                                    }
                                ),
                                html.I(
                                    id="tfidf_x",
                                    className="fa fa-times-circle",
                                    style={
                                        "color": "red",
                                        "font-size": "8rem",
                                        "opacity": "0.25"
                                    }
                                ),
                            ],
                            style={
                                "display": "flex",
                                "flex-direction": "row",
                                "justify-content": "space-around",
                                "width": "100%",
                                "padding": "2rem"
                            }
                        ),
                        # This is the label that change (1 Disaster, 0 Not a Disaster)
                        html.P(
                            id="vectorizer_tfidf",
                            style = {
								"textAlign": "center",
								"color": "orange",
								"fontSize": 15,
                                "margin-top": "1rem"
							}   
                        )
                    ],
                    className = "card_container three columns",
                    style={ "width": "50%" }
                )
            ],
            style = {
                "display": "flex",
                "flex-direction": "row",
                "justify-content": "space-between"
            }
        ),
        # Fifth Row
        html.Div(
            children=[
                # Title
                html.H4(
                    children = "Tweet Locations",
                    style = {
                        "padding-left": "2rem",
                        "color": "white"
                    }
                )
            ]
        ),
        # Drop Down
        html.Div(
            children=[
                # Input
                html.Div(
                    children=[
                        # (Row 1) Country selector
						html.P(
							children = "Choose tweet types: ",
							className = "fix_label",
							style = {
								"color": "white"
							}
						),
                        dcc.Dropdown(
							id = "tweet_type",
							multi = False,
							searchable = True,
							value = "Real Tweets",
							placeholder = "Tweet Type",
							options = [{"label": "Real Tweets", "value": "Real Tweets"}, {"label": "Fake Tweets", "value": "Fake Tweets"}],
							className = "dcc_compon"
						),
                    ],
                    className = "create_container three columns"
                )
            ]
        ),
        # Map
        # (Fourth Row) Map
        html.Div(children=[
            dcc.Graph(
                id='map_chart',
                figure=fig
            )
        ])
    ],
    className="main__container"
)

@app.callback(
    [
        Output('multinomialNBPrediction','children'),
        Output('multinomialNBPrediction', 'style'),
        Output('vectorizer_tfidf','children'),
        Output('vectorizer_tfidf', 'style'),
        Output('mnb_check', 'style'),
        Output('mnb_x', 'style'),
        Output('tfidf_check', 'style'),
        Output('tfidf_x', 'style')
    ],
    [
        Input('input_text','value')
    ]
)
def predictions(tweet):
    '''Get multinomialNB prediction'''

    if tweet:

        VectorizeMultinomialNBPrediction = models.predictVectorizeMultinomialNB([tweet])
        VectorizerTfidfPrediction = models.predictVectorizerTfidf([tweet])

        mnb_check_style = {
            "color": "green",
            "font-size": "8rem",
            "opacity": "0.25"
        }

        mnb_x_style = {
            "color": "red",
            "font-size": "8rem",
            "opacity": "0.25"
        }

        tfidf_check_style = {
            "color": "green",
            "font-size": "8rem",
            "opacity": "0.25"
        }

        tfidf_x_style = {
            "color": "red",
            "font-size": "8rem",
            "opacity": "0.25"
        }

        VectorizeMultinomialNBStyle = {
            "textAlign": "center",
            "color": "red",
            "fontSize": 15,
            "margin-top": "1rem"
        }

        VectorizerTfidfStyle = {
            "textAlign": "center",
            "color": "red",
            "fontSize": 15,
            "margin-top": "1rem"
        }

        vectorizeMultinomialNBPrediction_real = "NOT Real Tweet"
        VectorizerTfidfPrediction_real = "NOT Real Tweet"

        if VectorizeMultinomialNBPrediction[0] == 1:
            mnb_check_style = {
                "color": "green",
                "font-size": "8rem",
                "opacity": "1"
            }

            vectorizeMultinomialNBPrediction_real = "Real Tweet"
            VectorizeMultinomialNBStyle = {
                "textAlign": "center",
                "color": "green",
                "fontSize": 15,
                "margin-top": "1rem"
            }
        else:
            mnb_x_style = {
                "color": "red",
                "font-size": "8rem",
                "opacity": "1"
            }

        
        if VectorizerTfidfPrediction[0] == 1:
            tfidf_check_style = {
                "color": "green",
                "font-size": "8rem",
                "opacity": "1"
            }
            VectorizerTfidfPrediction_real = "Real Tweet"
            VectorizerTfidfStyle = {
                "textAlign": "center",
                "color": "green",
                "fontSize": 15,
                "margin-top": "1rem"
            }
        else:
            tfidf_x_style = {
                "color": "red",
                "font-size": "8rem",
                "opacity": "1"
            }
        
        return vectorizeMultinomialNBPrediction_real, VectorizeMultinomialNBStyle, VectorizerTfidfPrediction_real, VectorizerTfidfStyle, mnb_check_style, mnb_x_style, tfidf_check_style, tfidf_x_style

    return

# Map
@app.callback(
	Output(
		component_id = "map_chart",
		component_property = "figure"
	),
	Input(
		component_id = "tweet_type",
		component_property = "value"
	)
)
def update_map(tweet_type):

    # !TODO: Pasar todas las latitudes y longitudes al df completo

    # PRUEBAS  
    covid_data_5 = {
            "Lat": [15.783471],
            "Long": [-90.230759]
        }

    df = siDesastre

    if tweet_type == "Real Tweets":
        fig = go.Figure(data=go.Scattergeo(
            lon=df['long'],
            lat=df['lat'],
            mode='markers',
        ))
    elif tweet_type == "Fake Tweets":
        # 19.42847 y longitud -99.12766

        covid_data_5 = {
            "Lat": [19.42847],
            "Long": [-99.12766]
        }

        df = noDesastre

        fig = go.Figure(data=go.Scattergeo(
            lon=df['long'],
            lat=df['lat'],
            mode='markers',
        ))

    return fig



# Run the app
if __name__ == "__main__":
  app.run_server(debug = True)