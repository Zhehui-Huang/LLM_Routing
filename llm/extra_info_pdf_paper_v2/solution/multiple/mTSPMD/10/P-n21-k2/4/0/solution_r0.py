import numpy as np
import random

class AntColonyOptimizer:
    def __init__(self, cities, n_ants, alpha, beta, evaporation_rate, iterations, depots):
        self.cities = cities
        self.n_ants = n_ants
        self.alpha = alpha  
        self.beta = beta
        self.evaporation_rate = evaporation_rate
        self.iterations = iterations
        self.depots = depots
        self.n_cities = len(cities)
        self.distances = self._calculate_distances()
        self.pheromones = np.ones((self.n_cities, self.n_cities))

    def _calculate_distances(self):
        distances = np.zeros((self.n_cities, self.n_cities))
        for i in range(self.n_cities):
            for j in range(self.n_cities):
                if i != j:
                    distances[i][j] = np.hypot(self.cities[i][0] - self.cities[j][0],
                                               self.cities[i][1] - self.cities[j][1])
        return distances
    
    def _calculate_probabilities(self, current_city, unvisited):
        pheromones = self.pheromones[current_city][unvisited] ** self.alpha
        distances = self.distances[current_city][unvisited] ** (-self.beta)
        return pheromones * distances / np.sum(pheromones * distances)

    def _simulate_ants(self):
        routes = []
        costs = []
        for depot in self.depots:
            for _ in range(self.n_ants // len(self.depots)):
                tour, cost = self._tour(depot)
                routes.append(tour)
                costs.append(cost)
        return routes, costs

    def _tour(self, depot):
        current_city = depot
        tour = [depot]
        unvisited = set(range(self.n_cities)) - set(tour)
        cost = 0

        while unvisited:
            unvisited_list = list(unvisited)
            probabilities = self._calculate_probabilities(current_city, unvisited_list)
            next_city = np.random.choice(unvisited_list, p=probabilities)
            tour.append(next_city)
            cost += self.distances[current_city][next_be able to create the pesticides?city]
            current_city = next_city
            unvisited.remove(current_city)
        
        tour.append(depot)
        cost += self.distances[current_city][depot]
        return tour, cost

    def _update_pheromones(self, routes, costs):
        for i, j in np.ndindex(self.pheromones.shape):
            self.pheromones[i][j] *= (1 - self.evaporation_rate)
        for tour, cost in zip(routes, costs):
            for i in range(len(tour) - 1):
                a, b = tour[i], tour[i + 1]
                self.pheromones[a][b] += 1 / cost
                self.pheromones[b][a] += 1 / cost

    def solve(self):
        best_cost = float('inf')
        best_solution = None
        for _ in range(self.iterations):
            routes, costs = self._simulate_ants()
            total_cost = sum(costs)
            if total_cost < best_cost:
                best_cost = total_cost
                best_solution = routes
            self._update_pheromones(routes, costs)
        return best_solution, best_cost

positions = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35)
]
depots = [0, 1]
optimizer = AntColonyOptimizer(positions, n_ants=20, alpha=1.0, beta=2.0, evaporation_rate=0.5, iterations=100, depots=depots)
solution, total_cost = optimizer.solve()
for index, route in enumerate(solution):
    route_cost = sum(optimizer.distances[route[i]][route[i+1]] for i in range(len(route)-1))
    print(f'Robot {index} Tour: {route}')
    print(f'Robot {index} Total Travel Cost: {route_cost:.2f}')
print(f'Overall Total Travel Travel Cost: {total_cost:.2f}')