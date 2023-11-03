# First task from the lecture

#First way
countries = input().split()(", ")
capitals = input().split()(", ")
final_information = {countries[index]: capitals[index] for index in range(len(capitals))}
for country, capital in countries.items():
    print(f"{country} -> {capital}")
    
#Second way
countries = input().split()(", ")
capitals = input().split()(", ")
final_information = dict(zip(countries, capitals))
for country, capital in countries.items():
    print(f"{country} -> {capital}")


# Second task from me me

