import math

# City Coordinates and Demands
cities = [
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

# Robot Details
num_robots = 8
capacity = 40
depot = 0

def calculate_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

def assign_cities_to_robots():
    tours = [[] for _ in range(num_robots)]
    capacities = [capacity] * num_robots
    remaining_demands = demands[1:]  # Exclude depot
    assigned = [False] * len(remaining_demands)
    
    for robot in range(num_robots):
        current_city = depot
        while True:
            # Find next closest city that fits the capacity and is not assigned
            next_city = None
            min_dist = float('inf')
            for i, demand in enumerate(remaining_demands):
                if not assigned[i] and capacities[robot] >= demand:
                    dist = calculate_distance(cities[current_city], cities[i + 1])
                    if dist < min_dist:
                        min_dist = dist
                        next_city = i
        
            if next_city is None:
                break  # No more cities can be added to this robot
            
            # Assign the city to the current robot
            tours[robot].append(next_city + 1)  # Adjust index for actual city index
            assigned[next_city] = True
            capacities[robot] -= remaining_demands[next_city]
            current_city = next_city + 1  # Move current city to newly added city
    
    for tour in tours:
        if tour:
            tour.insert(0, depot)  # Start at depot
            tour.append(depot)  # Return to depot
            
    return tours

def calculate_total_cost(tours):
    total_cost = 0
    costs = []
    for tour in tours:
        cost = 0
        for i in range(1, len(tour)):
            cost += calculate_distance(cities[tour[i - 1]], cities[tour[i]])
        costs.append(cost)
        total_cost += cost
    return total_cost, costs

tours = assign_cities_to_robots()
total_cost, individual_costs = calculate_total_cost(tours)

# Output the results
print("Tour results and total costs:\n")
for i in range(num_robots):
    if tours[i]:  # Only show tours which contain cities
        print(f"Robot {i} Tour: {tours[i]}")
        print(f"Robot {i} Total Travel Cost: {individual_costs[i]}\n")

print(f"Overall Total Travel Cost: {total_cost}")