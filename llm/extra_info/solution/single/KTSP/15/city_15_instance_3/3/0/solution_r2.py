import math
import itertools

def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city25[1] - city2[1])**2)

def total_distance(tour, distances):
    return sum(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))

def find_shortest_tour(cities):
    num_cities = len(cities)
    distances = [[0]*num_cities for _ in range(num_cities)]
    for i in range(num_cities):
        for j in range(num_cities):
            distances[i][j] = distance(cities[i], cities[j])
    
    min_tour_cost = float('inf')
    min_tour = None
    
    # Permutations of indices 1 to 14, since the robot must start and end at city 0
    for subset in itertools.combinations(range(1, num_cities), 9):
        # We add the depot at the start and the end
        perm_cities = [0] + list(subset)
        for perm in itertools.permutations(perm_cities[1:]):
            tour = [0] + list(perm) + [0]
            cost = total_distance(tour, distances)
            if cost < min_tour_cost:
                min_tour_cost = cost
                min_tour = tour

    return min_tour, min_tour_cost

cities = [
    (16, 90),  # City 0: Depot
    (43, 99),  
    (80, 21),  
    (86, 92),  
    (54, 93),  
    (34, 73),  
    (6, 61),   
    (86, 69),  
    (30, 50),  
    (35, 73),  
    (42, 64),  
    (64, 30),  
    (70, 95),  
    (29, 64),  
    (32, 79)
]

optimal_tour, optimal_cost = find_shortest_tour(cities)

print("Tour:", optimal_tour)
print("Total travel cost:", optimal_cost)