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
		)]
)

# Run the app
if __name__ == "__main__":
  app.run_server(debug = True)