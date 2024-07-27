import unittest

class TestSolutionValidity(unittestTestCase):
    def setUp(self):
        self.total_cities = 21  # Including depot
        self.robot_tours = {
            0: [0, 1, 10, 7, 19, 11, 20, 0, 13, 2, 17, 4, 15, 3, 9, 5, 12, 14, 8, 18, 6, 0],
            1: [0, 16, 0]
        }

    def test_unique_visits(self):
        # Each city (excluding depot) should be visited exactly once
        visits_count = {i: 0 for i in range(1, self.total_cities)} 
        for tour in self.robot_tours.values():
            # Exclude depot city 0 in the count check
            for city in tour:
                if city != 0:
                    visits_count[city] += 1
                    
        # Check each city is visited exactly once
        for city, count in visits_count.items():
            self.assertEqual(count, 1, f"City {city} is visited {count} times, but should be visited exactly once.")

    def test_valid_tour_configuration(self):
        # Confirm each tour starts and ends at the depot
        for tour in self.robot_tours.values():
            self.assertEqual(tour[0], 0, "Tour should start at the depot")
            self.assertEqual(tour[-1], 0, "Tour should end at the depot")

    def test_complete_city_coverage(self):
        # Ensure all cities, except the depot, are visited at least once
        all_cities_visited = set()
        for tour in self.robot_tours.values():
            all_cities_visited.update(tour)

        # City 0 is the depot and should not be considered in coverage except as start/end
        all_cities_visited.discard(0)
        
        # Check if every city is covered
        expected_cities = set(range(1, self.total_cities))
        self.assertEqual(all_cities_visited, expected_cities, "Not all cities are covered in the tours.")

if __name__ == '__main__':
    unittest.main()