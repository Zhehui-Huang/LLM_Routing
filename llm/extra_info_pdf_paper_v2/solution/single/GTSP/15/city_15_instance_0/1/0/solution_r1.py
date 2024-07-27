import math

# Coordinates of cities
city_positions = {
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

# City groups
city_groups = [
    [2, 7, 10, 11, 14],
    [1, 3, 5, 8, 13],
    [4, 6, 9, 12]
]

# Function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    return math.sqrt((city_positions[city1][0] - city_positions[city2][0])**2 + (city_positions[city1][1] - city_positions[city2][1])**2)

# Calculate pairwise distances (memoization)
distance_matrix = {}
for i in city_positions:
    for j in city_positions:
        distance_matrix[(i, j)] = euclidean_distance(i, j)

# Search for the shortest tour
def find_shortest_tour():
    min_cost = float('inf')
    best_tour = []
    
    # Iterate through each combination of choosing one city from each group
    for g0 in city_groups[0]:
        for g1 in city_groups[1]:
            for g2 in city_groups[2]:
                cities_to_visit = [0, g0, g1, g2, 0]  # tour starting and ending at the depot city (0)
                cost = sum(distance_matrix[(cities_to_visit[i], cities_to_visit[i + 1])] for i in range(len(cities_to_visit) - 1))
                
                if cost < min_cost:
                    min_cost = cost
                    best_tour = cities_to_visit[:]
    
    return best_tour, min_cost

# Finding the optimal solution
best_tour, total_cost = find_shortest_tour()
print("Tour:", best_tour)
print("Total travel cost:", total_cost)