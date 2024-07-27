from itertools import combinations, permutations
import math

# City coordinates
cities = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

def euclidean_distance(p1, p2):
    """ Calculate Euclidean distance between two points """
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def get_route_distance(route):
    """ Calculate total distance of the given route """
    return sum(euclidean_distance(cities[route[i]], cities[route[i + 1]]) for i in range(len(route) - 1))

def find_optimal_tour():
    min_distance = float('inf')
    best_route = []
    
    # Generate all combinations of 5 cities excluding the depot city
    for city_combo in combinations(range(1, 10), 5):
        # Include the depot city in the route
        full_route = (0,) + city_combo + (0,)
        
        # Generate all permutations of the selected cities
        for perm in permutations(city_combo):
            current_route = (0,) + perm + (0,)
            current_distance = get_route_distance(current_route)
            
            # Update the minimum distance and best route if a shorter route is found
            if current_distance < min_distance:
                min_distance = current_distance
                best_route = current_route

    return best_route, min_distance

# Execute the function and print the optimal route and cost
optimal_route, optimal_cost = find_optimal_tour()
print(f"Tour: {list(optimal_route)}")
print(f"Total travel cost: {optimal_cost:.2f}")