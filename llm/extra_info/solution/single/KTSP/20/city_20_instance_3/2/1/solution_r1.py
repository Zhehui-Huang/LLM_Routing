import math
import itertools

# Define cities coordinate
cities = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57), 5: (6, 58), 6: (12, 84),
    7: (72, 77), 8: (98, 95), 9: (11, 0), 10: (61, 25), 11: (52, 0), 12: (60, 95), 13: (10, 94),
    14: (96, 73), 15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

# Function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Calculate all pairs distances
distances = {}
for i in cities:
    for j in cities:
        if i != j:
            distances[(i, j)] = euclidean_distance(cities[i], cities[j])

# Solve the TSP variant
def select_and_solve_tsp(all_cities, num_cities=13):
    min_tour = []
    min_cost = float('inf')
    
    for chosen_cities in itertools.combinations(all_cities.keys() - {0}, num_cities - 1):
        total_cities = [0] + list(chosen_cities) + [0]  # Start and end at the depot
        
        # Finding an optimal tour among these cities by brute-force searching all permutations
        for permuted_cities in itertools.permutations(total_cities[1:-1]):
            curr_tour = [0] + list(permuted_cities) + [0]
            curr_cost = sum(distances[(curr_tour[i], curr_tour[i+1])] for i in range(len(curr_tour) - 1))
            
            if curr_cost < min_cost:
                min_cost = curr_cost
                min_tour = curr_tour
                
    return min_tour, min_cost

# Main execution to find the best tour out of the given cities
optimal_tour, optimal_cost = select_and_solve_tsp(cities)

print(f"Tour: {optimal_tour}")
print(f"Total travel cost: {optimal_cost}")