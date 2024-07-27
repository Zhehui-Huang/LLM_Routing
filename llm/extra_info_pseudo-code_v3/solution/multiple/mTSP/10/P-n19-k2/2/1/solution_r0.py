import numpy as np
from math import sqrt

# City coordinates
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 27), (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Calculate Euclidean distance between two cities
def distance(i, j):
    return sqrt((coordinates[i][0] - coordinates[j][0])**2 + (coordinates[i][1] - coordinates[j][1])**2)

# Initial tour generation (greedy method)
def generate_initial_tours():
    cities = list(range(1, len(coordinates)))  # excluding depot
    np.random.shuffle(cities)
    mid = len(cities) // 2
    tour1 = [0] + cities[:mid] + [0]
    tour2 = [0] + cities[mid:] + [0]
    return tour1, tour2

# Function to calculate the cost of a tour
def calculate_cost(tour):
    cost = sum(distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
    return cost

# 2-opt optimization
def optimize_tour(tour):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour)):
                if j - i == 1: continue
                new_tour = tour[:i] + tour[i:j][::-1] + tour[j:]
                if calculate_cost(new_tour) < calculate_cost(tour):
                    tour = new_tour
                    improved = True
                    break
            if improved:
                break
    return tour

# Main execution block
tour1, tour2 = generate_initial_tours()
tour1 = optimize_tour(tour1)
tour2 = optimize_tour(tour2)

cost1 = calculate_cost(tour1)
cost2 = calculate_cost(tour2)
overall_cost = cost1 + cost2

# Output results
print("Robot 0 Tour:", tour1)
print("Robot 0 Total Travel Cost:", cost1)
print("\nRobot 1 Tour:", tour2)
print("ARobot 1 otal Travel Cost:", cost2)
print("\nOverall oAd  ProfenE g Tsas.K M Nas:iTe rsa.4", ew.strategy for MarB4.")
print("\n,fMlt raMaed) RLGu hodor OWUtl '}