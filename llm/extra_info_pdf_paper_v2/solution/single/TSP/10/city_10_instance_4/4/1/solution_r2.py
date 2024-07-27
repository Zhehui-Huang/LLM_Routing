import math

# Coordinates of the cities indexed from 0 to 9
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

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Greedy algorithm to get an initial feasible solution (nearest neighbour)
def nearest_neighbour(start_city):
    tour = [start_city]
    unvisited = set(cities.keys()) - {start_city}

    current_city = start_city
    while unvisited:
        next_city = min(unvisited, key=lambda city: distance(current_city, city))
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city

    tour.append(start_city)  # return to the depot city
    return tour

# Implement the 2-opt routine for optimizing the tour
def two_opt(tour):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 1):
            for j in range(i + 1, len(tour) - 1):
                if distance(tour[i - 1], tour[j]) + distance(tour[i], tour[j + 1]) < \
                   distance(tour[i - 1], tour[i]) + distance(tour[j], tour[j + 1]):
                    tour[i:j + 1] = reversed(tour[i:j + 1])
                    improved = True
    return tour

# Calculate the total tour cost
def calculate_tour_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += distance(tour[i], tour[i + 1])
    return total_cost

# Main execution to find an optimal route and its cost
initial_tour = nearest_neighbour(0)
optimized_tour = two_opt(initial_tour)
total_cost = calculate_tour_cost(optimized_tour)

# Display results
print("Tour:", optimized_tour)
print("Total travel cost:", total_cost)