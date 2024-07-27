import math
import random

# Define city coordinates
cities = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98),
    (45, 84), (4, 56), (54, 82), (37, 28), (27, 45),
    (90, 85), (98, 76), (6, 19), (26, 29), (21, 79),
    (49, 23), (78, 76), (68, 45), (50, 28), (69, 9)
]

def euclidean_distance(a, b):
    return math.sqrt((cities[a][0] - cities[b][0]) ** 2 + (cities[a][1] - cities[b][1]) ** 2)

def calculate_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(tour[i], tour[i + 1])
    return total_cost

def initial_tour():
    tour = list(range(1, len(cities)))  # excluding the depot city for the shuffle
    random.shuffle(tour)
    return [0] + tour + [0]  # adding the depot city as the start and end of the tour

def lin_kernighan(tour):
    best_gain = 0
    best_tour = tour[:]
    improvement = True
    
    while improvement:
        improvement = False
        # Try improving tour by reversing segments
        for start in range(1, len(tour) - 2):
            for end in range(start + 2, len(tour) - 1):
                new_tour = tour[:start] + tour[start:end][::-1] + tour[end:]
                new_cost = calculate_cost(new_tour)
                if new_cost < calculate_cost(best_tour):
                    best_tour = new_tour[:]
                    best_gain = new_cost
                    improvement = True
                    
    return best_tour

def find_shortest_tour():
    initial = initial_tour()
    optimized_tour = lin_kernighan(initial)
    total_cost = calculate_cost(optimized_tour)
    
    return optimized_tour, total_cost

# Execute the main function
tour, cost = find_shortest_tour()
print("Tour:", tour)
print("Total travel cost:", cost)