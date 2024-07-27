import math

def calculate_euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def verify_tour(cities, tour, total_cost_claimed, max_distance_claimed):
    # Verify start and end at the depot, and all cities visited once
    if tour[0] != 0 or tour[-1] != 0 or sorted(tour) != sorted(list(range(len(cities)))):
        return "FAIL"

    # Calculate total travel cost and max distance
    total_cost_calculated = 0
    max_distance_calculated = 0

    for i in range(len(tour) - 1):
        city_1 = cities[tour[i]]
        city_2 = cities[tour[i+1]]
        distance = calculate_euclidean_distance(city_1, city_2)
        total_cost_calculated += distance
        if distance > max_distance_calculated:
            max_distance_calculated = distance

    # Check if the calculated values match the claimed values
    if (abs(total_cost_claimed - total_cost_calculated) > 1e-5 or
            abs(max_distance_claimed - max_distance_calculated) > 1e-5):
        return "FAIL"

    return "CORRECT"

# Given cities and received solution
cities = [
    (79, 15),  # Depot city 0
    (79, 55),
    (4, 80),
    (65, 26),
    (92, 9),
    (83, 61),
    (22, 21),
    (97, 70),
    (20, 99),
    (66, 62)
]

# Provided solution
tour = [0, 1, 5, 4, 9, 7, 3, 2, 8, 6, 0]
total_travel_cost = 487.08741963050335
maximum_distance = 81.46778504415104

# Verify the solution
result = verify_tour(cities, tour, total_travel_cost, maximum_distance)
print(result)