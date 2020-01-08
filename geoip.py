import geoip2.database

reader = geoip2.database.Reader('GeoLite2-City.mmdb')
response = reader.city('220.73.134.140')

print(response.country.iso_code)
print(response.country.name)

print("End")
