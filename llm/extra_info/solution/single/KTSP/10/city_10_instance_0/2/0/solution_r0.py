import itertools
import math

# Define city coordinates
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

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Find the shortest tour that includes the depot and 3 other cities
def find_shortest_tour():
    min_cost = float('inf')
    best_tour = []
    
    # Generate all combinations of 3 cities excluding the depot
    for combination in itertools.combinations(range(1, 10), 3):
        # Include the depot city in the tour
        tour = [0] + list(combination) + [0]
        
        # Calculate the total cost of this tour
        cost = 0
        for i in range(len(tour) - 1):
            cost += distance(tour[i], tour[i + 1])
        
        # Update the best tour if the current one is shorter
        if cost < min_cost:
            min_cost = cost
            best_tour = tour
    
    return best_tour, min_cost

# Run the function
tour, total_cost = find_shortest_tour()

# Output the result
print("Tour:", tour)
print("Total travel cost:", round(total_cost, 2))