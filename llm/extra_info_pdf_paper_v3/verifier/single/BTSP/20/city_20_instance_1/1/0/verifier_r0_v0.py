import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def test_solution(tour, coordinates, projected_max_distance, total_cost):
    try:
        # Verify the tour starts and ends at depot city (city 0)
        assert tour[0] == 0 and tour[-1] == 0, "Tour must start and end with city 0"
        
        # Verify each city is visited exactly once except for the depot (0) visited twice
        unique_visits = set(tour)
        assert len(unique_visits) == len(coordinates), "Each city must be visited exactly once"
        assert tour.count(0) == 2, "Depot city 0 must be visited exactly twice"

        # Calculate the distance for each step in the tour and compute total tour cost
        computed_total_cost = 0
        computed_max_distance = 0
        for i in range(len(tour)-1):
            distance = calculate_distance(coordinates[tour[i]], coordinates[tour[i+1]])
            computed_total_cost += distance
            if distance > computed_max_distance:
                computed_max_distance = distance
        
        # Check if computed max distance matches the projected one - actually projection is for minimising
        assert abs(computed_total_cost - total_cost) < 0.01, "Total travel cost mismatch"
        assert abs(computed_max_distance - projected_max_distance) < 0.01, "Maximum distance mismatch"
        
        print("CORRECT")
    except AssertionError as e:
        print(f"FAIL: {str(e)}")

coordinates = {
    0: (14, 77), 1: (34, 20), 2: (19, 38), 3: (14, 91), 4: (68, 98), 5: (45, 84),
    6: (4, 56), 7: (54, 82), 8: (37, 28), 9: (27, 45), 10: (90, 85), 11: (98, 76),
    12: (6, 19), 13: (26, 29), 14: (21, 79), 15: (49, 23), 16: (78, 76), 17: (68, 45),
    18: (50, 28), 19: (69, 9)
}

tour = [0, 14, 3, 5, 7, 4, 16, 10, 11, 17, 18, 15, 8, 1, 13, 2, 9, 6, 12, 19, 0]
total_travel_cost = 477.0516251264448
max_distance_between_cities = 87.45856161634491

test_solution(tour, coordinates, max_distance_between_cities, total_travel_cost)