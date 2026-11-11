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

def filter_items(condition, dict_list):
    result = []
    for item in dict_list:
        if condition(item):
            result.append(item)
    return result


def aggregate(aggregation_key, aggregation_function, dict_list):
    values = []
    for item in dict_list:
        values.append(item[aggregation_key])
    return aggregation_function(values)


# Print the average temperature of all the cities
print(aggregate(
    "temperature",
    lambda values: sum(float(value) for value in values) / len(values),
    cities,
))

# Print all cities in Germany
german_cities = filter_items(lambda city: city["country"] == "Germany", cities)
for city in german_cities:
    print(city)

# Print all cities in Spain with a temperature above 12°C
spanish_cities = filter_items(
    lambda city: city["country"] == "Spain" and float(city["temperature"]) > 12,
    cities,
)
for city in spanish_cities:
    print(city)

# Count the number of unique countries
print(aggregate("country", lambda countries: len(set(countries)), cities))

# Print the average temperature for all the cities in Germany
print(aggregate(
    "temperature",
    lambda values: sum(float(value) for value in values) / len(values),
    german_cities,
))

# Print the max temperature for all the cities in Italy
italian_cities = filter_items(lambda city: city["country"] == "Italy", cities)
print(aggregate(
    "temperature",
    lambda values: max(float(value) for value in values),
    italian_cities,
))