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
# German_city = []
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

# Print the average temperature for all the cities in Germany

'''
Your code here

'''

# Print the max temperature for all the cities in Italy

'''
Your code here

'''
