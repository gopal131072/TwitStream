from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

# Draw a base map with the miller cylindrical projection.
m = Basemap(projection ='mill', llcrnrlat = -90, urcrnrlat = 90,\
            llcrnrlon = -180, urcrnrlon = 180, resolution='l')

# The list in which we'll store all the coordinates from coordinates.txt
coordinates = []

# The calls are self evident but can be looked up in the basemap documentation if needed.
m.drawcoastlines()
m.drawcountries()
m.fillcontinents()
m.drawmapboundary(fill_color='#FFFFFF')

# Split my \n to seperate all coordinates.
with open('../output/coordinates.txt') as f:
    coordinates = f.read()
    coordinates = coordinates.split("\n")

# Remove the last element in the list because there's an extra \n.
coordinates = coordinates[:-1]
# Split each element of the list by , to seperate latitude and longitude.
coord = [(i.split(',')) for i in coordinates]

# X is the longitude which is the first element.
# Y is the latitude which is the second element.
for co in coord:
     x = round(float(co[0]),2)
     y = round(float(co[1]),2)

     # Convert these into mapped coordinates.
     xmap, ymap = m(x,y)
     # Plot said coordinate with a red dot of size 2.
     # Feel free to play around with the size and color. You can also add alpha values for transparency.
     m.plot(xmap,ymap,'ro',markersize='2')

# The title of the plot.
plt.title('Twitter visualizer')

# Draw the plot you've created.
plt.show()
