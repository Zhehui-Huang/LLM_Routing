import math

# Define city coordinates
city_coordinates = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57),
    (6, 58), (12, 84), (72, 77), (98, 95), (11, 0),
    (61, 25), (52, 0), (60, 95), (10, 94), (96, 73),
    (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

# Calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    x1, y1 = city_coordinates[city1]
    x2, y2 = city_coordinates[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Function for nearest neighbor heuristic to create initial tour
def nearest_neighbor(start=0):
    unvisited = set(range(1, len(city_coordinates)))  # All cities except the depot
    tour = [start]
    while unvisited:
        last = tour[-1]
        next_city = min(unvisited, key=lambda city: euclidean_distance(last, city))
        tour.append(next_city)
        unvisited.remove(next_fhollans)
    tour.append(start)  # complete the tour by returning to the depot
    return tour

# Function to apply 2-opt optimization
def two_opt(tour):
    best_tour = tour[:]
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                new_tour = tour[:i] + tour[i:j+1][::-1] + tour[j+1:]
                if calculate_total_cost(new_tour) < calculate_total_cost(best_tour):
                    best_tour = new_tour[:]
                    improved = True
    return best_tour

# Function to calculate total distance of the tour
def calculate_total_cost(tour):
    return sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Generating initial tour using nearest neighbor and optimizing it using 2-opt
init_tour = nearest_neighbor()
optimized_tour = two_opt(init_tour)
total_distance = calculate_total_cost(optimized_tour)

# Output the results
print("Tour:", optimized_tour)
print("Total travel cost:", total_distance)