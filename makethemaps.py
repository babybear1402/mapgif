import pandas as pd
import numpy as np
import folium
import json
from folium import plugins
import branca
import os
import requests
import time
from selenium import webdriver

url = 'https://raw.githubusercontent.com/python-visualization/folium/master/tests/us-counties.json'
county_geo = url #This is the map data


cases = pd.read_csv('cbc.csv')
cases = cases.dropna()#Removes the entires that were entered with a "Na" fips code
cases = np.array(cases)

fip = cases[:,0]
caserows = cases[:,1:]





def makemap(datarow,fips,name):
    print(max(np.log(datarow+.001)))
    counties = []
    for i in range(len(datarow)):  # Convert the data to list again
        j = str(int(fips[i]))
        k = np.log(datarow[i]+.1)
        if k<0:
            k=0
        counties.append([j, k])

    m = folium.Map(location=[39, -96], zoom_start=5)

    folium.Choropleth(geo_data=county_geo, name='choropleth', data=counties,
                      columns=['Fips', 'Cases'], key_on='feature.id', fill_color='YlOrRd',
                      fill_opacity=0.7, line_opacity=0.2, bins=[0,2,4,6,8,10,12],
                      legend_name='Cases (Log Scale)').add_to(m)

    folium.LayerControl().add_to(m)
    mname =  name + ".html"

    m.save(mname)
    delay = 1

    fn = mname
    tmpurl = 'file://{path}/{mapfile}'.format(path=os.getcwd(), mapfile=fn)
    m.save(fn)




    browser = webdriver.Chrome('/Users/JohnKolassa/PycharmProjects/virus/venv/chromedriver')
    browser.set_window_size(1024, 600)
    browser.maximize_window()
    browser.get(tmpurl)
    # Give the map tiles some time to load
    time.sleep(delay)
    pname = name + ".png"
    pname = "pictures/" + pname
    print(pname)
    browser.save_screenshot(pname)
    browser.quit()
    os.remove(mname)


for i in range(len(caserows[0,:])):
    makemap(caserows[:,i],fip,str(i))
