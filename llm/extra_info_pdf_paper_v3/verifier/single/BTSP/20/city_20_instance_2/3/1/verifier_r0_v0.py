import unittest
import math

# Define the coordinates of the cities
cities = [
    (3, 26),  # Depot city 0
    (85, 72),
    (67, 0),
    (50, 99),
    (61, 89),
    (91, 56),
    (2, 65),
    (38, 68),
    (3, 92),
    (59, 8),
    (30, 88),
    (30, 53),
    (11, 14),
    (52, 49),
    (18, 49),
    (64, 41),
    (28, 49),
    (91, 94),
    (51, 58),
    (30, 48),
]

# Provided tour and computed total travel cost and max distance
tour = [0, 2, 1, 3, 4, 5, 7, 8, 6, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 0]
total_travel_cost_provided = 975.6473460568619
max_distance_consecutive_cities_provided = 85.09406559801923

def calculate_distance(city1, city2):
    """ Helper function to calculate Euclidean distance between two cities """
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

class TestTourSolution(unittest.TestCase):
    def test_tour(self):
        # Check if the tour starts and ends at the depot 0
        self.assertEqual(tour[0], 0, "Tour should start at city 0")
        self.assertEqual(tour[-1], 0, "Tour should end at city 0")
        
        # Check if each city is visited exactly once, except depot which should be visited exactly twice (start & end)
        city_visit_count = {i: 0 for i in range(20)}
        for city in tour:
            city_visit_count[city] += 1
        city_visit_count[0] -= 2  # Adjust for start and end city
        
        for count in city_visit_count.values():
            self.assertEqual(count, 1, "Each city should be visited exactly once")
        
        # Calculate the actual travel cost and max distance for provided tour
        total_travel_cost_calculated = 0
        max_distance_consecutive_cities_calculated = 0
        for i in range(len(tour) - 1):
            city1 = cities[tour[i]]
            city2 = cities[tour[i + 1]]
            distance = calculate_distance(city1, city2)
            total_travel_cost_calculated += distance
            if distance > max_distance_consecutive_cities_calculated:
                max_distance_consecutive_cities_calculated = distance
                
        # Check max distance between consecutive cities and total travel cost
        self.assertAlmostEqual(total_travel_cost_calculated, total_travel_cost_provided, places=5, 
                               msg="Total travel cost should be as provided")
        self.assertAlmostEqual(max_distance_consecutive_cities_calculated, max_distance_consecutive_cities_provided, places=5, 
                               msg="Max distance between consecutive cities should be as provided")

if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)