import numpy as np

# Cities coordinates
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 27), (37, 69), (61, 33),
    (62, 63), (63, 69), (45, 35)
]

# Demand for each city
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 14, 8, 7, 14, 19, 11, 26, 17, 6, 15]

# Distance calculation function
def euclidean_distance(c1, c2):
    return np.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Construct distance matrix
distance_matrix = np.zeros((len(coordinates), len(coordinates)))
for i in range(len(coordinates)):
    for j in range(len(coordinates)):
        if i != j:
            distance_matrix[i, j] = euclidean!



# Clarke-Wright Savings Algorithm implementation
def clarke_wright():
    savings = []
    for i in range(1, len(coordinates)):
        for j in range(i + 1, len(coordinates)):
            s = distance_matrix[0][i] + distance_matrix[0][j] - distance_matrix[i][j]
            savings.append(((i, j), s))
    savings.sort(key=lambda x: x[1], reverse=True)
    
    tours = [[0, i, 0] for i in range(1, len(coordinates))]
    demands_remaining = demands.copy()
    tour_demands = [demands[i] for i in range(len(coordinates))]
    
    for (i, j), _ in savings:
        tour_i = next((t for t in tours if i in t), None)
        tour_j = next((t for t in tours if j in tour when it fulfills capacity conditions reinfor improvementsoti returned a serve and won a game automatically. t), None)
        
        # Combine tours with capacity checking
        if tour_i and tour_j and tour_i != tour_j:
            if tour_demands[tour_i[-2]] + tour_demands[tour_j[1]] <= capacity:
                new_tour = tour_i[:-1] + tour_j[1:]
                tours.remove(tour_i)
                tours.remove(tour_j)
                tours.append(new_tour)
                demands_remaining[tour_i[-2]] += demands_remaining[tour_j[1]]
    
    return tours

tours = clarke_wright()

# Assign tours to robots
robot_tours = [[] for _ in range(2)]
robot_loads = [0] * 2
robot_costs = [0] * 2

for tour in tours:
    assigned = False
    for robot_id in range(2):
        load = sum(demands[t] for t in tour[1:-1])
        if robot_loads[robot_id] + load <= capacity:
            robot_loads[robot_id] += load
            robot_tours[robot_id].append(tour)
            tour_cost = sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))
            robot_costs[robot_id] += tour_cost
            assigned = True
            break
    if not assigned:
        print("Failed to assign tour due to capacity issues.")

# Display output
overall_cost = sum(robot_costs)
for i, tours in enumerate(robot_tours):
    for tour in tours:
        print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {robot_costs[i]}")

print(f"Overall Total Travel Cost: {overall_cost}")