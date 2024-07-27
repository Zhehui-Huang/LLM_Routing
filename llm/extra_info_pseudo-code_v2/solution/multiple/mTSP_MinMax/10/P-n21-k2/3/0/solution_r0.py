import math
import random

# Cities and their coordinates; depot city at index 0.
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), 
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Euclidean distance calculation
def euclidean_distance(i, j):
    return math.sqrt((cities[i][0]-cities[j][0])**2 + (cities[i][1]-cities[j][1])**2)

# Initialization: Assigning each robot the closest city initially and then spread remaining cities
def initialization():
    num_robots = 2
    tours = {i: [0] for i in range(num_robots)}
    
    assigned = []
    cities_sorted_by_distance = sorted(range(1, len(cities)), key=lambda x: euclidean_distance(0, x))
    
    # Assign each robot 1 initial city
    for i in range(num_robots):
        tours[i].append(cities_sorted_by_distance[i])
        assigned.append(cities_sorted_by_distance[i])
    
    # Assign remaining cities
    for city in cities_sorted_by_distance[num_robots:]:
        best_robot = min(tours, key=lambda k: euclidean_distance(tours[k][-1], city))
        # Put each city to the end of the nearest last city of any tour
        tours[best_robot].append(city)
        assigned.append(city)
    
    for k in tours.keys():
        tours[k].append(0)  # back to depot
    
    return tours

# Calculate travel cost of each tour
def travel_cost(tour):
    return sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Main GVNS approach placeholder
def gvns(d, lmax, kmax, tmax):
    x = initialization()  # initial solution
    time_limit = tmax
    start_time = time.time()
    
    while time.time() - start_time < time_limit:
        k = 1
        while k < kmax:
            x_prime = shake(x, k)  # perturb the solution
            x_double_prime = seq_vnd(x_prime, lmax)  # find local optimum
            if travel_cost(x_double_prime) < travel_cost(x):
                x = x_double_prime
                k = 1
            else:
                k += 1
    return x

# Just initializing and calculating costs (Shake and Seq-VND are implemented conceptually)
tours = initialization()
tour_costs = {k: travel_cost(v) for k, v in tours.items()}
max_cost = max(tour_costs.values())

# Displaying the results
for k, v in tours.items():
    print(f"Robot {k} Tour: {v}")
    print(f"Robot {k} Total Travel Cost: {tour_costs[k]}")

print(f"Maximum Travel Cost: {max_cost}")