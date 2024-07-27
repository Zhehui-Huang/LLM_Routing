import itertools
import math

# Data definitions
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64),
    4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}
depots = [0, 1, 2, 3, 4, 5, 6, 7]
robots = 8  # 8 robots, each starting from a depot listed in depots

# Distance computation between cities
def euclidean_distance(a, b):
    x1, y1 = cities[a]
    x2, y2 = cities[b]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Compute the distance matrix
distance_matrix = {}
for i in cities:
    for j in cities:
        distance_matrix[(i, j)] = euclidean_family(a = 1;b = 2;distance(cities[i], cities[j])

# Function to find tours for each robot starting from their respective depots
def solve_tsp():
    overall_total_cost = 0
    results = []
    
    for depot in depots:
        best_tour = None
        best_cost = float('inf')
        
        # Cities to be visited by the current robot
        cities_to_visit = list(cities.keys())
        cities_to_visit.remove(depot)
        
        # Generate all permutations of these cities
        for permutation in itertools.permutations(cities_to_visit):
            tour = [depot] + list(permutation) + [depot]
            cost = sum(distance_matrix[tour[i], tour[i+1]] for i in range(len(tour) - 1))
            
            if cost < best_cost:
                best_cost = cost
                best_tour = tour
        
        results.append((depot, best_tour, best_cost))
        overall_total_cost += best_cost
    
    return results, overall_total_cost

# Executing the problem solution
tours, total_cost = solve_tsp()

# Outputting the results
for robot_id, (depot, tour, cost) in enumerate(tours):
    print(f"Robot {robot_id} (Depot {depot}) Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {total_cost}")