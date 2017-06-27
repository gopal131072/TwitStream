from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

m = Basemap(projection ='mill', llcrnrlat = -90, urcrnrlat = 90,\
            llcrnrlon = -180, urcrnrlon = 180, resolution='l')

coordinates = []

m.drawcoastlines()
m.drawcountries()
m.fillcontinents()
m.drawmapboundary(fill_color='#FFFFFF')

with open('coordinates.txt') as f:
    coordinates = f.read()
    coordinates = coordinates.split("\n")

coordinates = coordinates[:-1]
coord = [(i.split(',')) for i in coordinates]

for co in coord:
     x = round(float(co[0]),2)
     y = round(float(co[1]),2)
     xmap, ymap = m(x,y)
     m.plot(xmap,ymap,'ro',markersize='2')

plt.title('Twitter visualizer')
plt.show()
