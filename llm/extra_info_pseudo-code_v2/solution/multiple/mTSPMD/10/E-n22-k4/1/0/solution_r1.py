import numpy as np
from math import sqrt

class ACO:
    def __init__(self, coordinates, num_robots, num_ants=10, alpha=1.0, beta=2.0, rho=0.5, cyclenum=100):
        self.coordinates = coordinates
        self.num_robots = num_robots
        self.num_ants = num_ants
        self.alpha = alpha
        self.beta = beta
        self.rho = rho
        self.cyclenum = cyclenum
        self.num_cities = len(coordinates)
        self.d_matrix = np.zeros((self.num_cities, self.num_cities))
        self.pheromone = np.ones((self.num_cities, self.num_cities)) * 0.1
        
        # Initialize distance matrix
        for i in range(self.num_cities):
            for j in range(self.num_cities):
                if i != j:
                    self.d_matrix[i][j] = sqrt((coordinates[i][0] - coordinates[j][0])**2 + (coordinates[i][1] - coordinates[j][1])**2)
                else:
                    self.d_matrix[i][j] = float('inf')

    def solve(self):
        best_cost = float('inf')
        best_solution = None

        for cycle in range(self.cyclenum):
            solutions = []
            costs = []
            
            for ant in range(self.num_ants):
                tours = [[] for _ in range(self.num_robots)]
                for robot in range(self.num_robots):
                    tours[robot].append(robot)  # init tour at robot's depot

                remaining_cities = set(range(self.num_robots, self.num_cities))
                while remaining_cities:
                    for robot in range(self.num_robots):
                        if remaining_cities:
                            current_city = tours[robot][-1]
                            next_city = self.select_next_city(current_city, remaining_cities)
                            tours[robot].append(next_city)
                            remaining_cities.remove(next_city)
                
                # Closing the tour at the respective robot's depot
                for robot in range(self.num_robots):
                    tours[robot].append(robot)

                total_cost = self.evaluate(tours)
                costs.append(total_cost)
                solutions.append(tours)

                if total_cost < best_cost:
                    best_cost = total_cost
                    best_solution = tours
            
            # Pheromone update
            self.update_pheromone(solutions, costs)

        return best_solution, best_cost

    def select_next_city(self, current_city, allowed_cities):
        probabilities = np.zeros(self.num_cities)
        allowed_list = list(allowed_cities)
        denominator = sum((self.pheromone[current_city][j] ** self.alpha) * ((1.0 / self.d_matrix[current_city][j]) ** self.beta) for j in allowed_list)
        for city in allowed_list:
            probabilities[city] = ((self.pheromone[current_city][city] ** self.alpha) * 
                                   ((1.0 / self.d_matrix[current_city][city]) ** self.beta)) / denominator
        next_city = np.random.choice(allowed_list, p=probabilities[allowed_list])
        return next_city

    def evaluate(self, tours):
        total_cost = 0
        for tour in tours:
            tour_cost = 0
            for i in range(len(tour) - 1):
                tour_cost += self.d_matrix[tour[i]][tour[i+1]]
            total_cost += tour_cost
        return total_cost

    def update_pheromone(self, solutions, costs):
        self.pheromone *= (1 - self.rho)  # Evaporation
        for solution, cost in zip(solutions, costs):
            for tour in solution:
                for i in range(len(tour) - 1):
                    self.pheromone[tour[i]][tour[i+1]] += 1.0 / cost

# City coordinates, including depots
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254),
    (128, 252), (163, 247), (146, 246), (161, 242),
    (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208),
    (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]

aco = ACO(coordinates, num_robots=4)
best_solution, best_cost = aco.solve()

print("Optimal tours and costs:")
overall_cost = 0
for i, tour in enumerate(best_solution):
    tour_cost = sum(aco.d_matrix[tour[j]][tour[j+1]] for j in range(len(tour)-1))
    print(f'Robot {i} Tour: {tour}')
    print(f'Robot {i} Total Travel Cost: {tour_cost}')
    overall_cost += tour_cost

print(f'Overall Total Travel Cost: {overall_cost}')