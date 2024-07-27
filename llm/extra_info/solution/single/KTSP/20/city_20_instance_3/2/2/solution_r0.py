import itertools
import random
import math

# City coordinates
cities = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57),
    5: (6, 58), 6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0),
    10: (61, 25), 11: (52, 0), 12: (60, 95), 13: (10, 94), 14: (96, 73),
    15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

def euclidean_distance(city1, city2):
    """ Calculate Euclidean distance between two cities """
    x1, y1 = city1
    x2, y2 = city2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Create a distance matrix for all pairs of cities
num_cities = len(cities)
dist_matrix = {}
for i in range(num_cities):
    for j in range(num_cities):
        if i not in dist_matrix:
            dist_matrix[i] = {}
        dist_matrix[i][j] = euclidean_distance(cities[i], cities[j])

# Function to calculate total travel cost of a tour
def tour_cost(tour):
    return sum(dist_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

# Greedy algorithm to select initial cities close to the depot
def select_initial_cities(depot, num_cities_needed):
    distances = sorted((dist_matrix[depot][i], i) for i in range(num_cities) if i != depot)
    selected_cities = [distances[i][1] for i in range(num_cities_needed - 1)]
    return [depot] + selected_cities

# Generate initial list of cities
selected_cities = select_initial_cities(0, 13)
selected_cities.append(0)  # Add depot city at the end to complete the loop

# Simple genetic algorithm to find an optimal tour from selected cities
def genetic_algorithm(population, generations, mutation_rate):
    def breed(parent1, parent2):
        """ Breeding via ordered crossover """
        cut_points = sorted(random.sample(range(1, len(parent1)-1), 2))
        middle = parent1[cut_points[0]:cut_points[1]]
        child = [city for city in parent2 if city not in middle]
        return child[:cut_points[0]] + middle + child[cut_points[0]:]

    def mutate(tour):
        """ Mutate via swapping two cities """
        if random.random() < mutation_rate:
            i, j = random.sample(range(1, len(tour)-1), 2)
            tour[i], tour[j] = tour[j], tour[i]
        return tour

    # Initialize random population
    pop = [random.sample(selected_cities, len(selected_cities)) for _ in range(population)]
    best_tour = min(pop, key=tour_cost)

    for _ in range(generations):
        new_pop = []
        scores = [(tour_cost(tour), tour) for tour in pop]
        scores.sort()
        best_tour = min(best_tour, scores[0][1], key=tour_cost)
        # Elitism: carry best solutions to next gen
        elitism_count = population // 20
        new_pop.extend([scores[i][1] for i in range(elitism_count)])

        # Breeding
        potential_parents = scores[:len(scores) // 2]
        parent_choice = [x[1] for x in potential_parents]
        for _ in range(population - elitism_count):
            parents = random.sample(parent_choice, 2)
            child = breed(parents[0], parents[1])
            child = mutate(child)
            new_pop.append(child)

        pop = new_pop

    return best_t

result = genetic_algorithm(1000, 2000, 0.03)
print("Tour:", [0] + result[1:-1])  # Include the depot city
print("Total travel cost:", tour_cost(result))