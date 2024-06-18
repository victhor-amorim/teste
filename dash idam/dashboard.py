import dash 
import dash_core_components as dcc
from dash import html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

import plotly.express as px
import plotly.graph_objects as go

import numpy as np
import pandas as pd
import json

df = pd.read_excel("municipios_amazonas_regioes.xlsx")

am_municipios = json.load(open("geojson/am_municipios.json", "r"))
type(am_municipios)
am_municipios.keys()
type(am_municipios["features"])
am_municipios["features"][1].keys()
am_municipios["features"][1]["id"]


