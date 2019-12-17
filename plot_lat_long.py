import pandas as pd
import folium

summary = pd.read_excel('PermianTops.xlsx', sheet_name='Data')

#create a map and add multiple layers
this_map = folium.Map(prefer_canvas=True, tiles ='mapbox', 
                      API_key='pk.eyJ1IjoiYmliaW5tam9zZSIsImEiOiJjamdmMHJ2YW8yaWxtMnFvNW9iYmZka3U3In0.rjuLKvzjYDeIcsxj4Q5UBQ')
this_map = folium.Map(prefer_canvas=True)
folium.TileLayer('Stamen Terrain').add_to(this_map)

# adding layer control to map
this_map.add_child(folium.LayerControl())

# function to map points on to map
def plotDot(point):
    '''input: series that contains a numeric named latitude and a numeric named longitude
    this function creates a CircleMarker and adds it to your this_map'''
    folium.CircleMarker(location=[point.WGS84Latitude, point.WGS84Longitude],
                        radius = 2,
                        color=color_dict[point.Name],
                        popup='UWI:{0}\n Formation:{1}'.format(
                            str(point.UWI),
                            str(point.FormationName)))\
    .add_to(this_map)

##########Plotting Everythign together #############
#color dictionary for maping to name
color_dict={'Delaware':'blue','Midland':'red'}
summary.apply(plotDot, axis = 1)

#Set the zoom to the maximum possible
this_map.fit_bounds(this_map.get_bounds())

#Save the map to an HTML file
this_map.save('Formation_Distribution_Plot.html')

