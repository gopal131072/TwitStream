from geopy.geocoders import Nominatim
from time import sleep

geolocator = Nominatim()

# This is the list where we'll store all the locations we get from locations.txt
addresses = []

# This is the file where we'll dump all the coordinates.
file = open("../output/coordinates.txt","w",encoding="utf-8")

# Split by newline to seperate all locations and store them in the list.
with open('../output/location.txt') as f:
    addresses = f.read()
    addresses = addresses.split("\n")

for address in addresses:
    if(address is not "No location supplied"):
        # The sleep is to prevent the app from sending too many requests and timing out.
        # Even if it times out it should retry within a couple of seconds.
        try:
            # Geopy call to obtain the coordinates when supplied with an address.
            current = geolocator.geocode(address,timeout=10)
            sleep(1)
        except Exception as exception:
            # You can force a recall of geocode here if you suspect that timeouts are still happening.
            print(exception)
            sleep(2)
        if current is not None:
            # Write longitude,latitude into the file. This is the format that Basemap requires them in.
            file.write(str(current.longitude))
            file.write(",")
            file.write(str(current.latitude))
            file.write("\n")
            print(current.longitude, end='')
            print(", ",end = '')
            print(current.latitude)
#Close file when done writing.
file.close()
