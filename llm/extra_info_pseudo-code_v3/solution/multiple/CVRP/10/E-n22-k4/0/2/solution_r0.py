import numpy as np

class CVRP:
    def __init__(self, locations, demands, num_robots, capacity):
        self.locations = np.array(locations)
        self.demands = np.array(demands)
        self.num_robots = num_robots
        self.capacity = capacity
        self.num_cities = len(locations)
        self.distance_matrix = self._compute_distance_matrix()
        self.tours = [[] for _ in range(num_robots)]
        self.tour_costs = []

    def _compute_distance_matrix(self):
        num_cities = len(self.locations)
        dist_matrix = np.zeros((num_cities, num_cities))
        for i in range(num_cities):
            for j in range(num_cities):
                if i != j:
                    dist_matrix[i, j] = np.linalg.norm(self.locations[i] - self.locations[j])
        return dist_matrix

    def solve(self):
        unvisited = set(range(1, self.num_cities))  # we skip the depot city 0
        used_capacity = [0] * self.num_robots
        current_city = [0] * self.num_robots  # all start at depot

        self.tours = [[0] for _ in range(self.num_robots)]

        while unvisited:
            for robot in range(self.num_robots):
                next_city = None
                min_distance = float('inf')

                for city in unvisited:
                    if self.distance_matrix[current_city[robot], city] < min_distance and self.demands[city] + used_capacity[robot] <= self.capacity:
                        min_distance = self.distance_matrix[current_city[robot], city]
                        next_city = city

                if next_city is not None:
                    self.tours[robot].append(next_city)
                    used_capacity[robot] += self.demands[next_city]
                    current_city[robot] = next_city
                    unvisited.remove(next_city)

                if used_capacity[robot] >= self.capacity or not unvisited:
                    break

        # Adding depot back to each tour
        self.tour_costs = [0] * self.num_robots
        for robot in range(self.num_robots):
            self.tours[robot].append(0)
            tour_cost = 0
            for i in range(1, len(self.tours[robot])):
                tour_cost += self.distance_matrix[self.tours[robot][i-1]][self.tours[robot][i]]
            self.tour_costs[robot] = tour_cost

        total_cost = sum(self.tour_costs)
        return self.tours, self.tour_costs, total_cost

# Constants
locations = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252),
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]
demands = [0, 1100, 700, 800, 1400, 2100, 400, 800, 100, 500, 600, 1200, 1300, 1300, 300, 900, 2100, 1000, 900, 2500, 1800, 700]
num_robots = 4
capacity = 6000

# Solve the CVRP
cvrp = CVRP(locations, demands, num_robots, capacity)
tours, tour_costs, total_cost = cvrp.solve()

# Output the results
for robot_id in range(num_robots):
    print(f"Robot {robot_id} Tour: {tours[robot_id]}")
    print(f"Robot {robot_id} Total Travel Cost: {tour_costs[robot_id]}")

print(f"Overall Total Travel Cost: {total_cost}")