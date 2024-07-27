import math
import random

# City coordinates
cities = [
    (29, 51),  # Depot city 0
    (49, 20),
    (79, 69),
    (17, 20),
    (18, 61),
    (40, 57),
    (57, 30),
    (36, 12),
    (93, 43),
    (17, 36),
    (4, 60),
    (78, 82),
    (83, 96),
    (60, 50),
    (98, 1)
]

# Parameters
k = 6  # Number of cities in the tour including the depot
iter_max = 1000
p_max = 3

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def total_distance(tour):
    return sum(euclidean_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour)-1))

def generate_initial_solution():
    tour = [0]  # Start at the depot city
    selected_cities = set(tour)
    while len(tour) < k:
        remaining_cities = [c for c in range(1, len(cities)) if c not in selected_cities]
        city = random.choice(remaining_cities)
        best_cost = float('inf')
        best_position = 1
        # Insert city at the best position
        for position in range(1, len(tour) + 1):
            new_tour = tour[:position] + [city] + tour[position:]
            cost = total_distance(new_tour + [new_tour[0]])  # Close loop
            if cost < best_cost:
                best_cost = cost
                best_position = position
        tour.insert(best_position, city)
        selected_cities.add(city)
    tour.append(0)  # Return to depot
    return tour  

def shake(s, p):
    # Shuffling cities inside the tour, except the depot (first and last elements)
    s_prime = s[1:-1]
    if p == 1:
        random.shuffle(s_prime)
    elif p == 2:
        if len(s_prime) > 1:
            i, j = random.sample(range(len(s_prime)), 2)
            s_prime[i], s_prime[j] = s_prime[j], s_prime[i]
    return [0] + s_prime + [0]

def local_search(s, p):
    improved = True
    if p == 1:
        # Exchange with unvisited city
        for i in range(1, len(s) - 1):
            for j in range(1, len(cities)):
                if j not in s:
                    new_s = s[:i] + [j] + s[i+1:]
                    new_s[-1] = new_s[0]  # ensure return to start
                    if total_distance(new_s) < total_distance(s):
                        return new_s
        improved = False
    elif p == 2:
        # Swap positions
        for i in range(1, len(s) - 2):
            for j in range(i + 1, len(s) - 1):
                s[i], s[j] = s[j], s[i]
                if total_distance(s) < total_distance(s):
                    return s
                s[i], s[j] = s[j], s[i]
        improved = False
    return s if improved else None

def vnd(s):
    p = 1
    while p <= p_max:
        new_s = local_search(s, p)
        if new_s:
            s = new_s
            p = 1
        else:
            p += 1
    return s

def gvns():
    best_solution = generate_initial_solution()
    best_cost = total_distance(best_solution)
    iter = 1
    while iter <= iter_max:
        s = best_solution
        p = 1
        while p <= p_max:
            s_prime = shake(s, p)
            s_double_prime = vnd(s_prime)
            cost = total_distance(s_double_prime)
            if cost < best_cost:
                best_solution = s_double_prime
                best_cost = cost
                p = 1
            else:
                p += 1
        iter += 1
    return best_solution, best_cost

# Execute the algorithm
tour, cost = gvns()
print("Tour:", tour)
print("Total travel cost:", cost)