import random
import math
import itertools

# City coordinates
cities = {
    0: (14, 77), 1: (34, 20), 2: (19, 38), 3: (14, 91), 4: (68, 98),
    5: (45, 84), 6: (4, 56), 7: (54, 82), 8: (37, 28), 9: (27, 45),
    10: (90, 85), 11: (98, 76), 12: (6, 19), 13: (26, 29), 14: (21, 79),
    15: (49, 23), 16: (78, 76), 17: (68, 45), 18: (50, 28), 19: (69, 9)
}

# Parameters for GVNS
k = 7
pmax = 2
itermax = 100

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

def total_distance(tour):
    total_dist = 0
    for i in range(len(tour) - 1):
        total_dist += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    return total_dist

def generate_initial_solution():
    tour = [0]
    available_cities = list(cities.keys())
    available_cities.remove(0)
    while len(tour) < k:
        next_city = random.choice(available_cities)
        tour.append(next_city)
        available_cities.remove(next_city)
    tour.append(0)
    return tour

def shake(tour, p):
    if p == 1:
        # Random replacement
        tour = tour[:-1]  # Remove last zero for ease
        i = random.randint(1, len(tour) - 2)
        available_cities = list(set(cities.keys()) - set(tour))
        new_city = random.choice(available_cities)
        tour[i] = new_city
        tour.append(0)
    elif p == 2:
        # Random swap
        i, j = random.sample(range(1, len(tour) - 1), 2)
        tour[i], tour[j] = tour[j], tour[i]
    return tour

def local_search(tour, p):
    if p == 1:
        for i in range(1, len(tour) - 1):
            for new_city in set(cities.keys()) - set(tour):
                new_tour = tour[:-1]
                new_tour[i] = new_city
                new_tour.append(0)
                if total_distance(new_tour) < total_distance(tour):
                    return new_tour
    elif p == 2:
        for i, j in itertools.combinations(range(1, len(tour) - 1), 2):
            new_tour = tour[:]
            new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
            if total_distance(new_tour) < total_distance(tour):
                return new_tour
    return tour

def vnd(solution):
    p = 1
    while p <= pmax:
        new_solution = local_search(solution, p)
        if total_distance(new_solution) < total_distance(solution):
            solution = new_solution
            p = 1
        else:
            p += 1
    return solution

def gvns():
    best_solution = generate_initial_solution()
    for _ in range(itermax):
        p = 1
        while p <= pmax:
            new_solution = shake(best_solution, p)
            improved_solution = vnd(new_solution)
            if total_distance(improved_solution) < total_temperature(best_solution):
                best_solution = improved_solution
                p = 1
            else:
                p += 1
    return best_solution, total_distance(best_solution)

# Run the algorithm
best_tour, best_cost = gvns()

print("Tour:", best_tour)
print("Total travel cost:", best_cost)