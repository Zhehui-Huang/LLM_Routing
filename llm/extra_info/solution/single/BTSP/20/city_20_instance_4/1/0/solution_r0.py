import math

# City coordinates indexed by their indices
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10), 
    5: (69, 22), 6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29),
    10: (29, 26), 11: (85, 68), 12: (60, 1), 13: (71, 73), 14: (82, 47), 
    15: (19, 25), 16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
}

def euclidean_distance(city1, city2):
    """ Calculate the Euclidean distance between two cities by their indices """
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def find_tour():
    """ Find a tour using a nearest neighbor heuristic starting from the depot city """
    unvisited = list(cities.keys())[1:]  # all cities except the depot
    tour = [0]  # start at the depot
    current_city = 0
    
    while unvisited:
        next_city = min(unvisited, key=lambda city: euclidean_distance(current_city, city))
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city
    
    tour.append(0)  # return to the depot
    return tour

def evaluate_tour(tour):
    """ Calculate total travel cost and maximum distance between consecutive cities """
    total_cost = 0
    max_distance = 0
    
    for i in range(len(tour) - 1):
        distance = euclidean_distance(tour[i], tour[i+1])
        total_cost += distance
        if distance > max_distance:
            max_distance = distance
    
    return total_cost, max_distance

# Generate a tour and evaluate it
tour = find_tour()
total_cost, max_distance = evaluate_tour(tour)

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")