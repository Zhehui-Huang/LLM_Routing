import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(route, cities):
    visited = set()
    n = len(cities)
    total_cost = 0
    max_distance = 0

    # Visit each city exactly once check
    for city_idx in route:
        if city_idx in visited:
            print("FAIL: City", city_idx, "is visited more than once.")
            return "FAIL"
        visited.add(city_idx)
    
    if len(visited) != n or route[0] != 0 or route[-1] != 0:
        print("FAIL: Not all cities visited exactly once or the route does not start/end at the depot.")
        return "FAIL"

    # Subtour elimination check
    if len(set(route)) < len(route) - 1:
        print("FAIL: There are subtours present.")
        return "FAIL"

    # Validate maximum and total travel cost
    for i in range(1, len(route)):
        distance = calculate_distance(cities[route[i-1]], cities[route[i]])
        total_cost += distance
        max_distance = max(max_distance, distance)
    
    if not math.isclose(total_cost, 341, abs_tol=0.1):
        print(f"FAIL: Expected total travel cost of approximately 341, but got {total_cost}")
        return "FAIL"
    
    if not math.isclose(max_distance, 32, abs_tol=0.1):
        print(f"FAIL: Expected maximum distance between consecutive cities of 32, but got {max_distance}")
        return "FAIL"
    
    return "CORRECT"

# City coordinates provided in the problem
cities_coordinates = [
    (8, 11), (40, 6), (95, 33), (80, 60), (25, 18), (67, 23), (97, 32), (25, 71), (61, 16),
    (27, 91), (91, 46), (40, 87), (20, 97), (61, 25), (5, 59), (62, 88), (13, 43), (61, 28),
    (60, 63), (93, 15)
]

# Route given in the solution
given_route = [0, 4, 1, 8, 16, 5, 18, 6, 2, 10, 3, 17, 14, 11, 9, 12, 7, 13, 15, 0]

# Check the route
output = verify_solution(given_route, cities_coordinates)
print(output)