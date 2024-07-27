import math
import random
import itertools

# City coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33),
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

# Calculating Euclidean distance
def dist(f, t):
    return math.sqrt((cities[f][0] - cities[t][0])**2 + (cities[f][1] - cities[t][1])**2)

# Rotate a sublist to bring specified item to front
def rotate_to_front(seq, item):
    idx = seq.index(item)
    return seq[idx:] + seq[:idx]

# Perform the Simulated Annealing algorithm
def simulated_annealing(depots, cities):
    # Initialize parameters
    T = 1000.0
    cooling_rate = 0.99
    min_temp = 1

    num_robots = len(depots)
    city_list = list(set(cities.keys()) - set(depots))
    random.shuffle(city_list)

    # Initial partition into almost equal segments
    tours = {i: [depots[i]] for i in range(num_robots)}
    slices = [len(city_list) // num_robots + (1 if x < len(city_list) % num_robots else 0)  for x in range(num_robots)]
    start = 0
    for i, slice_size in enumerate(slices):
        part = city_list[start:start + slice_size]
        tours[i].extend(part)
        start += slice_size

    def total_tour_cost(tours):
        cost = 0
        for key, tour in tours.items():
            local_cost = 0
            for i in range(1, len(tour)):
                local_cost += dist(tour[i - 1], tour[i])
            cost += local_cost
        return cost

    current_cost = total_tour_cost(tours)

    # Start the annealing process
    while T > min_temp:
        # Generate new neighboring solution
        i, j = random.sample(range(num_robots), 2)
        if len(tours[j]) > 1:
            city = random.choice(tours[j][1:])
            tours[j].remove(city)
            tours[i].append(city)
        
        # Calculate new cost
        new_cost = total_tour_cost(tours)
        cost_diff = new_cost - current_cost
        
        # Decide if we should accept the new solution
        if cost_diff < 0 or random.random() < math.exp(-cost_diff / T):
            current_cost = new_cost
        else:
            # Revert move
            tours[i].remove(city)
            tours[j].append(city)
        
        T *= cooling_rate

    return tours, current_cost

# Defining our depots and city mapping
depots = [0, 1, 2, 3, 4, 5, 6, 7]
tours, total_cost = simulated_annealing(depots, cities)

# Output the tours and their costs
overall_total_cost = 0
for i in range(len(depots)):
    tour_cost = sum(dist(tours[i][j], tours[i][j+1]) for j in range(len(tours[i])-1))
    overall_total_cost += tour_cost
    print(f"Robot {i} Tour: {tours[i]}")
    print(f"Robot {i} Total Travel Cost: {tour_cost:.2f}")

print(f"Overall Total Travel Cost: {overall_total_cost:.2f}")