import math

# Define the cities' coordinates
cities = {
    0: (29, 51),
    1: (49, 20),
    2: (79, 69),
    3: (17, 20),
    4: (18, 61),
    5: (40, 57),
    6: (57, 30),
    7: (36, 12),
    8: (93, 43),
    9: (17, 36),
    10: (4, 60),
    11: (78, 82),
    12: (83, 96),
    13: (60, 50),
    14: (98, 1)
}

def calculate_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

def solve_tsp(cities):
    n = len(cities)
    visited = [False] * n
    tour = [0]
    visited[0] = True

    current_index = 0

    while len(tour) < n:
        nearest = None
        min_distance = float('inf')

        for i in range(n):
            if not visited[i]:
                distance = calculate_distance(current_index, i)
                if distance < min_distance:
                    min_distance = distance
                    nearest = i

        visited[nearest] = True
        tour.append(nearest)
        current_index = nearest

    tour.append(0)  # return to the depot
    return tour

def calculate_tour_details(tour):
    total_cost = 0
    max_distance = 0

    for i in range(1, len(tour)):
        distance = calculate_distance(tour[i-1], tour[i])
        total_cost += distance
        if distance > max_distance:
            max_distance = distance

    return total_cost, max_distance

# Solve the TSP
tour = solve_tsp(cities) 

# Evaluate the obtained tour
total_cost, max_distance = calculate_tour_details(tour)

# Print the Tour, Total Cost, and Maximum Distance
print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)