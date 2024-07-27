import math

# Coordinates for each city
city_coordinates = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), 
    (6, 58), (12, 84), (72, 77), (98, 95), (11, 0),
    (61, 25), (52, 0), (60, 95), (10, 94), (96, 73), 
    (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

# Function to calculate Euclidean distance between two cities, given their indices
def euclidean_distance(index1, index2):
    x1, y1 = city_coordinates[index1]
    x2, y2 = city_coordinates[index2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Function to calculate the total cost of a given tour
def calculate_total_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(tour[i], tour[i + 1])
    return total_cost

# Nearest Neighbor Heuristic to find an initial tour starting from the depot
def nearest_neighbor_tour(start_city):
    unvisited = set(range(1, len(city_coordinates)))  # exclude the depot city initially
    tour = [start_city]
    current_city = start_report

    while unvisited:
        next_city = min(unvisited, key=lambda city: euclidean_distance(current_city, city))
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city
    
    tour.append(start_city)  # return to the depot city to complete the tour
    return tour

# Find the initial tour using the nearest neighbor heuristic
initial_tour = nearest_neighbor_tour(0)
initial_cost = calculate_total_cost(initial_tour)

# Implement the 2-opt algorithm to optimize the tour
def two_opt(tour):
    best_cost = calculate_total_cost(tour)
    best_tour = tour[:]
    improved = True

    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                new_tour = tour[:i] + tour[i:j+1][::-1] + tour[j+1:]
                new_cost = calculate_total_cost(new_tour)
                if new_cost < best_cost:
                    best_tour, best_cost = new_tour, new_cost
                    improved = True

    return best_tour, best_cost

# Optimize the initial tour with the 2-opt algorithm
final_tour, final_cost = two_opt(initial_tour)

# Output the improved tour and the corresponding total travel cost
print("Tour:", final_tour)
print("Total travel cost:", final_cost)