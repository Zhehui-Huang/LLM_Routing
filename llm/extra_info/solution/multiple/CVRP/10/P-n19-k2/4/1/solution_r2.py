import numpy as np

# Coordinates of the cities including the depot
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
    (61, 33), (62, 63), (63, 69), (45, 35)
]

# Demand list for each city
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 14, 8, 7, 14, 19, 11, 26, 17, 6, 15]

# Calculate Euclidean distance
def calculate_distance(city1, city2):
    return np.sqrt((coordinates[city1][0] - coordinates[city2][0])**2 + (coordinates[city1][1] - coordinates[city2][1])**2)

# Distance matrix
num_cities = len(coordinates)
distances = [[calculate_distance(i, j) for j in range(num_cities)] for i in range(num_cities)]

def find_tours():
    tours = [[] for _ in range(2)]
    loads = [0] * 2
    city_assignment = [False] * num_cities
    city_assignment[0] = True
    available_cities = set(range(1, num_cities))

    while available_cities:
        for robot in range(2):
            if not tours[robot]:
                tours[robot].append(0)
            current_city = tours[robot][-1]
            next_city = None
            min_dist = float('inf')
            
            for city in available_cities:
                if loads[robot] + demands[city] <= 160 and distances[current_city][city] < min_dist:
                    min_dist = distances[current_city][city]
                    next_city = city

            if next_city is not None:
                tours[robot].append(next_city)
                loads[robot] += demands[next_city]
                city_assignment[next_city] = True
                available_cities.remove(next_city)

            if not available_cities or (loads[robot] + min(demands) > 160):
                tours[robot].append(0)
                break
        
    return tours, loads

tours, loads = find_tours()

def calculate_total_travel_cost(tours):
    total_cost = 0
    for tour in tours:
        cost = sum(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
        total_cost += cost
        print(f"Tour: {tour}, Cost: {cost}")
    return total_cost

total_cost = calculate_total_travel_cost(tours)
print(f"Overall Total Travel Cost: {total_cost}")