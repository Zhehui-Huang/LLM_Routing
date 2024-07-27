import math

# Define coordinates of the cities
cities = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

# Function to calculate Euclidean distance
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Finding an initial tour using the nearest neighbour strategy
def initial_tour(start_city):
    unvisited = set(cities.keys())
    unvisited.remove(start_city)
    tour = [start_city]
    current_city = start_city
    while unvisited:
        next_city = min(unvisited, key=lambda city: distance(current_city, city))
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city
    tour.append(start_city)  # Completing the loop by returning to the start
    return tour

# Optimization using the 2-opt swap
def two_opt(tour):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour)):
                if distance(tour[i - 1], tour[i]) + distance(tour[j], tour[j + 1 % len(tour)]) > \
                   distance(tour[i - 1], tour[j]) + distance(tour[i], tour[j + 1 % len(tour)]):
                    tour[i:j + 1] = reversed(tour[i:j + 1])
                    improved = True
    return tour

# Computing the total travel cost
def tour_cost(tour):
    return sum(distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

# Generate and optimize initial tour
initial = initial_tour(0)
optimized_tour = two_opt(initial)
total_cost = tour_cost(optimized_tour)

# Output results
print("Tour:", optimized_tour)
print("Total travel cost:", total_cost)