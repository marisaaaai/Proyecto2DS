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
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
import models

siDesastre = pd.read_csv('siDesastre.csv')
noDesastre = pd.read_csv('noDesastre.csv')



# Instanciate the app
app = dash.Dash(__name__, meta_tags = [{"name": "viewport", "content": "width=device-width"}])

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
			className = "row flex-display",
			style = {
				"margin-bottom": "25px"
			}
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
            ]
        ),
        # (Third Row): Predict
        html.Div(
            children=[
                html.Div(
                    children=[
                        # (Row 1) Country selector
						html.P(
							children = "Escribe algo: ",
							className = "fix_label",
							style = {
								"color": "white"
							}
						),
                        dcc.Input(
                            id="input_text",
                            type="text",
                            placeholder="Escribe algo...",
                            style={"margin": "1rem"}
                        )
                    ],
                    className = "card_container three columns"
                ),
                html.Div(
                    children=[
                        html.P(
							children = "Vectorizer + Multinomial NB Prediction: ",
							className = "fix_label",
							style = {
								"color": "white"
							}
						),
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
                    className = "card_container three columns"
                )
            ]
        )
    ],
    className="main__container"
)

@app.callback(
    [
        Output('multinomialNBPrediction','children'),
        Output('multinomialNBPrediction', 'style')
    ],
    [
        Input('input_text','value')
    ]
)
def multinomialNBPred(tweet):
    '''Get multinomialNB prediction'''

    if tweet:

        prediction = models.predictVectorizeMultinomialNB([tweet])

        style = {
            "textAlign": "center",
            "color": "green",
            "fontSize": 15,
            "margin-top": "1rem"
        }

        if prediction[0] == 1:
            style = {
                "textAlign": "center",
                "color": "red",
                "fontSize": 15,
                "margin-top": "1rem"
            }
        
        return str(prediction[0]), style

    return


# Run the app
if __name__ == "__main__":
  app.run_server(debug = True)