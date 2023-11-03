# First task from the lecture

resources = {}

while True:
    current_resources = input()
    if current_resources == "stop":
        break
    current_quantity = int(input())
    if current_resources not in resources.keys():
        resources[current_resources] = 0
    resources[current_resources] += current_quantity
        



# Second task from me me

