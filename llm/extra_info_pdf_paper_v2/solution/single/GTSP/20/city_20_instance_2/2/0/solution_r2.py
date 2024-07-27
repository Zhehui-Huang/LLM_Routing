import math

# City coordinates as given
cities = [
    (3, 26),   # Depot city 0
    (85, 72),  # City 1
    (67, 0),   # City 2
    (50, 99),  # City 3
    (61, 89),  # City 4
    (91, 56),  # City 5
    (2, 65),   # City 6
    (38, 68),  # City 7
    (3, 92),   # City 8
    (59, 8),   # City 9
    (30, 88),  # City 10
    (30, 53),  # City 11
    (11, 14),  # City 12
    (52, 49),  # City 13
    (18, 49),  # City 14
    (64, 41),  # City 15
    (28, 49),  # City 16
    (91, 94),  # City 17
    (51, 58),  # City 18
    (30, 48)   # City 19
]

# Groupings of the cities
groups = [
    [7, 10, 11, 12],
    [3, 8, 13, 16],
    [2, 4, 15, 18],
    [1, 9, 14, 19],
    [5, 6, 17]
]

def euclidean_distance(city1_index, city2_index):
    x1, y1 = cities[city1_index]
    x2, y2 = cities[city2_index]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def find_shortest_path():
    current_path = [0]  # Start at the depot city
    total_cost = 0

    # Find the minimum distance city from each group to visit
    for group in groups:
        last_city = current_path[-1]
        min_distance = float('inf')
        next_city = group[0]

        # Check each city in the group to find the one with minimum distance from the last city in the current path
        for city in group:
            distance = euclidean_distance(last_city, city)
            if distance < min_distance:
                min_distance = distance
                next_city = city
        
        current_path.append(next_city)
        total_cost += min_distance

    # Return to depot
    return_distance = euclidean_distance(current_path[-1], 0)
    current_path.append(0)
    total_cost += return_distance

    return current_path, total_cost

# Calculate the shortest tour and total cost
optimal_tour, total_travel_cost = find_shortest_path()

print('Tour:', optimal_tour)
print('Total travel cost:', total_travel=objec.distance)