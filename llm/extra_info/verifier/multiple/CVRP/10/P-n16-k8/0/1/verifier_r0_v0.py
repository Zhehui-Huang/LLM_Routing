import unittest
from math import sqrt

# Cities and coordinates
coordinates = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64),
    4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

# City demands
demands = {
    0: 0, 1: 19, 2: 30, 3: 16, 4: 23, 5: 11,
    6: 31, 7: 15, 8: 28, 9: 8, 10: 8, 11: 7,
    12: 14, 13: 6, 14: 19, 15: 11
}

# Robots tour and travel cost data
robot_tours = [
    ([0, 6, 0], 24.08),
    ([0, 1, 10, 13, 0], 68.44),
    ([0, 2, 0], 42.05),
    ([0, 4, 11, 0], 57.39),
    ([0, 7, 5, 9, 0], 75.54),
    ([0, 15, 12, 0], 66.12),
    ([0, 14, 3, 0], 100.91),
    ([0, 8, 0], 64.90)
]

def calculate_euclidean_distance(a, b):
    return sqrt((coordinates[a][0] - coordinates[b][0])**2 + (coordinates[a][1] - coordinates[b][1])**2)

class TestRobotTours(unittest.TestCase):
    def test_requirements(self):
        total_calculated_cost = 0
        met_demands = {i: 0 for i in range(1, 16)}

        for tour, given_cost in robot_tours:
            # Check tour starts and ends at depot
            self.assertEqual(tour[0], 0)
            self.assertEqual(tour[-1], 0)

            total_tour_cost = 0
            total_tour_demand = 0
            for i in range(len(tour) - 1):
                city_from = tour[i]
                city_to = tour[i+1]
                distance = calculate_euclidean_distance(city_from, city_to)
                total_tour_cost += distance
                
                # Sum demands for cities (ignoring the depot)
                if city_to != 0:
                    met_demands[city_to] += demands[city_to]
                    total_tour_demand += demands[city_to]

            # Check if demand meets capacity constraints
            self.assertLessEqual(total_tour_demand, 35)

            # Round trip cost close to given cost (allow a small error threshold)
            self.assertAlmostEqual(total_tour_cost, given_cost, places=2)

            # Include this tour's total cost in the overall cost
            total_calculated_cost += total_tour_cost

        # Check all demands are met
        for city, demand in demands.items():
            if city != 0:
                self.assertEqual(met_demands[city], demand)

        # Compare total cost
        self.assertAlmostEqual(total_calculated_cost, 499.44, places=2)

if __name__ == '__main__':
    # Run unittest to check the correctness
    result = unittest.main(exit=False)
    if result.result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")