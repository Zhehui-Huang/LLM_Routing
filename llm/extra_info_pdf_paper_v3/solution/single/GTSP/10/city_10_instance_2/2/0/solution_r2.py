import math

# Cities coordinates
cities = {
    0: (90, 3),  # depot
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# Groups of cities
groups = {
    0: [3, 6],
    1: [5, 8],
    2: [4, 9],
    3: [1, 7],
    4: [2]
}

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Find the shortest tour using a heuristic
def find_shortest_tour(groups, start_city):
    tour = [start_city]
    current_city = start_city
    total_cost = 0
    
    # Iterate over each group to find the optimal city to visit from that group
    for group in groups.values():
        next_city = min(group, key=lambda city: distance(current_city, city))
        tour.append(next_city)
        total_cost += distance(current_city, next_city)
        current_city = next_city
    
    # Return to the start/depot city
    total_cost += distance(current_city, start_city)
    tour.append(start_city)
    
    return tour, total_cost

# Calculate the optimal tour and total distance
optimal_tour, optimal_cost = find_shortest_tour(groups, 0)

print(f"Tour: {optimal_tour}")
print(f"Total travel cost: {optimal_cost}")