import math

# City coordinates
cities = {
    0: (29, 51), 1: (49, 20), 2: (79, 69), 3: (17, 20), 4: (18, 61), 5: (40, 57),
    6: (57, 30), 7: (36, 12), 8: (93, 43), 9: (17, 36), 10: (4, 60), 11: (78, 82),
    12: (83, 96), 13: (60, 50), 14: (98, 1)
}

# Distance calculation function
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Initial tour using nearest neighbor heuristic from the depot
def nearest_neighbor(start):
    tour = [start]
    unvisited = set(cities.keys()) - {start}

    current = start
    while unvisited:
        next_city = min(unvisited, key=lambda city: distance(current, city))
        tour.append(next_city)
        unvisited.remove(next_city)
        current = next_city

    tour.append(start)  # Return to the depot
    return tour

# Function to calculate the total distance of the tour
def tour_distance(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# 2-opt swap
def two_opt(tour):
    best = tour
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour)):
                if j - i == 1: continue  # Consecutive nodes; no meaning to swap
                new_tour = tour[:i] + tour[i:j][::-1] + tour[j:]
                if tour_distance(new_tour) < tour_distance(best):
                    best = new_tour
                    improved = True
        tour = best
    return tour

starting_city = 0
initial_tour = nearest_neighbor(starting_city)
optimized_tour = two_opt(initial_tour)
total_cost = tour_distance(optimized_tour)

print("Tour:", optimized_tour)
print("Total travel cost:", total_cost)