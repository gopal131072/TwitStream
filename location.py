from geopy.geocoders import Nominatim
from time import sleep

geolocator = Nominatim()

address = []
file = open("coordinates.txt","w",encoding="utf-8")

with open('location.txt') as f:
    address = f.read()
    address = address.split("\n")

for addresses in address:
    if(addresses is not "No location supplied"):
        try:
            current = geolocator.geocode(addresses)
            sleep(1)
        except Exception as exception:
            print(exception)
            current = geolocator.geocode(addresses,timeout=10)
            sleep(2)
        if current is not None:
            file.write(str(current.latitude))
            file.write(" , ")
            file.write(str(current.longitude))
            file.write("\n")
            print(current.latitude, end='')
            print(" , ",end = '')
            print(current.longitude)
        else:
            file.write("Coordinates not found.\n")

file.close()
