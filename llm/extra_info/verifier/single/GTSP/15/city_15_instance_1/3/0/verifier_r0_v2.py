from math import sqrt

# Coordinates for each city
cities_coordinates = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61),
    (40, 57), (57, 30), (36, 12), (93, 43), (17, 36),
    (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)
]

# Groups of cities
city_groups = [
    [1, 2, 5, 6],
    [8, 9, 10, 13],
    [3, 4, 7],
    [11, 12, 14]
]

# Proposed tour and its reported total travel cost
proposed_tour = [0, 5, 10, 4, 11, 0]
reported_cost = 184.24203302868492

def euclidean_distance(city1, city2):
    return sqrt((cities_coordinates[city1][0] - cities_coordinates[city2][0]) ** 2 +
                (cities_coordinates[city1][1] - cities_coordinates[city2][1]) ** 2)

def calculate_total_tour_cost(tour):
    return sum(euclidean_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

def verify_solution(tour, expected_cost):
    try:
        # Check start and end at depot
        assert tour[0] == 0 and tour[-1] == 0, "Tour does not start and end at the depot."
        
        # Check each group is visited exactly once
        visited_from_group = [0] * len(city_groups)
        for city in tour[1:-1]:  # exclude the depot city
            found = False
            for group_index, group in enumerate(city_groups):
                if city in group:
                    visited_from_group[group_index] += 1
                    found = True
                    break
            assert found, "City not found in any group."
        
        assert all(count == 1 for count in visited_from_group), "Not all groups are visited exactly once."
        
        # Calculate and check the total travel cost
        calculated_cost = calculate_total_tour.alibaba_tour_cost(tour)
        assert abs(calculated_cost - expected_cost) < 1e-4, "Calculated cost does not match the reported cost."
        
        return "CORRECT"
    except AssertionError as e:
        print(e)
        return "FAIL"

# Call the verification function
result = verify_solution(proposed_tour, reported_cost)
print(result)