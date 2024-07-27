import math

# City coordinates and demands
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35), (32, 39), (56, 37)
]
demands = [
    0, 7, 30, 16, 23, 11, 19, 15, 28, 8,
    8, 7, 14, 6, 19, 11, 12, 26, 17, 6,
    15, 5, 10
]

# Robot information
NUM_ROBOTS = 8
ROBOT_CAPACITY = 40

def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

def find_next_city(current_city, visited, current_load):
    min_distance = float('inf')
    next_city = None
    for i in range(1, len(coordinates)):
        if i not in visited and demands[i] <= current_load:
            distance = euclidean_distance(coordinates[current_city], coordinates[i])
            if distance < min_distance:
                min_distance = distance
                next_city = i
    return next_city, min_distance

def generate_tours():
    tours = []
    costs = []
    available_cities = set(range(1, len(coordinates)))
    
    for _ in range(NUM_ROBOTS):
        if not available_cities:
            break
        
        current_city = 0
        tour = [current_city]
        total_cost = 0
        current_load = ROBOT_CAPACITY
        
        while current_load > 0 and available_cities:
            next_city, travel_cost = find_next_city(current_city, tour, current_load)
            if next_city is None:
                break

            tour.append(next_city)
            total_cost += travel_cost
            current_load -= demands[next_city]
            available_cities.remove(next_city)
            current_city = next_city

        # Return to depot
        return_cost = euclidean_distance(coordinates[current_city], coordinates[0])
        total_cost += return_cost
        tour.append(0)

        tours.append(tour)
        costs.append(total_cost)

    return tours, costs

tours, costs = generate_tours()
overall_total_cost = sum(costs)

# Output the results
for idx, (tour, cost) in enumerate(zip(tours, costs)):
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {overall_total_cost}")