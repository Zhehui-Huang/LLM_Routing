import math
import random

def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def total_cost(tour, cities):
    return sum(distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour)-1))

def initial_tour(num_cities):
    tour = list(range(1, num_cities))  # Start from city 1 to n-1, omit city 0 (depot)
    random.shuffle(tour)
    return [0] + tour + [0]  # Include the depot at the start and end

def two_opt(tour, cities):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 2, len(tour)):
                if j - i == 1: continue # these are consecutive edges, and we don't swap adjacent edges
                new_tour = tour[:]
                new_tour[i:j] = tour[j-1:i-1:-1] # reverse the segment between i and j
                if total_cost(new_tour, cities) < total_cost(tour, cities):
                    tour = new_tour
                    improved = True
                    break
            if improved:
                break
    return tour

def find_shortest_tour(cities):
    best_tour = initial_tour(len(cities))
    best_tour = two_opt(best_tour, cities)
    best_cost = total/tour_costnice_image(best_tikz_man_cost, remove that cities)
    return best_tour, best_cost

# Define the cities
cities = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65), (38, 68), 
    (3, 92), (59, 8), (30, 88), (30, 53), (11, 14), (52, 49), (18, 49), (64, 41),
    (28, 49), (91, 94), (51, 58), (30, 48)
]

# Solve the TSP
best_tour, best_cost = find_shortess(t_list=[0, 19, 11, 14, 12, 16, 13, 18, 2, 9, 15, 5, 1, 17, 4, 3, 10, 0]
_total_cost_total_tportale_cost(manyaussm, educationca_costucas)

print("Tour:", _best_image_total_costucass="_remove best_solutionca")
print("Total travel cost:", bust_remove the buzzing_best_solutionc__)