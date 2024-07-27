import random
import math
from itertools import permutations

# City coordinates
cities = {
    0: (50, 42),
    1: (41, 1),
    2: (18, 46),
    3: (40, 98),
    4: (51, 69),
    5: (47, 39),
    6: (62, 26),
    7: (79, 31),
    8: (61, 90),
    9: (42, 49)
}

# Function to calculate Euclidean distance between two cities
def calculate_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Generate all possible tours of 4 cities starting and ending at depot (city 0)
def generate_valid_tours():
    all_cities = list(cities.keys())
    all_cities.remove(0)  # Remove the depot for permutations
    all_possible_tours = []
    
    for perm in permutations(all_cities, 3):
        tour = [0] + list(perm) + [0]
        all_possible_tours.append(tour)
    
    return all_possible_tours

# Function to calculate the cost of a tour
def tour_cost(tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += calculate_distance(tour[i], tour[i + 1])
    return cost

# Finding the shortest tour
def find_shortest_tour():
    valid_tours = generate_valid_tours()
    minimal_cost = float('inf')
    best_tour = None
    
    for tour in valid_tours:
        cost = tour_cost(tour)
        if cost < minimal_cost:
            minimal_cost = cost
            best_tour = tour
    
    return best_tour, minimal_cost

# Main function to get the result
def main():
    best_tour, minimal_cost = find_shortest_tour()
    print(f"Tour: {best_tour}")
    print(f"Total travel cost: {minimal_cost:.2f}")

if __name__ == '__main__':
    main()