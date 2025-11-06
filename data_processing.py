import csv, os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
cities = []
with open(os.path.join(__location__, 'Cities.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities.append(dict(r))

# Print first 5 cities only
for city in cities[:5]:
    print(city)

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
temps = []
for city in cities:
    temps.append(float(city['temperature']))
print(sum(temps)/len(temps))
print()

# Print all cities in Germany


'''
Your code here

'''
# German_city = []c
# print("All city in Germany")
# for dict in cities:
#     if dict['country'] == 'Germany':
#         German_city.append(dict)
# print(German_city)
# print()
def fliter(condition, dict_list):
    temps = []
    for item in dict_list:
        if condition(item):
            temps.append(item)
    return temps

    
fliterd_list = fliter(lambda x: x['country'] == 'Germany', cities)
print(fliterd_list)
print()

# Print all cities in Spain with a temperature above 12°C

'''
Your code here

'''
Spain = []
for dict in cities:
    if dict['country'] == 'Spain':
        if float(dict['temperature']) > 12:
            Spain.append(dict)
print(Spain)

# Count the number of unique countries

'''
Your code here

'''
print("The number of unique countries:")
city_lists = []
for city in cities:
    if city['country'] not in city_lists:
        city_lists.append(city['country'])
print(len(city_lists))
print()

# Print the average temperature for all the cities in Germany

'''

Your code here

'''
print("The average temperature for all the cities in Germany:")
city_lists = []
for city in cities:
    if city['country'] == 'Germany':
        city_lists.append(float(city['temperature']))
print(sum(city_lists)/len(city_lists))
print()

# Print the max temperature for all the cities in Italy

'''
Your code here

'''
print("The max temperature for all the cities in Italy:")
city_lists = []
for city in cities:
    if city['country'] == 'Italy':
        city_lists.append(float(city['temperature']))
print(max(city_lists))
print()