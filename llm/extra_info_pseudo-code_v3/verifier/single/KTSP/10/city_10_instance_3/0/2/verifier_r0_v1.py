import math

# Define the coordinates of the cities
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

# Provided tour and its total travel cost
provided_tour = [0, 7, 1, 5, 6, 3, 8, 0]
provided_cost = 226.07

def calculate_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

def total_tour_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_distance(tour[i], tour[i + 1])
    return total_cost

def verify_solution(tour, calculated_cost, provided_cost):
    checks = [
        # Check if tour starts and ends at depot city 0
        tour[0] == 0 and tour[-1] == 0,
        # Check if exactly 7 cities are visited (8 items in the tour include the return to city 0)
        len(set(tour)) == 8,
        # Check if the provided tour cost is close to the calculated tour cost
        abs(provided_cost - calculated_cost) < 1e-2
    ]
    return all(checks)

# Calculate the total cost using the tour provided
calculated_cost = total_tour_cost(provided_tour)

# Validate the solution's satisfaction against the listed requirements
if verify_solution(provided_tour, calculated_cost, provided_cost):
    print("CORRECT")
else:
    print("FAIL")