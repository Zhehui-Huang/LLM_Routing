import math
import random

# City coordinates
cities = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61), 
    (40, 57), (57, 30), (36, 12), (93, 43), (17, 36), 
    (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)
]

# Function to compute Euclidean distance
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Generates initial random tour
def generate_initial_solution():
    S = [0]  # Start at depot
    while len(S) < 6:
        new_city = random.choice([city for city in range(1, 15) if city not in S])
        S.append(new_city)
    S.append(0)  # End at depot
    return S

# Function to calculate the total cost of a tour
def tour_cost(tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += distance(tour[i], tour[i + 1])
    return cost

# Shaking the solution
def shake(S):
    middle_part = S[1:-1]
    random.shuffle(middle_part)
    return [S[0]] + middle_part + [S[-1]]

# Local search improvement using two different neighborhood structures
def local_search(S):
    for i in range(1, len(S)-2):
        for j in range(i+1, len(S)-1):
            new_S = S[:i] + [S[j]] + S[i+1:j] + [S[i]] + S[j+1:]
            if tour_cost(new_S) < tour_cost(S):
                S = new_S
    return S

# Implementing the Variable Neighborhood Search
def gvns(S, max_iters=100, k_max=3):
    best_S = S
    best_cost = tour_cost(S)
    for _ in range(max_iters):
        k = 1
        while k <= k_max:
            Shaken_S = shake(best_S)
            S_new = local_search(Shaken_S)
            New_cost = tour_cost(S_new)
            if New_cost < best_cost:
                best_S = S_new
                best_cost = New_cost
                k = 1
            else:
                k += 1
    return best_S, best_cost

# Initialize and run the algorithm
initial_S = generate_initial_solution()
best_tour, min_cost = gvns(initial_S)

# Display the best tour and the minimum cost
print("Tour:", best_tour)
print("Total travel cost:", round(min_cost, 2))