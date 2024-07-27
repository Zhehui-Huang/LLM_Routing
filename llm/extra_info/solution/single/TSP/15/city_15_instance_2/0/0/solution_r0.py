import math
from simanneal import Annealer

# Calculate the Euclidean distance between two points
def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y1 - y2) ** 2)

# Define the problem by extending the Annealer class
class TSPSolver(Annealer):
    def move(self):
        """Swaps two cities in the tour."""
        a = random.randint(1, len(self.state) - 3)
        b = random.randint(a + 1, len(self.state) - 2)
        self.state[a], self.state[b] = self.state[b], self.state[a]

    def energy(self):
        """Calculates the total length of the tour."""
        e = 0
        for i in range(len(self.state) - 1):
            e += self.distance_matrix[self.floor(self.state[i])][self.floor(self.state[i + 1])]
        return e

# City coordinates
cities = {
    0: (54, 87), 1: (21, 84), 2: (69, 84), 3: (53, 40), 4: (54, 42), 5: (36, 30), 
    6: (52, 82), 7: (93, 44), 8: (21, 78), 9: (68, 14), 10: (51, 28), 11: (44, 79), 
    12: (56, 58), 13: (72, 43), 14: (6, 99)
}

# Create a distance matrix
distance_matrix = []
for i in range(len(cities)):
    distances = []
    for j in range(len(cities)):
        dist = euclidean_distance(*cities[i], *cities[j])
        distances.append(dist)
    distance_matrix.append(distances)

# Starting tour: start at the depot, visit every city once, and return to the depot
initial_tour = list(cities.keys()) + [0]

# Set up the TSP solver
solver = TSPSolver(initial_tour)
solver.distance_matrix = distance_matrix

# Set hyperparameters for the annealer
solver.steps = 100000
solver.Tmax = 25000.0
solver.Tmin = 2.5

# Solve the problem
best_tour, best_cost = solver.anneal()

# Output results
print("Tour:", best_tour)
print("Total travel cost:", best_cost)