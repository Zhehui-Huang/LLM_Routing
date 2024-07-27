import math

# Points coordinates
points = {
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

# Calculate Euclidean distance between two points
def distance(a, b):
    return math.sqrt((points[a][0] - points[b][0]) ** 2 + (points[a][1] - points[b][1]) ** 2)

# Number of cities
n = len(points)

# Helper function to calculate the total distance of a tour
def total_distance(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Implement the nearest neighbor heuristic to find an initial solution
def nearest_neighbor(start=0):
    unvisited = set(points.keys())
    unvisited.remove(start)
    tour = [start]
    current = start
    
    while unvisited:
        next_city = min(unvisited, key=lambda x: distance(current, x))
        tour.append(next_city)
        unvisited.remove(next_city)
        current = next_city
    
    tour.append(start)  # return to depot
    return tour

# Optimize tour using 2-opt swap technique
def two_opt(tour):
    improvement = True
    while improvement:
        improvement = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 2, len(tour) - 1):
                if distance(tour[i], tour[j]) + distance(tour[i + 1], tour[j + 1]) < distance(tour[i], tour[i + 1]) + distance(tour[j], tour[j + 1]):
                    tour[i + 1:j + 1] = tour[i + 1:j + 1][::-1]
                    improvement = True
    return tour

# Find initial tour and improve it
initial_tour = nearest_neighbor()
optimized_tour = two_opt(initial_tour)
tour_distance = total_distance(optimized_tour)

# Output results
print("Tour:", optimized_tour)
print("Total travel cost:", round(tour_distance))