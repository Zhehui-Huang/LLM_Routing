import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, computed_cost, cities):
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"  # Check start and end at depot city

    if len(tour) != 8 or len(set(tour)) != 8:
        return "FAIL"  # Check if tour comprises exactly 7 different cities including the depot

    # Calculate the total travel cost from the tour
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += calculate_distance(cities[tour[i]], cities[tour[i + 1]])

    # Round to match precision of provided cost
    total_distance = round(total_distance, 2)

    # Check if calculated distance is equal to the provided total cost
    if total_distance != computed_cost:
        return "FAIL"

    return "CORRECT"

# Definitions of the cities (index corresponds to city number)
cities = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

# Solution to test
tour = [0, 4, 2, 1, 7, 3, 8, 0]
computed_cost = 159.97

# Run the verification test
result = verify_solution(tour, computed_cost, cities)
print(result)