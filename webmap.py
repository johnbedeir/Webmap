#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 20:57:55 2020

@author: triple-a
"""


import folium
import jinja2
import pandas

def color_gen(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'

data = pandas.read_csv("locations.csv")
lon= list(data["LON"])
lat= list(data["LAT"])
elev= list(data["ELEV"])

map = folium.Map(location=[0,0], zoom_start=3)

fgv = folium.FeatureGroup(name="Locations")

for lt, ln, el in zip(lat, lon, elev):
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius=6, popup=str(el)+"m", fill_color=color_gen(el), color='transparent', fill_opacity=0.7))
    

map.add_child(fgv)
map.add_child(folium.LayerControl())

map.save("Map.html")