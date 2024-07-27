import math
import random

# Cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69), 20: (45, 35)
}

# Euclidean distance function
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Travel cost of a tour
def tour_cost(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Initialization
def initialization():
    nodes = list(cities.keys())[1:]  # Exclude the depot
    random.shuffle(nodes)
    half = len(nodes) // 2
    tours = [nodes[:half], nodes[half:]]
    for tour in tours:
        tour.insert(0, 0)
        tour.append(0)
    return tours

# Shaking: Relocate a random node from one tour to the other
def shake(tours):
    from_tour = random.choice(tours)
    if len(from_tour) <= 3:
        # Prevent breaking tours with only depot and one city
        return tours

    node = random.choice(from_tour[1:-1])
    from_tour.remove(node)

    # Choose another tour to insert into
    to_tour = random.choice([tour for tour in tours if tour != from_tour])
    insert_pos = random.randint(1, len(to_tour) - 1)
    to_tour.insert(insert_pos, node)
    return tours

# Sequential Variable Neighborhood Descent
def seq_vnd(tours):
    improved = True
    while improved:
        improved = False
        for tour in tours:
            best_cost = tour_cost(tour)
            for i in range(1, len(tour) - 2):
                for j in range(i+1, len(tour) - 1):
                    new_tour = tour[:]
                    new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
                    new_cost = tour_cost(new_tour)
                    if new_cost < best_cost:
                        tour[i], tour[j] = tour[j], tour[i]
                        best_cost = new_cost
                        improved = True
    return tours

# GVNS main function
def gvns(k_max, max_iter):
    tours = initialization()
    for _ in range(max_iter):
        current_max_cost = max(tour_cost(tour) for tour in tours)
        k = 1
        while k <= k_max:
            new_tours = shake([t[:] for t in tours])
            new_tours = seq_vnd(new_tours)
            new_max_cost = max(tour_cost(tour) for tour in new_tours)
            if new_max_cost < current_max_cost:
                tours = new_tours
                current_max_cost = new_max_cost
                k = 1
            else:
                k += 1
    return tours

# Parameters setup
k_max = 5
max_iter = 100
final_tours = gvns(k_max, max_iter)
robot_tour_costs = [tour_cost(tour) for tour in final_tours]
max_travel_cost = max(robot_tour_costs)

for index, tour in enumerate(final_tours):
    print(f"Robot {index} Tour: {tour}")
    print(f"Robot {index} Total Travel Cost: {robot_tour_costs[index]}")

print(f"Maximum Travel Cost: {max_travel_cost}")