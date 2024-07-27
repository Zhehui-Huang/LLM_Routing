import itertools
import math

# City coordinates
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

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Function to find the shortest tour visiting exactly k cities including the depot city
def find_shortest_tour(k):
    # All available cities excluding the depot
    other_cities = list(cities.keys())[1:]
    min_tour = None
    min_cost = float('inf')
    
    # Generate all combinations of k-1 cities (since we include the depot automatically)
    for city_combination in itertools.combinations(other_cities, k-1):
        # Full tour includes the depot
        full_tour = [0] + list(city_combination) + [0]
        
        # Generate all permutations of the full tour (excluding start and end point which are the depot)
        for tour_permutation in itertools.permutations(city_combination):
            tour = [0] + list(tour_permutation) + [0]
            tour_cost = sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
            
            # Check if this permutation yields a shorter tour
            if tour_cost < min_cost:
                min_cost = tour_cost
                min_tour = tour
        
    return min_tour, min_cost

# Setting k=8 as specified
k = 8
tour, cost = find_shortest_tour(k)

# Display the results
print(f"Tour: {tour}")
print(f"Total travel cost: {cost}")