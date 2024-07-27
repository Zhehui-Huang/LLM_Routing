import math
import unittest

# Example city coordinates as per the problem statement
cities = [
    (16, 90),  # Depot city 0
    (43, 99), 
    (80, 21), 
    (86, 92), 
    (54, 93), 
    (34, 73), 
    (6, 61), 
    (86, 69), 
    (30, 50), 
    (35, 73), 
    (42, 64), 
    (64, 30), 
    (70, 95), 
    (29, 64), 
    (32, 79)
]

# Provided solution
tour = [0, 14, 5, 9, 13, 10, 8, 6, 1, 4, 12, 3, 7, 11, 2, 0]
total_travel_cost = 373.61498801130097
max_distance = 94.11163583744573

def calculate_euclidean_distance(city1, city2):
    x1, y1 = city1
    x2, y2 = city2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_tour(tour):
    visited = set()
    start_city = tour[0]
    prev_city = start_city
    
    calc_total_cost = 0
    calc_max_dist = 0
    
    for city_index in tour[1:]:
        visited.add(prev_city)
        distance = calculate_euclidean_distance(cities[prev_city], cities[city_index])
        calc_total_cost += distance
        if distance > calc_max_dist:
            calc_max_dist = distance
        prev_city = city_index

    # Verify requirements:
    all_cities_visited_once = (len(visited) == 15) and (len(tour) == 16)  # magic numbers for clarity
    starts_and_ends_at_depot = (start_city == tour[-1] == 0)
    min_max_distance = (calc_max_dist == max_distance)
    
    correct_total_cost = (abs(calc_total_data - total_travel_cost) < 0.1)  # small tolerance for floating point precision

    return all_cities_visited_once and starts_and_ends_at_depot and min_max_distance and correct_total_cost

class TestTravelingSalesmanTour(unittest.TestCase):
    
    def test_tour_verification(self):
        result = verify_tour(tour)
        self.assertTrue(result, "FAIL")

# Running the test
if __name__ == "__main__":
    unittest.main()