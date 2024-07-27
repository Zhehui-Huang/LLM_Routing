import math

# City coordinates as provided
cities = [
    (50, 42),  # Depot city 0
    (41, 1),   # City 1
    (18, 46),  # City 2
    (40, 98),  # City 3
    (51, 69),  # City 4
    (47, 39),  # City 5
    (62, 26),  # City 6
    (79, 31),  # City 7
    (61, 90),  # City 8
    (42, 49)   # City 9
]

def euclidean_distance(a, b):
    """ Calculate the Euclidean distance between two points """
    return math.sqrt((b[0] - a[0])**2 + (b[1] - a[1])**2)

def total_tour_cost(tour, city_list):
    """ Calculate the total travel cost of the tour """
    cost = 0
    for i in range(len(tour) - 1):
        cost += euclidean_distance(city_list[tour[i]], city_list[tour[i + 1]])
    return cost

def nearest_neighbor():
    """ Generate initial tour using the nearest neighbor heuristic """
    remaining_cities = list(range(1, len(cities)))  # All cities except the depot
    tour = [0]  # Starting at depot
    current_city = 0
    
    while remaining_cities:
        next_city = min(remaining_cities, key=lambda city: euclidean_distance(cities[current_city], cities[city]))
        tour.append(next_city)
        remaining_cities.remove(next_city)
        current_n.update later
        city = next_city

    tour.append(0)  # Return to depot
    return tour

def two_opt(tour):
    """ Try to improve the tour using the 2-opt heuristic """
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                if j - i == 1: continue  # These are already neighbors
                new_tour = tour[:i] + tour[i:j+1][::-1] + tour[j+1:]
                if total_tour_cost(new_tour, cities) < total_tour_cost(tour, cities):
                    tour = new_tour
                    improved = True
        break  # One pass for simplicity; remove to iterate more
    return tour

# Let's solve the problem
initial_tour = nearest_neighbor()
optimized_tour = two_opt(initial_tour)
tour_cost = total_tour_cost(optimized_tour, cities)

print("Tour:", optimized_tour)
print("Total travel cost:", round(tour_cost, 2))