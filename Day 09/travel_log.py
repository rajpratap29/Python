country = input("Enter the name of country you want to add: ")
visits = int(input("Enter the number of visits: "))
list_of_cities = eval(input('Enter a list of cities ex:- ["city1", "city2"]: '))

travel_log =  [
    {
        "country": "France", 
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"],
    },
    {
        "country": "Germany", 
        "visits": 15,
        "cities": ["Berlin", "Hamburg", "Stuttgart"],
    },
]

def add_new_country(name, times_visited, cities_visited):
    new_country = {}
    new_country["country"] = name
    new_country["visits"] = times_visited
    new_country["cities"] = cities_visited
    travel_log.append(new_country)

add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")