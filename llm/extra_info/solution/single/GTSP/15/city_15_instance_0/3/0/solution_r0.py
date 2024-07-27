import math

# City coordinates
coordinates = {
    0: (9, 93),
    1: (8, 51),
    2: (74, 99),
    3: (78, 50),
    4: (21, 23),
    5: (88, 59),
    6: (79, 77),
    7: (63, 23),
    8: (19, 76),
    9: (21, 38),
    10: (19, 65),
    11: (11, 40),
    12: (3, 21),
    13: (60, 55),
    14: (4, 39)
}

# Compute the Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Grouping cities
groups = {
    0: [2, 7, 10, 11, 14],
    1: [1, 3, 5, 8, 13],
    2: [4, 6, 9, 12]
}

# Calculate minimum tour and cost by brute-force exploration
def find_minimum_tour():
    min_cost = float('inf')
    best_tour = []
    
    # Iterate over each combination of one city per group
    for city_from_group_0 in groups[0]:
        for city_from_group_1 in groups[1]:
            for city_from_group_2 in groups[2]:
                current_tour = [0, city_from_group_0, city_from_group_1, city_from_group_2, 0]
                current_cost = 0
                for i in range(len(current_tour) - 1):
                    current_cost += distance(current_tour[i], current_tour[i+1])
                
                # Compare and store the minimum cost tour
                if current_cost < min_cost:
                    min_cost = current_cost
                    best_tour = current_tour
    
    return best_tour, min_cost

# Get the minimum tour and its cost
optimal_tour, total_cost = find_minimum_tour()
print("Tour:", optimal_tour)
print("Total travel cost:", round(total_cost, 2))