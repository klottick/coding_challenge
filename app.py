from dash import Dash, Input, Output, html, dcc, State, ctx
import dash_bootstrap_components as dbc
import os

from coding_challenge.questions import *
from utils import get_function_text_from_file
import subprocess
from subprocess import CalledProcessError
from typing import Type, Tuple


PORT = 8050
HOST = "localhost"
QUESTIONS_PATH = os.path.join("coding_challenge", "questions.py")
NUM_QUESTIONS = 5
DEBUG = False

"""
    Used documentation from 
    https://dash-bootstrap-components.opensource.faculty.ai/
    https://dash.plotly.com/
    to check syntax, but I did not take any code blocks
    
    I had to look up how to get stdout from python thinking I could do it with with os module, but 
    https://stackoverflow.com/questions/18739239/python-how-to-get-stdout-after-running-os-system
    indicated I had to use subprocess
    
    For the colors, I used 
    https://colorhunt.co/palette/82aae391d8e4bfeaf5eafdfc
    
    I also was having trouble styling the background of the markdown for the css which led me to looking this up:
    https://github.com/plotly/dash-core-components/issues/664
"""

app = Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    suppress_callback_exceptions=True,
)

# Sidebar definition

sidebar = html.Div(
    [
        html.H3("Sections"),
        html.Hr(),
        dbc.Nav(
            [
                dbc.NavLink("Home", href="/", active="exact"),
            ]
            + [
                dbc.NavLink(f"Question {i}", href=f"/question_{i}", active="exact")
                for i in range(1, NUM_QUESTIONS + 1)
            ],
            vertical=True,
            pills=True,
        ),
    ],
    className="sidebar-container",
)

# Main content definitions


content_area = html.Div(id="content-area")

home_content = dbc.CardBody(
    html.H1(
        "Use this tool to view the results of the tests for the coding challenge.",
        style={"textAlign": "center"},
    )
)


# Parse functions from questions file and use it to create a dictionary of cardbodies with the code in markdown
funcs = get_function_text_from_file(QUESTIONS_PATH)
other_contents = {}
for key, value in funcs.items():
    # we have to add an indent to every line so the first part of the function is detected as being in code
    lines = value.split("\n")
    indented_lines = ["\t" + x for x in lines]
    value = "##### Function Definition: \n" + "\n".join(indented_lines)
    other_contents[key] = html.Div(
        dbc.CardBody(dcc.Markdown(value, className="markdown"))
    )


# Layout definition

app.layout = html.Div(
    [
        dcc.Store(data={}, id="test-result-store"),
        dcc.Location(id="url"),
        dbc.Container(
            dbc.Row(
                [
                    dbc.Col(sidebar, width=1),
                    dbc.Col(
                        [
                            dbc.Card(
                                content_area,
                                style={"height": "60vh"},
                                className="card",
                            ),
                            dbc.Card(
                                dbc.Spinner(
                                    dbc.CardBody(
                                        html.H1(
                                            "Use the sidebar to pick a question",
                                            style={"textAlign": "center"},
                                        ),
                                        id="results-area",
                                        style={
                                            "height": "35vh",
                                        },
                                    )
                                ),
                                class_name="card",
                            ),
                        ],
                        width=11,
                    ),
                ],
                style={"height": "100vh"},
            ),
            style={"height": "100vh"},
        ),
    ],
)


# Callbacks
@app.callback(
    Output("results-area", "children"),
    Output("test-result-store", "data"),
    Input("test-button", "n_clicks"),
    Input("url", "pathname"),
    State("test-result-store", "data"),
    prevent_initial_call=True,
)
def run_test(
    n_clicks: int,
    pathname: str,
    data: dict,
) -> Tuple[Type[html.Div], dict]:
    """Callback to run a single test and update the internal state of test results

    Args:
        n_clicks (int): When the test-button has been clicked, the results are run
        pathname (str): part of url after domain as determined by the sidebar
        data (dict): a store that starts empty and gets results of test runs
                        when they happen for displaying on sidebar switch

    Returns:
        tuple[html.Div, dict]: The div containing the formatted result of
        the testing along with the updated data dict
    """
    trigger = ctx.triggered_id
    print(trigger)
    q = pathname[1:]
    # print(q)
    # print(n_clicks)
    # print(data)

    if trigger == "test-button" or q in data:
        if trigger == "test-button":
            test_call = ["poetry", "run", "pytest", "-k", f"test_{q}"]
            try:
                result = subprocess.check_output(
                    test_call, text=True, stderr=subprocess.STDOUT
                )
            except CalledProcessError as e:
                result = e.output
            result = f"```{result}```"
            data[q] = result
        else:
            result = data[q]
        ans = html.Div(
            [
                html.H3(f"Results for Question {pathname[-1]}"),
                dcc.Markdown(result, className="markdown"),
            ]
        )
    else:
        if "question" in pathname:
            text = "Hit the 'Run Test' button to see how the code performs"
        else:
            text = "Use the sidebar to pick a question"
        ans = html.H1(
            text,
            style={"textAlign": "center"},
        )
    return ans, data


@app.callback(Output("content-area", "children"), [Input("url", "pathname")])
def get_answers(pathname: str) -> html.Div:
    """Generates the html for the top right section displaying the function definion.
        If the sidebar is still on home, this displays just a text prompt otherwise
        it displays a formatted function definition for the answer to that question.

    Args:
        pathname (str): part of url after domain as determined by the sidebar

    Returns:
        html.Div: The formatted html.
    """
    if pathname in ["/", ""]:
        return home_content
    elif pathname in [f"/question_{i}" for i in range(1, NUM_QUESTIONS + 1)]:
        return html.Div(
            [
                dbc.CardHeader(
                    dbc.Row(
                        [
                            dbc.Col(
                                html.H3(
                                    f"Attempt for Question {pathname[-1]}",
                                ),
                                width=10,
                            ),
                            dbc.Col(
                                dbc.Button("Run Test", id="test-button"),
                                width=2,
                            ),
                        ],
                        justify="between",
                    )
                ),
                other_contents[pathname[1:]],
            ]
        )
    else:
        return html.Div("404: Not found")


if __name__ == "__main__":
    app.run_server(debug=DEBUG, host=HOST, port=PORT)
