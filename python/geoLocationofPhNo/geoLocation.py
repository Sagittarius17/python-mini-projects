import phonenumbers
import opencage
import folium
from opencage.geocoder import OpenCageGeocode
from phonenumbers import geocoder
from phonenumbers import carrier

number = input('Write here --> ') #write phn number
pepnum = phonenumbers.parse(number) 
location = geocoder.description_for_number(pepnum, "en") # location identifier
print(location) # print country name

service_pro = phonenumbers.parse(number)
name  = carrier.name_for_number(service_pro, "en") 
print(name) # print service provider name

key = "(Provide your API key here.)" # api key

geocoder = OpenCageGeocode(key)
query = str(location)
results = geocoder.geocode(query)
#print(results)
'''gmaps = googlemaps.Client(key)
query = str(location)
results = gmaps.geocode(query)
print(results)'''

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print(lat, lng)

myMap = folium.Map(location=[lat, lng], zoom_start = 0)
folium.Marker([lat, lng], popup= location).add_to(myMap)

myMap.save("mylocation.html")
