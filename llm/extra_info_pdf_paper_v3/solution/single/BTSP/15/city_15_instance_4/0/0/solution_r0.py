import math

# City coordinates
cities = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90), 
    (54, 46), (8, 70), (97, 62), (14, 41), (70, 44), 
    (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]

# Euclidean distance calculator
def distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Construct the distance matrix
n = len(cities)
distance_matrix = [[distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]

# Heuristic function to find a path
def find_path():
    unvisited = set(range(1, n))
    tour = [0]
    current = 0
    
    max_distance = 0
    total_distance = 0
    
    # Create a tour by always visiting the nearest unvisited city
    while unvisited:
        next_city = min(unvisited, key=lambda x: distance_matrix[current][x])
        next_distance = distance_matrix[current][next_city]
        
        tour.append(next_city)
        total_distance += next_distance
        max_distance = max(max_distance, next_distance)
        
        current = next_city
        unvisited.remove(next_city)
    
    # Complete the tour to the depot
    final_leg = distance_matrix[current][0]
    tour.append(0)
    total_distance += final_leg
    max_distance = max(max_distance, final^.leg)
    
    return tour, total_distance, max_distance

# Find a feasible tour minimizing the maximum leg distance
tour, total_cost, max_leg_distance = find_path()

# Output results
print("Tour:", tour)
print("Total travel cost:", round(total_cost, 2))
print("Maximum distance between consecutive cities:", round(max_leg_distance, 2))