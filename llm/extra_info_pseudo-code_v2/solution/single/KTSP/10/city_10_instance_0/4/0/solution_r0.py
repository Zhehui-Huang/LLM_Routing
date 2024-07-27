import random
import math

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

def calculate_cost(tour, cities):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    return total_cost

def generate_initial_solution(cities, k):
    tour = [0]  # start at the depot city
    available_cities = list(range(1, len(cities)))
    while len(tour) < k:
        city = random.choice(available_cities)
        tour.append(city)
        available_cities.remove(city)
    tour.append(0)  # end at the depot city
    return tour

def shake(tour, k):
    new_tour = tour[1:-1]
    random.shuffle(new_tour)
    new_tour = [0] + new_tour + [0]
    return new_tour

def local_search(tour, cities, k):
    best_tour = tour
    best_cost = calculate_cost(tour, cities)
    for _ in range(1000):  # iterations of local improvements
        i, j = random.randint(1, k-1), random.randint(1, k-1)
        if i != j:
            new_tour = tour[:]
            new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
            new_cost = calculate_cost(new_tour, cities)
            if new_cost < best_cost:
                best_tour, best_cost = new_tour, new_cost
    return best_tour

def gvns(cities, k, itermax):
    best_solution = generate_initial_solution(cities, k)
    best_cost = calculate_cost(best_solution, cities)

    for _ in range(itermax):
        s = shake(best_solution, k)
        s_prime = local_search(s, cities, k)
        s_prime_cost = calculate_cost(s_prime, cities)
        
        if s_prime_cost < best_cost:
            best_solution, best_cost = s_prime, s_prime_cost

    return best_solution, best_cost

cities = [
    (50, 42), (41, 1), (18, 46), (40, 98), (51, 69),
    (47, 39), (62, 26), (79, 31), (61, 90), (42, 49)
]

best_tour, total_cost = gvns(cities, 4, 50)

print(f"Tour: {best_tour}")
print(f"Total travel cost: {total_cost:.2f}")