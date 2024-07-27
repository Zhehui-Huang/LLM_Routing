import numpy as np

# Constants
NUM_CITIES = 16
DEPOTS = [0, 1, 2, 3, 4, 5, 6, 7]

# City coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)
]

def calculate_distance(point1, point2):
    """ Calculate Euclidean distance between two points """
    return np.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def nearest_neighbor_solution(depots, coordinates):
    cities = set(range(NUM_CITIES))
    tours = [[] for _ in depots]

    # Assign the nearest non-depot city to each depot
    for i, depot in enumerate(depots):
        nearest_city = None
        min_distance = float('inf')
        for city in cities:
            if city not in depots:
                distance = calculate_distance(coordinates[depot], coordinates[city])
                if distance < min_distance:
                    nearest_city = city
                    min_distance = distance
        if nearest_city is not None:
            tours[i].append(nearest_city)
            cities.remove(nearest_city)

    # Expand tours by assigning closest city available
    change = True
    while change:
        change = False
        for i, depot in enumerate(depots):
            if not tours[i]:
                continue
            current_city = tours[i][-1]
            nearest_city = None
            min_distance = float('inf')
            for city in cities:
                distance = calculate_distance(coordinates[current_city], coordinates[city])
                if distance < min_distance:
                    nearest_city = city
                    min_distance = distance
            if nearest_city is not None:
                tours[i].append(nearest_city)
                cities.remove(nearest_city)
                change = True

    # Append the depots to start of each tour for complete loop
    for i, depot in enumerate(depots):
        tours[i].insert(0, depot)
        tours[i].append(depot)  # Ending at depot for closure, adjust if not needed

    return tours

def total_tour_cost(tour, coordinates):
    cost = 0
    for i in range(len(tour) - 1):
        cost += calculate_distance(coordinates[tour[i]], coordinates[tour[i + 1]])
    return cost

# Generate initial solutions
tours = nearest_neighbor_solution(DEPOTS, coordinates)

# Calculate costs and print results
total_cost_aggregate = 0
for i, tour in enumerate(tours):
    cost = total_tour_cost(tour, coordinates)
    total_cost_aggregate += cost
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {cost:.2f}")

print(f"Overall Total Travel Cost: {total_cost_aggregate:.2f}")