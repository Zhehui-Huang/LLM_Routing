import random
import math

# Define the coordinates of each city, including the depot as city 0
cities = [
    (54, 87), (21, 84), (69, 84), (53, 40), (54, 42), 
    (36, 30), (52, 82), (93, 44), (21, 78), (68, 14), 
    (51, 28), (44, 79), (56, 58), (72, 43), (6, 99)
]

# Function to calculate the Euclidean distance between two cities
def euclidean_distance(index1, index2):
    return math.sqrt((cities[index1][0] - cities[index2][0])**2 + (cities[index1][1] - cities[index2][1])**2)

# Function to calculate the total travel cost of a tour
def calculate_cost(tour):
    total_cost = sum(euclidean_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
    return total_cost

# Generate an initial solution by randomly selecting k cities including the depot
def generate_initial_solution(k):
    S = [0]  # Start at the depot city
    while len(S) < k:
        new_city = random.choice([i for i in range(1, len(cities)) if i not in S])
        S.append(new_city)
    S.append(0)  # End at the depot city
    return S

# Shaking the solution within specified neighborhood size
def shake(S, k):
    city_to_replace = random.randint(1, k-2)
    city_not_in_tour = random.choice([i for i in range(1, len(cities)) if i not in S])
    new_S = S[:]
    new_S[city_to_replace] = city_not_in_tour
    return new_S

# Local search through first improvement strategy in neighborhood
def local_search(S):
    for i in range(1, len(S)-2):
        for j in range(i+1, len(S)-1):
            new_S = S[:]
            new_S[i], new_S[j] = new_S[j], new_S[i]  # Swap two cities
            if calculate_cost(new_S) < calculate_cost(S):
                return new_S
    return S

# GVNS algorithm implementation
def GVNS(k, itermax):
    S = generate_initial_solution(k)
    best_S = S
    best_cost = calculate_cost(S)
    for _ in range(itermax):
        p = 1
        while p <= 2:
            S_prime = shake(S, k)
            S_double_prime = local_search(S_prime)
            if calculate_cost(S_double_prime) < best_cost:
                best_S = S_double_prime
                best_cost = calculate_cost(S_double_poore)
                p = 1
            else:
                p += 1
        if calculate_cost(S) < best_cost:
            best_S = S
            best_cost = calculate_cost(S)
    return best_S, best_cost

# Define problem parameters
k = 8  # Including the depot (total cities in tour)
itermax = 100  # Maximum iterations

# Solve the 8-city tour problem
best_tour, best_cost = GVNS(k, itermax)

print("Tour:", best_tour)
print("Total travel cost:", best_cost)