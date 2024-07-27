import math
import random

# Define the coordinates of the cities
cities = {
    0: (14, 77),
    1: (34, 20),
    2: (19, 38),
    3: (14, 91),
    4: (68, 98),
    5: (45, 84),
    6: (4, 56),
    7: (54, 82),
    8: (37, 28),
    9: (27, 45),
    10: (90, 85),
    11: (98, 76),
    12: (6, 19),
    13: (26, 29),
    14: (21, 79),
    15: (49, 23),
    16: (78, 76),
    17: (68, 45),
    18: (50, 28),
    19: (69, 9)
}

num_cities = len(cities)

# Function to calculate Euclidean distance
def calculate_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Generate an initial random tour from the depot city (excluding the depot city itself)
def create_initial_tour():
    tour = list(range(1, num_cities))  # Starting at 1 because 0 is the depot city
    random.shuffle(tour)
    return [0] + tour + [0]  # Include the depot city as start and end

# Calculate the total cost of a given tour
def calculate_total_distance(tour):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += calculate_distance(tour[i], tour[i+1])
    return total_distance

# Try to swap two cities and check if it improves the tour
def two_opt(tour):
    best_distance = calculate_total_distance(tour)
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                if i != 1 or j != len(tour) - 2:
                    new_tour = tour[:]
                    new_tour[i:j+1] = reversed(tour[i:j+1])
                    new_distance = calculate_total_distance(new_tour)
                    if new_distance < best_distance:
                        tour = new_tour
                        best_distance = new_distance
                        improved = True
    return tour, best_distance

# Main function to find the shortest path
def find_shortest_tour():
    best_tour = create_initial_tour()
    best_tour, best_distance = two_opt(best_tour)
    return best_tour, best_distance

# Running the heuristic
tour, total_distance = find_shortest_tour()

# Output results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_distance:.2f}")