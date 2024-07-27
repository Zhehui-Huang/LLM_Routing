import numpy as np

class AntColonyOptimizer:
    def __init__(self, cities, n_ants, alpha, beta, evaporation_rate, iterations, depots):
        self.cities = cities
        self.n_ants = n_ants
        self.alpha = alpha  # influence of pheromone on direction
        self.beta = beta  # influence of distance on direction
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
        visible = (1 / self.distances[current_city][unvisited]) ** self.beta
        return pheromones * visible / np.sum(pheromones * visible)

    def _update_pheromones(self, routes, costs):
        for i, j in np.ndindex(self.pheromones.shape):
            self.pheromones[i][j] *= (1 - self.evaporation_rate)
        for tour, cost in zip(routes, costs):
            for i in range(len(tour) - 1):
                a, b = tour[i], tour[i + 1]
                self.pheromones[a][b] += 1 / cost
                self.pheromones[b][a] += 1 / cost

    def _simulate_ants(self):
        best_route = None
        best_cost = float('inf')
        for _ in range(self.n_ants):
            for depot in self.depots:
                route = self._construct_solution(depot)
                cost = sum(self.distances[route[i]][route[i+1]] for i in range(len(route) - 1))
                if cost < best_cost:
                    best_cost = cost
                    best_route = route
        return best_route, best_cost

    def _construct_solution(self, depot):
        route = [depot]
        current_city = depot
        to_visit = set(range(self.n_cities)) - {depot}
        while to_visit:
            probabilities = self._calculate_probabilities(current_city, list(to_visit))
            next_city = np.random.choice(list(to_visit), p=probabilities)
            route.append(next_city)
            to_visit.remove(next_city)
            current_city = next_city
        route.append(depot)
        return route

    def solve(self):
        for _ in range(self.iterations):
            route, cost = self._simulate_ants()
            self._update_pheromones([route], [cost])
        return route, cost

positions = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35)
]
depots = [0, 1]
optimizer = AntColonyOptimizer(positions, n_ants=10, alpha=1.0, beta=5.0, evaporation_rate=0.5, iterations=100, depots=depots)
solution, total_cost = optimizer.solve()

print(f'Final Tour: {solution}')
print(f'Total Travel Cost: {total_cost:.2f}')