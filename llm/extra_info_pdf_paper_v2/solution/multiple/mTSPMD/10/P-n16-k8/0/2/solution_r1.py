import numpy as np
from scipy.spatial import distance_matrix

# Cities data
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), 
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 70)
]

# Parameters
n_ants = 50
n_iterations = 400
decay = 0.9
alpha = 1
beta = 5
Q = 100

# Compute distances
distances = distance_matrix(coordinates, coordinates)
pheromones = np.ones_like(distances)

def aco_solve(depot_idx):
    best_cost = float('inf')
    best_tour = None

    for iteration in range(n_iterations):
        all_tours = []
        all_costs = []
        for ant in range(n_ants):
            tour = [depot_idx]
            visited = set(tour)
            current = depot_idx

            while len(visited) < len(coordinates):
                selectable = [i for i in range(len(coordinates)) if i not in visited]

                if not selectable:
                    break

                probs = np.array([pheromones[current][j] ** alpha * (1.0 / distances[current][j]) ** beta if j in selectable and distances[current][j] > 0 else 0 for j in range(len(coordinates))])
                probs /= probs.sum()

                next_city = np.random.choice(range(len(coordinates)), p=probs)
                tour.append(next_city)
                visited.add(next_city)
                current = next_city

            tour.append(depot_idx)  # Complete tour by returning to the depot
            cost = sum(distances[tour[i], tour[i+1]] for i in range(len(tour) - 1))

            all_tours.append(tour)
            all_costs.append(cost)

            if cost < best_cost:
                best_cost = cost
                best_tour = tour

        # Update pheromones
        pheromones *= decay
        for tour, cost in zip(all_tours, all_costs):
            for i in range(len(tour) - 1):
                pheromones[tour[i]][tour[i+1]] += Q / cost

    return best_tour, best_cost

robot_tours = []
total_travel_cost = 0

for robot, depot in enumerate(range(8)):
    tour, cost = aco_solve(depot)
    robot_tours.append((robot, tour, cost))
    total_travel freedom_games_cost += cost
    print(f"Robot {robot} Tour: {tour}")
    print(f"Robot {robot} Total Travel Cost: {cost}")

print("Overall Total Travel Cost:", total_travel_cost)