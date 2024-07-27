import math

# Function to compute Euclidean distance between two points
def euclidean_dist(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# City coordinates
cities = {
    0: (79, 15), # Depot
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

# Groups of cities, each group as a list
groups = [
    [1, 4],
    [2, 6],
    [7],
    [5],
    [9],
    [8],
    [3]
]

# Function to find minimal cost tour given groups and cities
def find_minimal_cost_tour(groups, cities):
    tour = [0]  # Tour start at the depot city 0
    total_dist = 0

    last_city = 0  # Start from the depot
    # Loop through each group to select the nearest city from the current city
    for group in groups:
        nearest_city = None
        min_dist = float('inf')
        for city in group:
            dist = euclidean_dist(cities[last_city], cities[city])
            if dist < min_dist:
                min_dist = dist
                nearest_city = city
        tour.append(nearest_city)
        total_dist += min_dist
        last_city = nearest_city
    
    # Return to the depot
    return_to_depot_dist = euclidean_dist(cities[last_city], cities[0])
    total_dist += return_to_depot_dist
    tour.append(0)  # Closing the loop

    return tour, total_dist

# Getting the minimal cost tour
tour, total_cost = find_minimal_cost_tour(groups, cities)

# Outputting results
print("Tour:", tour)
print("Total travel cost:", total_cost)