import itertools
import math

# Defining the coordinates for each city
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

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Function to calculate the total tour distance
def calculate_tour_distance(tour):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    return total_distanceto

# Function to find the shortest tour
def find_shortest_tour():
    min_distance = float('inf')
    best_tour = None
    
    # Generate all combinations of 3 cities excluding the depot (0), combined with the depot
    for city_combination in itertools.combinations(range(1, 10), 3):
        current_combination = [0] + list(city_combination)
        
        # Generate all permutations of the current combination of 4 cities
        for tour in itertools.permutations(current_combination):
            # Ensure the tour starts and ends at the depot city
            if tour[0] == 0:
                total_distance = calculate_tour_distance(tour + (0,))
                if total_distance < min_distance:
                    min_distance = total_distance
                    best_tour = tour
                    
    return best_tour, min_distance

# Call the function to find the shortest tour and distance
best_tour, min_distance = find_shortest_tour()

# Output
print(f"Tour: {list(best_tour + (0,))}")
print(f"Total travel cost: {min_distance}")