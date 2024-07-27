import numpy as np
import math
import random

# City and robot information based on provided environment
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35), (32, 39), (56, 37)
]

robots = [i for i in range(8)]

# Distance matrix calculation
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

dist_matrix = [[distance(c1, c2) for c2 in cities] for c1 in cities]

# Ant Colony Optimization Setup
num_ants = 50
max_iter = 100
decay = 0.1
alpha = 1.0
beta = 2.0

class Ant:
    def __init__(self, start):
        self.tour = [start]
        self.cost = 0.0

    def visit_city(self, city):
        last_city = self.tour[-1]
        travel_cost = dist_matrix[last_city][city]
        self.tour.append(city)
        self.cost += travel_cost

    def tour_complete(self, start_city):
        # Close the tour loop
        travel_cost = dist_matrix[self.tour[-1]][start_city]
        self.tour.append(start_city)
        self.cost += travel_cost

    def get_possible_moves(self, unvisited):
        return unvisited

# ACO Algorithm
pheromone = [[1 for _ in range(len(cities))] for _ in range(len(cities))]
def aco_tsp():
    
    best_cost = float('inf')
    best_solution = []

    for _ in range(max_iter):
        all_ants = [Ant(start=robot) for robot in robots]

        for ant in all_ants:
            unvisited = set(range(len(cities))) - set(ant.tour)
            while unvisited:
                current = ant.tour[-1]
                probabilities = []
                
                for next_city in ant.get_possible_moves(unvisited):
                    if next_city not in ant.tour:
                        pheromone_influence = pheromone[current][next_city] ** alpha
                        distance_influence = (1.0 / dist_matrix[current][next_city]) ** beta
                        probabilities.append(pheromone_influence * distance_influence)
                    else:
                        probabilities.append(0)

                probabilities = np.array(probabilities)
                probabilities /= probabilities.sum()

                next_city = np.random.choice(list(unvisited), p=probabilities)
                ant.visit_city(next_city)
                unvisited.remove(next_city)
        
        for ant in all_ants:
            ant.tour_complete(ant.tour[0])

        new_pheromone = [[0 for _ in range(len(cities))] for _ in range(len(cities))]
        contributors = 0
        for ant in all_ants:
            contributors += 1
            for i in range(1, len(ant.tour)):
                x = ant.tour[i - 1]
                y = ant.tour[i]
                new_pheromone[x][y] += 1 / ant.cost
        
        for i in range(len(cities)):
            for j in range(len(cities)):
                pheromone[i][j] = (1 - decay) * pheromone[i][j] + new_pheromone[i][j]

        current_best = min(all_ants, key=lambda ant: ant.cost)
        if current_best.cost < best_cost:
            best_cost = current_best.cost
            best_solution = current_best.tour

    return best_solution, best_cost

best_tour, best_cost = aco_tsp()

print("Optimal tour:", best_tour)
print("Best tour cost:", best_cost)