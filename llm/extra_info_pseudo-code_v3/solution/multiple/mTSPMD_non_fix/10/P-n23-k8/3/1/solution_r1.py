import numpy as np

# Coordinates for all the cities including depots
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]

# Calculate distances matrix using Euclidean distance
n_cities = len(coordinates)
distances = np.zeros((n_cities, n_cities))

for i in range(n_cities):
    for j in range(n_cities):
        if i != j:
            distances[i][j] = np.sqrt((coordinates[i][0] - coordinates[j][0])**2 + (coordinates[i][1] - coordinates[j][1])**2)

# Nearest Neighbor Search (NNS) algorithm initialization
num_robots = 8
tours = [[] for _ in range(num_robots)]
visited = set()

# Initialize by assigning the closest city to each robot from the depot
depot = 0
for robot in range(num_robots):
    min_dist = float('inf')
    chosen_city = None
    for city in range(n_cities):
        if city not in visited and city != depot:
            dist = distances[depot][city]
            if dist < min_dist:
                min_dist = dist
                chosen_city = city
    if chosen_city is not None:
        tours[robot].append(depot)
        tours[robot].append(chosen_city)
        visited.add(chosen_city)

# Assign remaining cities
remaining_cities = set(range(n_cities)) - visited
while remaining_cities:
    for robot in range(num_robots):
        if not remaining_cities:
            break
        last_city = tours[robot][-1]
        min_dist = float('inf')
        chosen_city = None
        for city in remaining_cities:
            dist = distances[last_city][city]
            if dist < min_dist:
                min_dist = dist
                chosen_city = city
        if chosen_city is not None:
            tours[robot].append(chosen_city)
            visited.add(chosen_city)
            remaining_cities.remove(chosen_city)

# Calculation of tour costs
tour_costs = []
total_cost = 0
for idx, tour in enumerate(tours):
    cost = 0
    if len(tour) > 1:  # Calculate cost if there's a meaningful tour
        for i in range(len(tour)-1):
            cost += distances[tour[i]][tour[i+1]]
    tour_costs.append(cost)
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {cost:.2f}")
    total_cost += cost

# Print total cost for all tours
print(f"Overall Total Travel Cost: {total_cost:.2f}")