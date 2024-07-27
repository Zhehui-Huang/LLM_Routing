import math

# Defining the cities and their coordinates
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10), 
    5: (69, 22), 6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29),
    10: (29, 26), 11: (85, 68), 12: (60, 1), 13: (71, 73), 14: (82, 47),
    15: (19, 25), 16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
}

# Grouping the cities
city_groups = [
    [5, 6, 16], [8, 18, 19], [11, 12, 13], [1, 3, 9],
    [2, 4, 14], [10, 17], [7, 15]
]

# Helper function to compute Euclidean distance
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Initial tour selection by nearest city in each group to the depot
def initial_tour(depot):
    tour = [depot]
    for group in city_groups:
        min_dist = math.inf
        chosen_city = None
        for city in group:
            dist = distance(depot, city)
            if dist < min_dist:
                min_dist = dist
                chosen_city = city
        tour.append(chosen_city)
    tour.append(depot)  # Complete the tour by returning to the depot
    return tour

# Calculate the total distance of the tour
def tour_cost(tour):
    total_cost = 0
    for i in range(len(tour)-1):
        total_cost += distance(tour[i], tour[i + 1])
    return total_cost

# Generate the initial tour and calculate its cost
initial_tour = initial_tour(0)
initial_cost = tour_cost(initial_tour)

# Output the results
print(f"Tour: {initial_tour}")
print(f"Total travel cost: {initial_cost:.2f}")