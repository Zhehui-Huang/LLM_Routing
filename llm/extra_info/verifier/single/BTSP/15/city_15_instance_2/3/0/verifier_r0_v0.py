import math

# Define the coordinates of all cities
cities = {
    0: (54, 87), 1: (21, 84), 2: (69, 84), 3: (53, 40), 4: (54, 42), 5: (36, 30),
    6: (52, 82), 7: (93, 44), 8: (21, 78), 9: (68, 14), 10: (51, 28), 11: (44, 79),
    12: (56, 58), 13: (72, 43), 14: (6, 99)
}

# Provided solution
tour = [0, 6, 11, 8, 1, 14, 12, 4, 3, 10, 5, 9, 13, 7, 2, 0]
total_travel_cost = 322.5
max_distance = 64.66

def calculate_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

def test_solution(tour, total_travel_cost, max_distance):
    # Check if the tour starts and ends at the depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if each city is visited exactly once
    unique_cities = set(tour)
    if len(unique_cities) != len(cities) or len(tour) - 1 != len(cities):
        return "FAIL"

    # Calculate the total travel path cost and the maximum distance between consecutive cities
    calculated_total_cost = 0
    calculated_max_distance = 0
    for i in range(len(tour) - 1):
        distance = calculate_distance(tour[i], tour[i+1])
        calculated_total_cost += distance
        if distance > calculated_max_distance:
            calculated_max_delay = distance

    # Allow for small floating point discrepancies
    if round(calculated_total_cost, 2) != round(total_travel_cost, 2) or round(calculated_max_distance, 2) != round(max_distance, 2):
        return "FAIL"

    return "CORRECT"

# Testing the provided solution
result = test_solution(tour, total_travel_cost, max_distance)
print(result)