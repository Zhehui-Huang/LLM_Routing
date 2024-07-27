import math

# Define the coordinates of each city
locations = {
    0: (3, 26),
    1: (85, 72),
    2: (67, 0),
    3: (50, 99),
    4: (61, 89),
    5: (91, 56),
    6: (2, 65),
    7: (38, 68),
    8: (3, 92),
    9: (59, 8),
    10: (30, 88),
    11: (30, 53),
    12: (11, 14),
    13: (52, 49),
    14: (18, 49),
    15: (64, 41),
    16: (28, 49),
    17: (91, 94),
    18: (51, 58),
    19: (30, 48)
}

# Function to calculate the Euclidean distance between two cities
def calculate_distance(city1, city2):
    x1, y1 = locations[city1]
    x2, y2 = locations[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Function to find a tour using a simple greedy algorithm (nearest neighbor heuristic)
def greedy_tsp():
    unvisited = set(locations.keys())
    current_city = 0
    tour = [current_city]
    total_cost = 0
    max_leg = 0
    unvisited.remove(current_city)
    
    while unvisited:
        nearest_city = min(unvisited, key=lambda city: calculate_distance(current_city, city))
        distance = calculate_distance(current_city, nearest_city)
        tour.append(nearest_city)
        total_cost += distance
        max_leg = max(max_leg, distance)
        current_city = nearest_city
        unvisited.remove(nearest_city)

    # Close the tour by returning to the depot city
    final_leg = calculate_distance(current_city, 0)
    tour.append(0)
    total_cost += final_leg
    max_leg = max(max_leg, final_leg)
    
    return tour, total_cost, max_leg

# Execute the TSP solver
tour, total_cost, max_leg = greedy_tsp()

# Print the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_leg:.2f}")