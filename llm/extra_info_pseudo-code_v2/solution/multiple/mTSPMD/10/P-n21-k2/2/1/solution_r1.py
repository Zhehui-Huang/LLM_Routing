import numpy as np

# Coordinates given for each city including depots
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), 
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), 
    (45, 35)
]

# Parameters for ACO
num_cities = len(coordinates)
antnum = 5
cyclenum = 50
inittrail = 1.0
alpha = 1
beta = 5
rho = 0.8

# Calculate all pairwise distances
def euclidean_distance(coord1, coord2):
    return np.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

distances = np.array([[euclidean_distance(coordinates[i], coordinates[j])
                       for j in range(num_cities)] for i in range(num_cities)])
pheromone = np.ones((num_cities, num_cities)) * inittrail
heuristic = 1 / (distances + 1e-10)

def solve_tsp_ants():
    best_cost = np.inf
    best_solution = None

    for cycle in range(cyclenum):
        for ant in range(antnum):
            # Robots initialize at their respective depots
            starting_points = [0, 1]
            tours = [[] for _ in starting_points]
            costs = [0 for _ in starting_points]

            for r in range(len(starting_points)):
                current = starting_points[r]
                tours[r].append(current)
                allowed = set(range(num_cities)) - {current}

                while allowed:
                    transitions = np.zeros(num_cities)
                    for j in allowed:
                        transitions[j] = pheromone[current, j]**alpha * heuristic[current, j]**beta
                    transitions /= transitions.sum()

                    next_city = np.random.choice(num_cities, p=transitions)
                    tours[r].append(next_city)
                    costs[r] += distances[current, next_city]
                    current = next_city
                    allowed.remove(next city)

                # Return to start depot
                tours[r].append(starting_points[r])
                costs[r] += distances[current, starting_points[r]]

            total_cost = sum(costs)
            
            # Check for best solution
            if total_cost < best_cost:
                best_cost = total_cost
                best_solution = tours

            # Update pheromones
            pheromone *= (1 - rho)  # Evaporation
            for r in range(len(tours)):
                for i in range(len(tours[r]) - 1):
                    a, b = tours[r][i], tours[r][i+1]
                    pheromone[a, b] += 1.0 / costs[r]  # Pheromone addition

    return best_solution, best_cost

best_solution, best_cost = solve_tsp_ants()
robot_tours = [{"Tour": tour, "Cost": np.sum([distances[tour[i], tour[i + 1]] for i in range(len(tour) - 1)])} for tour in best_solution]

# Pretty print the output
print("\n")
for idx, robot_tour in enumerate(robot_tours):
    print(f"Robot {idx} Tour: {robot_tour['Tour']}")
    print(f"Robot {idx} Total Travel Cost: {robot_tour['Cost']:.2f}")

print(f"\nOverall Total Travel Cost: {best_cost:.2f}")