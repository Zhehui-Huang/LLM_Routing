import math
from itertools import permutations, combinations

def calculate_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def main():
    # Coordinates of the cities
    cities = [
        (79, 15),  # Depot city 0
        (79, 55),  # City 1
        (4, 80),   # City 2
        (65, 26),  # City 3
        (92, 9),   # City 4
        (83, 61),  # City 5
        (22, 21),  # City 6
        (97, 70),  # City 7
        (20, 99),  # City 8
        (66, 62)   # City 9
    ]
    
    # Generate all combinations of 7 cities to visit in addition to the depot city
    city_indices = list(range(1, 10))
    city_combinations = combinations(city_indices, 7)
    
    min_cost = float('inf')
    best_tour = []
    
    for comb in city_combinations:
        # Make sure the tour includes the depot city by adding it to the combination
        cities_to_visit = (0,) + comb
        
        # Permute the selected cities to find the shortest tour
        for perm in permutations(cities_to_visit):
            # Start and end at depot
            if perm[0] == 0 and perm[-1] == 0:
                total_cost = sum(calculate_distance(cities[perm[i]], cities[perm[i+1]]) for i in range(len(perm)-1))
                
                # Check if this permutation is better
                if total_cost < min_cost:
                    min_cost = total_cost
                    best_tour = list(perm)
    
    # Display results
    print("Tour:", best_tour)
    print("Total travel cost:", min_cost)

if __name__ == "__main__":
    main()