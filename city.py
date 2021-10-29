# Creates a list of city JSON files starting from aa.json to just before zz.json
# The resulting files will be used for the WeatherApp
import json

# prefixes
p1 = 'a'
p2 = 'a'

# list of <Name, State/Country>'s generated from city.list.json
unsorted_l = []
sorted_l = []

# read city.list.json file and produce a list of <Name, State/Country)>'s
with open('city.list.json', encoding='utf-8') as f:
    data = json.load(f)
    for c in data:
        city = c["name"] + ', ' + c["state"]
        if c["state"] == '':
            city = city + c["country"]

        if len(city) == len(city.encode()):
            # I know this discludes a lot of cities, but it makes everything simpler
            if (ord(city[0]) >= ord('a') and ord(city[0]) <= ord('z')) or (ord(city[0]) >= ord('A') and ord(city[0]) <= ord('Z')):
                if (ord(city[1]) >= ord('a') and ord(city[1]) <= ord('z')) or (ord(city[1]) >= ord('A') and ord(city[1]) <= ord('Z')):
                    unsorted_l.append(city)
f.close()

# sort list of <Name, State/Country)>'s (case-insensitive)
sorted_l = sorted(unsorted_l, key=str.casefold)

# now write files aa.json, ab.json, ac.json, ..., zz.json
l = []
for city in sorted_l:
    if p1 == 'z' and p2 == 'z':
        # fortunately we don't have city starting with zz, so we can end here
        break
    else:
        if (city[0].lower()+city[1].lower()) == (p1+p2):
            # if first two letters of city name match {p1+p2} append to list
            l.append(city)
        else:
            # write list to file named {p1+p2}.json
            if l != []:
                with open('cities/' + p1+p2 + '.json', 'w') as f:
                    json.dump(l, f)

            # clear list
            l = []

            # then go to the next 2-prefix (examples: ab -> ac; az -> ba)
            if p2 == 'z':
                p1 = chr(ord(p1)+1)
                p2 = 'a'
            else:
                p2 = chr(ord(p2)+1)