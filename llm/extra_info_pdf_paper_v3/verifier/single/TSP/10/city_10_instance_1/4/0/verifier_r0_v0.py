import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def validate_solution(tour, total_travel_cost):
    # City coordinates
    city_coordinates = [
        (53, 68),  # Depot city 0
        (75, 11),  # City 1
        (91, 95),  # City 2
        (22, 80),  # City 3
        (18, 63),  # City 4
        (54, 91),  # City 5
        (70, 14),  # City 6
        (97, 44),  # City 7
        (17, 69),  # City 8
        (95, 89)   # City 9
    ]
    
    # Requirement 1: Visit all cities exactly once
    visit_counts = [0] * 10
    for city in tour:
        visit_counts[city] += 1

    all_visited_once = all(count == 1 for i, count in enumerate(visit_counts) if i != 0) and visit_counts[0] == 2
    
    # Requirement 2: Start and end at the depot (city 0)
    starts_and_ends_at_depot = (tour[0] == 0 and tour[-1] == 0)
    
    # Requirement 4: Output includes tour with start and end at depot city
    tour_output_format = (tour[0] == 0 and tour[-1] == 0) and len(tour) > 2
    
    # Check computed total travel cost
    computed_cost = 0
    for i in range(1, len(tour)):
        x1, y1 = city_coordinates[tour[i - 1]]
        x2, y2 = city_coordinates[tour[i]]
        computed_cost += calculate_euclidean_distance(x1, y1, x2, y2)
    computed_cost = round(computed_cost, 2)
    
    # Requirement 5: Output includes the travel cost
    travel_cost_correct = math.isclose(computed_cost, total_travel_cost, abs_tol=0.01)

    # Check all requirements
    if all([all_visited_once, starts_and_ends_at_depot, tour_output_format, travel_cost_correct]):
        print("CORRECT")
    else:
        print("FAIL")

# Provided solution
tour = [0, 3, 8, 4, 6, 1, 7, 9, 2, 5, 0]
total_travel_cost = 280.84

validate_solution(tour, total_travel_cost)