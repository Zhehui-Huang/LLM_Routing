import math

# City coordinates
city_positions = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90), (54, 46), 
    (8, 70), (97, 62), (14, 41), (70, 44), (27, 47), (41, 74), 
    (53, 80), (21, 21), (12, 39)
]

# Groups of cities
city_groups = [
    [3, 8], [4, 13], [1, 2], [6, 14], [5, 9], [7, 12], [10, 11]
]

def calculate_distance(city1, city2):
    """ Calculate Euclidean distance between two cities """
    x1, y1 = city_positions[city1]
    x2, y2 = city_positions[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def total_tour_cost(tour):
    """ Calculate total cost of the tour """
    cost = 0
    for i in range(len(tour) - 1):
        cost += calculate_distance(tour[i], tour[i + 1])
    return cost

def find_initial_tour():
    """ Find initial tour by selecting closest city in each group to the depot """
    tour = [0]
    for group in city_groups:
        closest_city = min(group, key=lambda city: calculate_distance(0, city))
        tour.append(closest_city)
    tour.append(0)  # returning to the depot
    return tour

def improve_tour(tour):
    """ Attempt to improve the tour by optimizing city choices within groups """
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 1):
            group_index = i - 1
            group = city_groups[group_index]
            current_city = tour[i]
            best_cost = total_tour_cost(tour)
            for city in group:
                if city != current_city:
                    new_tour = tour[:i] + [city] + tour[i + 1:]
                    new_cost = total_tour_cost(new_tour)
                    if new_cost < best_cost:
                        tour = new_tour
                        best_cost = new_cost
                        improved = True
    return tour

# Finding the initial feasible tour
initial_tour = find_initial_tour()
improved_tour = improve_tour(initial_tour)
tour_cost = total_tour_cost(improved_tour)

print("Tour:", improved_tour)
print("Total travel cost:", tour_cost)