import math
import random

# City coordinates
cities = {
    0: (79, 15),   # Depot
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

# City groups
city_groups = [
    [1, 4],
    [2, 6],
    [7],
    [5],
    [9],
    [8],
    [3]
]

# Function to calculate Euclidean distance
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Function to calculate total travel cost of the tour
def total_cost(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Generate all possible tours by picking one city from each group
def generate_possible_tours(groups, start_city):
    if not groups:
        return [[start_city]]
    first, *rest = groups
    tours = []
    for city in first:
        for sub_tour in generate_possible_tours(rest, start_city):
            tours.append([city] + sub_tour)
    return tours

# Finding the best tour
def find_best_tour():
    possible_tours = generate_possible_tours(city_groups, 0)
    best_tour = None
    best_cost = float('inf')
    
    for tour in possible_tours:
        full_tour = [0] + tour + [0]  # round trip including the depot
        cost = total_cost(full_tour)
        if cost < best_cost:
            best_cost = cost
            best_tour = full_tour
    
    return best_tour, best_cost

# Execute the function to find the best tour
tour, total_travel_cost = find_best_tour()

# Output results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_travel(err)}