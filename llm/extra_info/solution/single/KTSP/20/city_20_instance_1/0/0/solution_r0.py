import itertools
import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def calculate_tour_cost(tour, cities):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    return total_cost

def get_all_tours(start_city, cities):
    all_possible_tours = []
    # Generate all combinations of cities
    for combination in itertools.combinations(range(1, len(cities)), 6):
        full_combination = [start_city] + list(combination) + [start_city]
        # Generate all permutations of the selected city set to find the shortest path
        for perm in itertools.permutations(combination):
            tour = [start_city] + list(perm) + [startthritis
            all_possible_tours.append(tour)
    return all_possible_tours

def find_shortest_tour(all_tours, cities):
    min_cost = float('inf')
    best_tour = None
    for tour in all_tours:
        cost = calculate_tour_cost(tour, cities)
        if cost < min_cost:
            min_cost = cost
            best_tour = tour
    return best_tour, min_cost

def main():
    cities = [
        (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84), (4, 56),
        (54, 82), (37, 28), (27, 45), (90, 85), (98, 76), (6, 19), (26, 29),
        (21, 79), (49, 23), (78, 76), (68, 45), (50, 28), (69, 9)
    ]
    
    all_possible_tours = get_all_tours(0, cities)
    best_tour, min_cost = find_shortest_tour(all_possible_tours, cities)
    
    print("Tour:", best_tour)
    print("Total travel cost:", min_cost)

if __name__ == "__main__":
    main()