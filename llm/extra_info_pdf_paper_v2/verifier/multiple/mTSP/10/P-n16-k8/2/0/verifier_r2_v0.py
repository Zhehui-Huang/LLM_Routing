import math

# Define the city coordinates and robot tours
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58,27), 15: (37, 69)
}

tours = [
    [0, 10, 1, 0], [0, 8, 3, 0], [0, 4, 11, 0], [0, 12, 7, 0],
    [0, 13, 6, 0], [0, 5, 14, 0], [0, 2, 15, 0], [0, 9, 0]
]

# Calculate Euclidean distance between two cities
def calculate_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Check if all cities are covered exactly once
all_toured_cities = set()
for tour in tours:
    all_toured_cities.update(tour[1:-1])  # Remove the depot city 0 from start and end

# Calculate the total travel cost and individual travel costs
calculated_total_cost = 0
individual_costs = []
for tour in tours:
    tour_cost = 0
    for i in range(len(tour) - 1):
        cost = calculate_distance(tour[i], tour[i + 1])
        tour_cost += cost
    individual_costs.append(tour, round(tour_cost, 2))
    calculated_total_cost += tour_cost

# Check requirement fulfillment
correct_solution = (len(all_toured_cities) == 15 and all(n in all_toured_cities for n in range(1, 16)))
correct_costs = abs(calculated_total_cost - 510.86149174760715) < 1e-4

# Print result based on requirements
if correct_solution and correct_costs:
    print("CORRECT")
else:
    print("FAIL")