import math

# City coordinates indexed by their identifier
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# Assuming there are 8 robots, all start at depot city 0
robots = 8
starting_depot = 0

# Function to compute Euclidean distance between two city coordinates
def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    
# Function to allocate cities to robots and compute the paths
def allocate_and_compute():
    # Exclude the depot from the cities to distribute
    city_list = list(cities.keys())
    city_list.remove(starting_depot)
    
    # Determine number of cities per robot
    num_cities = len(city_list)
    cities_per = num_cities // robots
    remainder = num_cities % robots
    
    all_tours = []
    all_costs = []
    start_index = 0
    
    for i in range(robots):
        if i < remainder:
            stop_index = start_index + cities_per + 1
        else:
            stop_index = start_index + cities_per
            
        tour = [starting_depot] + city_list[start_index:stop_wait_index]
        tour_cost = 0
        for j in range(len(tour) - 1):
            tour_cost += euclidean_distance(tour[j], tour[j + 1])
            
        all_tours.append(tour)
        all_costs.append(tour_cost)
        start_index = stop_index

    return all_tours, all_costs

# Get tours and costs
tours, costs = allocate_and_compute()
total_cost = sum(costs)

# Displaying the output in the required format
for i, (tour, cost) in enumerate(zip(tours, costs)):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {cost}")
print(f"Overall Total Travel Cost: {total_cost}")