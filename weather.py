import re
import urllib.request

#https://www.weather-forecast.com/locations/Paris/forecasts/latest

city = input("Enter the city: ")
city = city.replace(' ', '-')
url = "https://www.weather-forecast.com/locations/" + city + "/forecasts/latest"

data = urllib.request.urlopen(url).read()
data1 = data.decode("utf8")
m = re.search('span class="phrase">', data1)
start = m.end()
end = start + 600
newString = data1[start:end]
m = re.search("</span>", newString)
end = m.start()
final = newString[0:end]
final = final.replace('&deg;C', ' degrees Celcius')
print(final)


