import random
import math
from itertools import permutations

# Define the city coordinates in a dict
cities = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

# Function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# General Variable Neighborhood Search (GVNS) Algorithm
def GVNS(k=7, itermax=1000, pmax=4):
    best_solution = None
    best_cost = float('inf')
    
    for _ in range(itermax):
        S = GenerateInitialSolution(k)
        p = 1
        
        while p <= pmax:
            Sp = Shake(S, p)
            Spp = VND(Sp)
            cost_spp = GetTotalTravelCost(Spp)
            
            if cost_spp < best_cost:
                best_solution = Spp
                best_cost = cost_spp
                p = 1
            else:
                p += 1
                
    return best_solution, best_cost

# Generate Initial Solution
def GenerateInitialSolution(k):
    S = [0]  # Start from the depot city
    available_cities = list(cities.keys())[1:]
    random.shuffle(available_cities)
    S += available_cities[:k-1]  # Select k-1 other cities randomly
    S.append(0)  # Return to the depot
    return S

# Shake function
def Shake(S, p):
    S_prime = S[:]
    random.shuffle(S_prime[1:-1])  # Shuffle cities except the depot
    return S_prime

# Variable Neighborhood Descent (VND)
def VND(S):
    neighborhoods = [1, 2]  # Define neighborhood structures
    for p in neighborhoods:
        improved = True
        while improved:
            S_prime = LocalSearch(S, p)
            if S_prime:
                S = S_prime
            else:
                improved = False
    return S

# Local Search function
def LocalSearch(S, p):
    if p == 1:  # N1 exchange strategy
        for i in range(1, len(S) - 1):
            for j in range(1, len(cities)):
                if j not in S:
                    S_prime = S[:i] + [j] + S[i+1:-1] + [0]
                    if GetTotalTravelCost(S_prime) < GetTotalTravelCost(S):
                        return S_prime
    elif p == 2:  # N2 swap strategy
        for i in range(1, len(S) - 2):
            for j in range(i + 1, len(S) - 1):
                S_prime = S[:]
                S_prime[i], S_prime[j] = S_prime[j], S_prime[i]
                if GetTotalTravelCost(S_prime) < GetTotalTravelCost(S):
                    return S_prime
    return None

# Get total travel cost of tour
def GetTotalTravelCost(tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += euclidean_distance(tour[i], tour[i+1])
    return cost

# Run the GVNS
best_tour, best_cost = GVNS()
print("Tour:", best_tour)
print("Total travel cost:", best_cost)