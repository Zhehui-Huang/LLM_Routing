import math
import random

# City coordinates
cities = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57), 5: (6, 58),
    6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0), 10: (61, 25),
    11: (52, 0), 12: (60, 95), 13: (10, 94), 14: (96, 73), 15: (14, 47),
    16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

def euclidean_distance(city1, city2):
    """ Calculate Euclidean distance between two cities """
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

def initial_tour():
    """ Generate a simple initial tour """
    included = set([0])
    tour = [0]
    last_city = 0
    while len(tour) < 13:
        next_city = min((city for city in cities if city not in included), key=lambda city: euclidean_distance(last_city, city))
        tour.append(next_city)
        included.add(next_city)
        last_city = next_city
    tour.append(0)
    return tour

def tour_cost(tour):
    """ Calculate the cost of the tour """
    return sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

def local_search(tour):
    """ Apply local search based on the swapping of nodes and two-opt """
    improvement = True
    while improvement:
        improvement = False
        for i in range(1, len(tour) - 2):
            for j in range(i+1, len(tour) - 1):
                if j - i == 1: continue  # Skip adjacent pairs
                new_tour = tour[:i] + tour[i:j+1][::-1] + tour[j+1:]
                if tour_cost(new_tour) < tour_cost(tour):
                    tour = new_tour
                    improvement = True
        random.shuffle(tour[1:-1])  # Shuffle internal nodes to escape local optima
    return tour

# Generate initial solution
initial = initial_tour()

# Perform local search
optimized_tour = local_tour_search(initial)

# Compute cost
cost = tour_cost(optimized_tour)

# Output result
print("Tour:", optimized_tour)
print("Total travel cost:", cost)