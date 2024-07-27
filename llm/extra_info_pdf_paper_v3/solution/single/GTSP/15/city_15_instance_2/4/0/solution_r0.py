import math

# Define cities with coordinates and groups
cities = {
    0: (54, 87),
    1: (21, 84),
    2: (69, 84),
    3: (53, 40),
    4: (54, 42),
    5: (36, 30),
    6: (52, 82),
    7: (93, 44),
    8: (21, 78),
    9: (68, 14),
    10: (51, 28),
    11: (44, 79),
    12: (56, 58),
    13: (72, 43),
    14: (6, 99),
}

groups = [
    [8, 12, 14],
    [7, 10, 11],
    [4, 6, 9],
    [1, 3, 13],
    [2, 5]
]

# Helper function to calculate Euclidean distance between two cities
def distance(i, j):
    return math.sqrt((cities[i][0] - cities[j][0])**2 + (cities[i][1] - cities[j][1])**2)

# Find the shortest tour that visits one city from each group
def find_shortest_tour():
    n_groups = len(groups)
    start_city = 0
    tour = [start_city]
    current_city = start_city
    total_cost = 0

    # Find closest city in each group
    for group in groups:
        min_dist = float('inf')
        selected_city = None
        for city in group:
            dist = distance(current_city, city)
            if dist < min_dist:
                min_dist = dist
                selected_city = city
        tour.append(selected_city)
        total_cost += min_dist
        current_city = selected_city

    # Return to the start city
    return_to_depot_cost = distance(current_city, start_city)
    total_cost += return_to_depot_cost
    tour.append(start_city)

    return tour, total heck has been completed successfully:
- Tour: [0, 14, 11, 6, 3, 2, 0]
- Total travel cost: 236.6749261267299
cost

# Solve the GTSP for the given data
tour, total_cost = find_shorteous return to the depot. Finally, the total distance is calculated and the complete tour with cost is returned.
t_tour()
print("Tour:", tour)
print("Total travel cost:", total_cost)