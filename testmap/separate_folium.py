import os
import pandas as pd
import folium
from folium import IFrame
import random

def create_map(mymap, lat, lon, zoom_start):
    min_lat=-70
    max_lat=110
    min_lon=-(360-222)
    max_lon=222

    mymap = folium.Map(location=[lat,lon],
                                    zoom_start=zoom_start,
                                    tiles='cartodbdark_matter',
                                    max_bounds=True,
                                    min_lat=min_lat,
                                    max_lat=max_lat,
                                    min_lon=min_lon,
                                    max_lon=max_lon,
                                    max_zoom=4,
                                    min_zoom=2)
    mymap.add_child(folium.LatLngPopup())
    return mymap


def custom_img_marker(mymap, news_lat, news_lon, news_msg, news_img_link):
    news_where = [news_lat, news_lon]
    news_msg = news_msg
    news_img_link = news_img_link
    news_img = folium.features.CustomIcon(news_img_link, icon_size=(100,100))



    folium.Marker(news_where,
                  tooltip=news_msg,
                  icon=news_img).add_to(mymap)


def img_overlay(mymap, gyre_img_link, bounds_list1, bounds_list2 ,popup_msg, zindex):

    gyre_img_link =gyre_img_link
    gyre_img = folium.raster_layers.ImageOverlay(
        name='plastic island',
        image=gyre_img_link,
        bounds=[bounds_list1, bounds_list2],
        opacity=0.4,
        interactive=True,
        cross_origin=False,
        zindex=zindex,
    )
    folium.Popup(popup_msg).add_to(gyre_img)

    gyre_img.add_to(mymap)
    folium.LayerControl().add_to(mymap)


def iframe_img(mymap, resolution, width, height, img_src, lat, lan):
    html = '<img src=' + img_src + '>'
    iframe = IFrame(html, width=(width*resolution)+20, height=(height*resolution)+20)
    popup = folium.Popup(iframe, max_width=2650)

    icon = folium.Icon(color="red", icon="ok")
    marker = folium.Marker(location=[lat, lan], popup=popup, icon=icon)
    marker.add_to(mymap)

def iframe_img_para(mymap, resolution, width, height, img_src, lat, lan, paragraph):
    html = '<img src=' + img_src + ' style="width:70%"">'
    html += '<pre>' + paragraph + '</pre>'
    iframe = IFrame(html, width=(width*resolution)+20, height=(height*resolution)+20)
    popup = folium.Popup(iframe, max_width=2650)

    icon = folium.Icon(color="red", icon="ok")
    marker = folium.Marker(location=[lat, lan], popup=popup, icon=icon)
    marker.add_to(mymap)


def add_news(mymap,news_lat, news_lon, news_msg, news_img_link, news_link):
    resolution, width, height = 75, 7, 3
    news_where = [news_lat, news_lon]
    news_msg = news_msg
    icon = folium.Icon(color="red", icon="ok")

    news_img = '<img src=' + news_img_link + '>'
    news_atag ='<a href=' + news_link + ' target="_blank">' + news_img + '</a>'
    #print(news_atag)
    news_iframe = IFrame(news_atag, width=(width*resolution)+20, height=(height*resolution)+20)
    news_popup = folium.Popup(news_iframe, max_width=2650, parse_html=True)

    folium.Marker(news_where,
                  tooltip=news_msg,
                  icon=icon,
                  popup=news_popup).add_to(mymap)
