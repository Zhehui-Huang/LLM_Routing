import math

# City coordinates
cities = {
    0: (8, 11), 1: (40, 6), 2: (95, 33), 3: (80, 60), 
    4: (25, 18), 5: (67, 23), 6: (97, 32), 7: (25, 71), 
    8: (61, 16), 9: (27, 91), 10: (91, 46), 11: (40, 87), 
    12: (20, 97), 13: (61, 25), 14: (5, 59), 15: (62, 88), 
    16: (13, 43), 17: (61, 28), 18: (60, 63), 19: (93, 15)
}

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def solve_tsp():
    not_visited = list(cities.keys())[1:]  # Exclude the depot from initial visit
    tour = [0]  # Start at the depot
    current_city = 0
    max_distance = 0
    total_cost = 0

    while not_visited:
        # Choosing the next city to visit based on the closest one
        next_city = min(not_visited, key=lambda x: euclidean_distance(cities[current_city], cities[x]))
        distance = euclidean_distance(cities[current_city], cities[next_city])
        total_cost += distance
        max_distance = max(max_distance, distance)
        tour.append(next_city)
        current_city = next_city
        not_visited.remove(next_city)

    # Adding the return trip to the depot
    returning_distance = euclidean_distance(cities[current_city], cities[0])
    total_cost += returning_distance
    max_distance = max(max_distance, returning_distance)
    tour.append(0)

    return tour, total_cost, max_distance

# Get the solution using the defined function
tour, total_team, request_max_distance = solve_tsp()  # Correcting previous typo in variable names

# Displaying result as requested
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")