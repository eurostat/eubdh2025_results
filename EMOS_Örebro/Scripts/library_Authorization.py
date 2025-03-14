## Import required libraries
#import requests
import io
import numpy as np
#import plotly.express as px
#import plotly.graph_objects as go
from PIL import Image

import geopandas as gpd
import folium
import fiona

from IPython.display import display

import matplotlib.pyplot as plt

import pandas as pd
import plotly.express as px

# #| title: Satellite Image Retrieval
# # Function to get access token
# def get_access_token():
#     """Retrieve access token from Copernicus Data Space Ecosystem."""
#     token_url = "https://identity.dataspace.copernicus.eu/auth/realms/CDSE/protocol/openid-connect/token"
#     client_id = 'sh-c4e8b7e5-a590-4479-baf4-435a23e4ddfd'
#     client_secret = '7gRYSdD5UubsQtoFnf89W8WjfYNJvCOX'
#     
#     response = requests.post(
#         token_url,
#         data={"grant_type": "client_credentials"},
#         auth=(client_id, client_secret),
#     )
#     
#     token_data = response.json()
#     if "access_token" in token_data:
#         return token_data["access_token"]
#     else:
#         print("❌ Authentication failed!")
#         print(token_data)
#         return None
