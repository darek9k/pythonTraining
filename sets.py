# collections do not store duplicates

cities = {"Detroit", "Washington", "Dallas", "Chicago"}
cities2 = {"Detroit"}

cities.add("Houston")
print(cities)
cities.add("Dallas")
print(cities)

print(cities - cities2)
print(cities | cities2)
print(cities & cities2)
print(cities ^ cities2)
