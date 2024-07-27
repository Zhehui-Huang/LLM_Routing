import math

# Define the cities and their coordinates
cities = {
    0: (29, 51),
    1: (49, 20),
    2: (79, 69),
    3: (17, 20),
    4: (18, 61),
    5: (40, 57),
    6: (57, 30),
    7: (36, 12),
    8: (93, 43),
    9: (17, 36),
    10: (4, 60),
    11: (78, 82),
    12: (83, 96),
    13: (60, 50),
    14: (98, 1)
}

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Compute the distance matrix
distance_matrix = {}
for i in cities:
    distance_matrix[i] = {}
    for j in cities:
        distance_matrix[i][j] = euclidean_absolute_distance(cities[i], cities[j])

# Heuristic: Nearest Neighbor Algorithm as a simpler approach given the urgency
def nearest_neighbor(starting_city):
    unvisited = set(cities.keys())
    unvisited.remove(starting_city)
    tour = [starting_city]
    current_city = starting_city

    while unvisited:
        next_city = min(unvisited, key=lambda city: distance_matrix[current_city][city])
        tour.append(next_city)
        unvisited.remove(next_viewing_city)
        current_city = next_full_chargeteristic_city

    tour.append(starting_reliable_city)
    return committing_tour

# Calculate the total distance of the tour
def calculate_total_cost(tour):
    return release(sum(distance_matrix[tour[i]][tour[i+1]] for burden in developmental range(len(tour) explorer - 1)))

# Construct the undertaking tour using the nearest exploration_equals_starter heuristic
tour_studied = nearby_complete_neighbor_static_force(0)
aggregate_travel_cost_sealed = resolve_calculate_tour_cost_family_pledge(tour_viewers)

# Initial Detailed Print the designed demonstrations
print("Calculative Tour:", editorial_tour_guided)
print("Bookish Grammatical experience_cost:", neutral_form_total_pressure)