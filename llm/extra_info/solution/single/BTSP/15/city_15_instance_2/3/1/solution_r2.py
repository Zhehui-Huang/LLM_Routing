import math
import random

# Coordinates of each city, including the depot
cities = [
    (54, 87), (21, 84), (69, 84), (53, 40), (54, 42),
    (36, 30), (52, 82), (93, 44), (21, 78), (68, 14),
    (51, 28), (44, 79), (56, 58), (72, 43), (6, 99)
]

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Calculate all pairwise distances between cities for easy access
distance_matrix = [[distance(cities[i], cities[j]) for j in range(len(cities))] for i in range(len(cities))]

# Genetic algorithm components
def create_route():
    route = list(range(1, len(cities)))
    random.shuffle(route)
    route = [0] + route + [0]
    return route

def create_initial_population(size):
    return [create_route() for _ in range(size)]

def route_distance(route):
    return sum(distance_matrix[route[i]][route[i+1]] for i in range(len(route)-1))

def route_max_distance(route):
    return max(distance_matrix[route[i]][route[i+1]] for i in range(len(route)-1))

def selection(population, scores, k=3):
    selection_ix = random.randint(0, len(population)-1)
    for ix in random.sample(range(len(population)), k-1):
        if scores[ix] < scores[selection_ix]:
            selection_ix = ix
    return population[selection_ix]

def crossover(p1, p2, r_cross):
    if random.random() < r_cross:
        pt = random.randint(1, len(p1)-3)
        child = [None]*len(p1)
        child[1:pt] = p1[1:pt]
        available = set(p2[1:-1]) - set(p1[1:pt])
        cursor = pt
        for city in p2:
            if city in available:
                child[cursor] = city
                cursor += 1
        child[0], child[-1] = 0, 0
        return [child]
    return [p1, p2]

def mutation(route, r_mut):
    if random.random() < r_mut:
        i, j = random.randint(1, len(route)-2), random.randint(1, len(route)-2)
        route[i], route[j] = route[j], route[i]

# Genetic algorithm
def genetic_algorithm(n_iter, pop_size, r_cross, r_mut):
    pop = create_initial_population(pop_size)
    best, best_eval = min((route, route_max_distance(route)) for route in pop), float('inf')
    for gen in range(n_iter):
        scores = [route_max_distance(route) for route in pop]
        ranked = sorted(zip(pop, scores), key=lambda x: x[1])
        top_performers = [x[0] for x in ranked[:10]]
        best, best_eval = ranked[0]
        print(f"Generation {gen+1}, Best Distance: {best_eval}")
        selected = [selection(pop, scores) for _ in range(pop_size - 10)]
        children = list()
        for i in range(0, len(selected), 2):
            p1, p2 = selected[i], selected[i+1]
            for c in crossover(p1, p2, r_cross):
                mutation(c, r_mut)
                children.append(c)
        pop = top_performers + children
    return best, best_eval

# Parameters
n_iter = 100
pop_size = 100
r_cross = 0.9
r_mut = 0.02

best_route, best_score = genetic_algorithm(n_iter, pop_size, r_cross, r_mut)
total_cost = route_distance(best_route)

# Results
print("Tour:", best_route)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", best_score)