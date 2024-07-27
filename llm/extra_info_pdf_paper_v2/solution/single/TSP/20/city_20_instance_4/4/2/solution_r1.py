import math

# Coordinates of each city
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10), 5: (69, 22),
    6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29), 10: (29, 26), 11: (85, 68),
    12: (60, 1), 13: (71, 73), 14: (82, 47), 15: (19, 25), 16: (75, 9), 17: (52, 54),
    18: (64, 72), 19: (14, 89)
}

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Initial nearest neighbor solution
def nearest_neighbor_tour(start_city):
    unvisited = set(cities.keys())
    unvisited.remove(start_city)
    tour = [start_city]
    current_city = start_city

    while unvisited:
        next_city = min(unvisited, key=lambda city: distance(current_city, city))
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city

    tour.append(start_city)  # return to the starting city (depot)
    return tour

# 2-opt optimization
def two_opt(tour):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                if distance(tour[i], tour[j]) + distance(tour[i + 1], tour[j + 1]) < \
                   distance(tour[i], tour[i + 1]) + distance(tour[j], tour[j + 1]):
                    tour[i + 1:j + 1] = reversed(tour[i + 1:j + 1])
                    improved = True
    return tour

# Initial tour by Nearest Neighbor
initial_tour = nearest_neighbor_tour(0)

# Optimized tour by 2-opt
optimized_tour = two_opt(initial_tour.copy())

# Calculate the total cost of the optimized tour
def total_travel_cost(tour):
    return sum(distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

cost = total_travel_cost(optimized_tour)

# Results
print("Tour:", optimized_tour)
print("Total travel cost:", round(cost, 2))