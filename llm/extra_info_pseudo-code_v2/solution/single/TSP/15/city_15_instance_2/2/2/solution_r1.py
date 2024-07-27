import math

# Cities coordinates with the depot city as the first entry
city_coords = [(54, 87), (21, 84), (69, 84), (53, 40), (54, 42), (36, 30), 
               (52, 82), (93, 44), (21, 78), (68, 14), (51, 28), 
               (44, 79), (56, 58), (72, 43), (6, 99)]

def euclidean_distance(city1, city2):
    """Calculate the Euclidean distance between two cities."""
    x1, y1 = city_coords[city1]
    x2, y2 = city_coords[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def nearest_neighbor_tour():
    """Generate an initial tour using the nearest neighbor heuristic."""
    unvisited_cities = list(range(1, len(city_coords)))  # skipping depot city
    tour = [0]  # start from the depot
    current_city = 0

    while unvisited_cities:
        next_city = min(unvisited_cities, key=lambda city: euclidean_distance(current_city, city))
        tour.append(next_city)
        unvisited_cities.remove(next_city)
        current_city = next_city
    
    tour.append(0)  # return to the depot
    return tour

def compute_tour_cost(tour):
    """Compute the total cost of a given tour."""
    total_cost = sum(euclidean_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
    return total_cost

# Generate an initial tour using the nearest neighbor strategy and compute its cost
initial_tour = nearest_neighbor_tour()
initial_cost = compute_tour_cost(initial_tour)

# Produce the necessary outputs
print("Tour:", initial_tour)
print("Total travel cost:", initial_cost)