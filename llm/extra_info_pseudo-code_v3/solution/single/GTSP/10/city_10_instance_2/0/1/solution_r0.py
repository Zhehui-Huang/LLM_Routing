import itertools
import math

# City coordinates
cities = [
    (90, 3),  # Depot
    (11, 17),
    (7, 27),
    (95, 81),
    (41, 54),
    (31, 35),
    (23, 95),
    (20, 56),
    (49, 29),
    (13, 17)
]

# Groups of cities
city_groups = [
    [3, 6],
    [5, 8],
    [4, 9],
    [1, 7],
    [2]
]

# Calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    x1, y1 = city1
    x2, y2 = city2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Generate all possible tours
def possible_tours(groups):
    return list(itertools.product(*groups))

# Calculate the full tour cost starting and ending at the depot
def calculate_tour_cost(tour):
    # Start at the depot, go through the tour, and return to the depot
    full_tour = [0] + list(tour) + [0]
    total_cost = 0
    for i in range(len(full_tour) - 1):
        city_index1 = full_tour[i]
        city_index2 = full_tour[i + 1]
        total_cost += euclidean_distance(cities[city_index1], cities[city_index2])
    return total_cost

# Find the shortest tour
def find_shortest_tour(groups):
    tours = possible_tours(groups)
    min_cost = float('inf')
    best_tour = None
    for tour in tours:
        cost = calculate_tour_cost(tour)
        if cost < min_cost:
            min_cost = cost
            best_tour = tour
    return best_tour, min_cost

# Main function to solve the problem
def main():
    best_tour, min_cost = find_shortest_tour(city_groups)
    full_tour = [0] + list(best_tour) + [0]
    print("Tour:", full_tour)
    print("Total travel cost:", round(min_cost, 2))

# Execute the main function
main()