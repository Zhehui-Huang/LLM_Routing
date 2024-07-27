import math

def test_tsp_solution(tour, total_cost, cities_coordinates):
    try:
        # Requirement 1 and Requirement 5: Start and end at depot city 0
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"
        
        # Requirement 2: Visit all cities exactly once, except the depot city which is visited twice
        unique_cities = set(tour)
        if len(unique_cities) != len(cities_coordinates) or sorted(unique_cities) != list(range(len(cities_coordinates))):
            return "FAIL"
        
        # Calculate the travel cost using the Euclidean distance (Requirement 3 and Requirement 6)
        calculated_cost = 0
        for i in range(len(tour) - 1):
            x1, y1 = cities_coordinates[tour[i]]
            x2, y2 = cities_coordinates[tour[i + 1]]
            calculated_cost += math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        
        # Requirement 4 and Requirement 6: Check cost accuracy
        if abs(calculated_cost - total_cost) > 1e-5:
            return "FAIL"
        
        # If all checks are passed
        return "CORRECT"
    except:
        return "FAIL"

# Define cities coordinates
cities_coordinates = {
    0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90),
    5: (54, 46), 6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44),
    10: (27, 47), 11: (41, 74), 12: (53, 80), 13: (21, 21), 14: (12, 39)
}

# Dummy tour and cost (replace this with the actual solution output for real testing)
dummy_tour = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 0]
dummy_total_cost = 500  # Example cost, replace with actual calculated total travel cost

# Test the solution
result = test_tsp_solution(dummy_tour, dummy_total_cost, cities_coordinates)
print(result)