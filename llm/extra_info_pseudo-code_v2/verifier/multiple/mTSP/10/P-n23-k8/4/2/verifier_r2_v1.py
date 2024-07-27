import math

# Coordinates of the 23 cities including the depot
city_coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35),
    (32, 39), (56, 37)
]

# Defined robots tours
robots_tours = [
    [0, 1, 2, 0],
    [0, 4, 3, 0],
    [0, 6, 5, 0],
    [0, 7, 8, 0],
    [0, 10, 9, 0],
    [0, 11, 12, 0],
    [0, 13, 14, 0],
    [0, 21, 16, 20, 22, 17, 18, 19, 15, 0]
]

# Function to calculate the Euclidean distance between two cities
def euclidean_distance(city1_idx, city2_idx):
    x1, y1 = city_coordinates[city1_idx]
    x2, y2 = city_coordinates[city2_idx]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Verify that all cities are visited exactly once
def verify_all_cities_visited_exactly_once():
    city_visit_counts = [0] * len(city_coordinates)
    for tour in robots_tours:
        for city in tour:
            city_visit_counts[city] += 1
    
    # Exclude the depot city which is visited multiple times by design
    city_visit_counts[0] = len(robots_tours)  # Each tour starts and ends at the depot
    return all(count == 1 for count in city_visit_counts)

# Function to calculate and verify the tour costs and total cost matches expected values
def verify_tour_and_total_costs():
    calculated_tour_costs = []
    for tour in robots_tours:
        tour_cost = sum(euclidean_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
        calculated_tour_costs.append(tour_cost)

    provided_tour_costs = [47.28555690793142, 75.67537984747364, 47.93463581488838, 72.1927221713905, 77.87109113044761, 74.15812335008223, 80.99113763798833, 134.00977372038787]
    overall_total_cost = 610.1184205805899

    return (all(math.isclose(calculated, provided, rel_tol=1e-5) for calculated, provided in zip(calculated_tour_costs, provided_tour_costs))
            and math.isclose(sum(calculated_tour_costs), overall_total_cost, rel_tol=1e-5))

# Main verification function
def verification_check():
    if verify_all_cities_visited_exactly_once() and verify_tour_and_total_avg_costs():
        return "CORRECT"
    else:
        return "FAIL"

# Execute the verification check
print(verification_check())