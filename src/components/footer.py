from dash import html

def create_footer():
    footer = html.Footer(
        children=[
            html.Div("© Mon Application Dash", style={'textAlign': 'center'}),
        ],
        style={'padding': '10px', 'backgroundColor': '#f8f9fa', 'position': 'fixed', 'width': '100%', 'bottom': '0'}
    )
    return footer
