import math

# Cities coordinates
cities = {
    0: (35, 40),
    1: (39, 41),
    2: (81, 30),
    3: (5, 50),
    4: (72, 90),
    5: (54, 46),
    6: (8, 70),
    7: (97, 62),
    8: (14, 41),
    9: (70, 44),
    10: (27, 47),
    11: (41, 74),
    12: (53, 80),
    13: (21, 21),
    14: (12, 39)
}

# Function to compute Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Greedy approach to solving k-TSP
def greedy_k_tsp(start, k):
    n = len(cities)
    visited = set([start])
    tour = [start]
    current = start

    while len(visited) < k:
        next_city = None
        min_dist = float('inf')
        
        for city in range(n):
            if city not in visited and distance(current, city) < min_dist:
                min_dist = distance(current, city)
                next_city = city
        
        visited.add(next_city)
        tour.append(next_city)
        current = next_city
    
    # Close the tour by returning to the start
    tour.append(start)
    return tour

# Function to calculate total travel cost of the tour
def calculate_tour_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += distance(tour[i], tour[i + 1])
    return total_cost

# Run the algorithm for exactly k cities including the depot
k = 12  # including the depot
tour = greedy_k_tsp(0, k)
tour_cost = calculate_tour_cost(tour)

# Print the resulting tour and its cost
print("Tour:", tour)
print("Total travel cost:", tour_cost)