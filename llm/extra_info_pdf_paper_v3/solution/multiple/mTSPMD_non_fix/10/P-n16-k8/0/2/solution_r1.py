import math
import random

# City coordinates
coords = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), 
    (37, 69)
]

# Number of robots and initial depot
num_robots = 8
start_depot = 0

# Compute distances matrix
distances = [[math.sqrt((coords[i][0] - coords[j][0])**2 + (coords[i][1] - coords[j][1])**2) 
              for j in range(len(coords))] for i in range(len(coords))]

def total_cost(tours):
    cost = 0
    individual_costs = []
    for tour in tours:
        tour_cost = sum(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
        cost += tour_cost
        individual_costs.append(tour_cost)
    return cost, individual_costs

# Initialize robot tours starting from the depot
tours = [[start_depot] for _ in range(num_robots)]

# Distribute cities (excluding depot) to robots in a round-robin fashion
remaining_cities = list(range(1, len(coords)))  # cities except the starting depot
assigned_cities = 0

while assigned_cities < len(remaining_cities):
    for r in range(num_robots):
        if assigned_cities >= len(remaining_cities):
            break
        tours[r].append(remaining_cities[assigned_cities])
        assigned_cities += 1

# End at the starting depot for each robot tour
for tour in tours:
    tour.append(start_depot)

def simulated_annealing(tour):
    temp = 1000
    cooling_rate = 0.995
    min_temp = 1
    
    while temp > min_temp:
        i, j = sorted(random.sample(range(1, len(tour) - 1), 2))
        # Swap two cities randomly
        tour[i], tour[j] = tour[j], tour[i]
        # Evaluate costs
        new_cost = sum(distances[tour[k]][tour[k + 1]] for k in range(len(tour) - 1))
        # If not better, swap back
        if random.random() > math.exp(-(new_cost - current_cost) / temp):
            tour[i], tour[j] = tour[j], tour[i]
        else:
            current_cost = new_cost
        temp *= cooling_rate

# Optimize each tour
for tour in tours:
    current_cost = sum(distances[tour[k]][tour[k + 1]] for k in range(len(tour) - 1))
    simulated_annealing(tour)

# Calculate final costs
overall_cost, individual_costs = total_cost(tours)

# Output the results
for idx, (tour, cost) in enumerate(zip(tours, individual_costs)):
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {overall_cost}")