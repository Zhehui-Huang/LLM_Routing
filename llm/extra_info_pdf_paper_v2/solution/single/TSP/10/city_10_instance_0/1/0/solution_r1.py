import math

# City coordinates as provided
cities = [
    (50, 42),  # Depot: City 0
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
    """ Calculate the Euclidean distance between two nodes """
    return math.sqrt((b[0] - a[0])**2 + (b[1] - a[1])**2)

def total_tour_cost(tour, city_list):
    """ Calculate the total cost of a given tour """
    cost = 0
    for i in range(len(tour) - 1):
        cost += euclidean_distance(city_list[tour[i]], city_list[tour[i+1]])
    return cost

def nearest_neighbor():
    """ Create an initial tour using the nearest neighbor algorithm """
    remaining_cities = list(range(1, len(cities)))  # Exclude the depot city initially
    tour = [0]  # Start from the depot
    current_city = 0
    
    while remaining_cities:
        next_city = min(remaining_cities, key=lambda city: euclidean_distance(cities[current_city], cities[city]))
        tour.append(next_city)
        remaining_cities.remove(next_city)
        current_city = next_city

    tour.append(0)  # Return to the depot to complete the tour
    return tour

def two_opt(tour):
    """ Optimize the tour using the 2-opt strategy to minimize distance """
    tour_improved = True
    while tour_improved:
        tour_improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour)):
                if j - i == 1: continue  # Skip adjacent edges (no benefit in swapping)
                new_tour = tour[:i] + tour[i:j+1][::-1] + tour[j+1:]
                if total_tour_cost(new_tour, cities) < total_tour_cost(tour, cities):
                    tour = new_tour
                    tour_improved = True
    return tour

# Generate and optimize the tour
initial_tour = nearest_neighbor()
optimized_tour = two_opt(initial_tour)
tour_cost = total_tour_cost(optimized_tour, cities)

# Output results
print("Tour:", optimized_tour)
print("Total travel cost:", round(tour_cost, 2))