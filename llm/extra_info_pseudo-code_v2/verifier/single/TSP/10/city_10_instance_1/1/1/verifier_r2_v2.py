import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def validate_tour(cities, tour):
    visited = set(tour)
    return len(tour) == len(cities) + 1 and len(visited) == len(cities) and tour[0] == tour[-1] == 0

def calculate_total_tour_cost(cities, tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        city_coords1 = cities[tour[i]]
        city_coords2 = cities[tour[i+1]]
        total_cost += euclidean_distance(city_coords1, city_state)
    return total_cost

# Environment setup
cities = {
    0: (53, 68), 1: (75, 11), 2: (91, 95), 3: (22, 80), 4: (18, 63),
    5: (54, 91), 6: (70, 14), 7: (97, 44), 8: (17, 69), 9: (95, 89)
}

# Provided solution
initial_tour = [0, 5, 3, 8, 4, 6, 1, 7, 9, 2, 0]
initial_tour_cost = 290.8376577906224
optimized_tour = [0, 5, 2, 9, 7, 1, 6, 4, 8, 3, 0]
optimized_tour_cost = 280.8414894850646

# Test each requirement
if not validate_tour(cities, initial_tour):
    print("FAIL: Initial tour is not valid.")
elif not validate_tour(cities, optimized_tour):
    print("FAIL: Optimized tour is not valid.")
elif abs(calculate_total_tour_cost(cities, initial_tour) - initial_tour_cost) > 1e-5:
    print("FAIL: Incorrect initial tour cost calculation.")
elif abs(calculate_total_tour_cost(cities, optimized_tour) - optimized_tour_cost) > 1e-5:
    print("FAIL: Incorrect optimized tour cost calculation.")
elif optimized_tour_cost >= initial_tour_cost:
    print("FAIL: Optimized tour should have a lower cost than initial.")
else:
rint("CORRECT")