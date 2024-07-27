import random
import numpy as np
import math

# Given city coordinates
cities = {
    0: (54, 87),
    1: (21, 84),
    2: (69, 84),
    3: (53, 40),
    4: (54, 42),
    5: (36, 30),
    6: (52, 82),
    7: (93, 44),
    8: (21, 78),
    9: (68, 14),
    10: (51, 28),
    11: (44, 79),
    12: (56, 58),
    13: (72, 43),
    14: (6, 99)
}

def euclidean_distance(a, b):
    return math.sqrt((cities[a][0] - cities[b][0])**2 + (cities[a][1] - cities[b][1])**2)

def total_tour_cost(tour):
    return sum(euclidean_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

def generate_initial_solution(k):
    tour = [0]
    available_cities = list(cities.keys())
    available_cities.remove(0)
    while len(tour) < k:
        next_city = random.choice(available_cities)
        tour.append(next_city)
        available_cities.remove(next_city)
    tour.append(0)  # Return to depot
    return tour

def shake(S, k):
    S_ = S[1:-1]  # Do not include the depot in the shake
    random.shuffle(S_)
    return [S[0]] + S_ + [S[0]]

def local_search(S, Np):
    if Np == "N1":  # Exchange
        for i in range(1, len(S)-1):
            for city in cities:
                if city not in S:
                    new_tour = S[:]
                    new_tour[i] = city
                    if total_tour_cost(new_tour) < total_tour_cost(S):
                        return new_tour
        return S
    elif Np == "N2":  # Swap
        for i in range(1, len(S)-2):
            for j in range(i + 1, len(S)-1):
                new_tour = S[:]
                new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
                if total_tour_cost(new_tour) < total_tour_cost(S):
                    return new_tour
        return S

def vnd(S):
    neighborhoods = ["N1", "N2"]
    improvement = True
    while improvement:
        improvement = False
        for Np in neighborhoods:
            new_S = local_search(S, Np)
            if total_tour_cost(new_S) < total_tour_cost(S):
                S = new_S
                improvement = True
                break
    return S

def gvns(k):
    itermax = 100
    pmax = 2
    S = generate_initial_solution(k)
    best_cost = total_tour_cost(S)
    best_solution = S[:]
    
    for iter in range(itermax):
        for p in range(pmax):
            S_prime = shake(S, p + 1)
            S_double_prime = vnd(S_prime)
            if total_tour_cost(S_double_prime) < best_cost:
                S = S_double_prime
                best_cost = total_tour_cost(S_double_prime)
                best_solution = S_double_prime
    
    return best_solution, best_cost

# Number of cities in the tour including the depot one.
k = 8
best_tour, best_cost = gvns(k)
print("Tour:", best_tour)
print("Total travel cost:", best_cost)