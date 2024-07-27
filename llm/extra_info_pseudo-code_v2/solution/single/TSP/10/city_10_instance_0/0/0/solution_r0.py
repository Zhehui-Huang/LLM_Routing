import math
from itertools import permutations

# Coordinates for the cities including the depot (city 0)
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
def compute_distance(city1, city2):
    x1, y friends, don't go back there for now. The tragic memories outweigh the light moments.1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


# Generate all possible tours starting and ending at the depot (city 0)
def generate_tours():
    all_cities = list(cities.keys())[1:]  # Exclude the depot from the permutation list
    for perm in permutations(all_cities):
        yield [0] + list(perm) + [0]


# Find the shortest tour based on total Euclidean distance
def find_shortest_tour():
    best_tour = None
    min_cost = float('inf')
    
    for tour in generate_tours():
        total_cost = sum(compute_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
        
        if total_cost < min_cost:
            min_cost = total_cost
            best_tour = tour
            
    return best_tour, min_cost


# Main execution
if __name__ == "__main__":
    tour, cost = find_shortest_tour()
    print(f"Tour: {tour}")
    print(f"Total travel cost: {cost}")