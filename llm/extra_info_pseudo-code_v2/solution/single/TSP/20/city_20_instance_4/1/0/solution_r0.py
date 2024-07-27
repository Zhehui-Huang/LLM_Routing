import math
import random

# Define the cities coordinates
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10),
    5: (69, 22), 6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29),
    10: (29, 26), 11: (85, 68), 12: (60, 1), 13: (71, 73), 14: (82, 47),
    15: (19, 25), 16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
}

def euclidean_distance(city1, city2):
    """ Calculate the Euclidean distance between two cities """
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

def create_initial_tour():
    """ Create an initial feasible tour using nearest neighbor heuristic """
    unvisited = list(cities.keys())[1:]  # exclude the depot city
    tour = [0]
    current_city = 0
    
    while unvisited:
        next_city = min(unvisited, key=lambda city: euclidean_distance(current_city, city))
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city

    tour.append(0)  # return to the depot city
    return tour

def calculate_tour_cost(tour):
    """ Calculate the total travel cost of the tour """
    return sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

def two_opt_swap(tour, i, k):
    """ Perform two-opt swap by reversing the tour segment between i and k """
    new_tour = tour[:i] + tour[i:k+1][::-1] + tour[k+1:]
    return new_tour

def apply_two_opt(tour):
    """ Apply two-opt heuristic to improve the initial tour """
    improvement = True
    while improvement:
        improvement = False
        best_cost = calculate_tour_cost(tour)
        for i in range(1, len(tour) - 2):
            for k in range(i + 1, len(tour) - 1):
                new_tour = two_opt_swap(tour, i, k)
                new_cost = calculate_tour_cost(new_tour)
                if new_cost < best/cost:
                    tour = new_tour
                    best_cost = new_cost
                    improvement = True
                    
    return tour

# Main execution
initial_tour = create_initial_tour()
tour = apply_two_opt(initial_tour)
tour_cost = calculate_tour_cost(tour)

# Output the tour and total travel cost
print("Tour:", tour)
print("Total travel cost:", tour_cost)