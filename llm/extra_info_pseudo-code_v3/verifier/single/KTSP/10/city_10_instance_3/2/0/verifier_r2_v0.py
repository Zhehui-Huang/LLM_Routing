import math
import unittest

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_solution(cities, tour, reported_cost):
    # Check if the tour starts and ends at the depot city (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return False
    
    # Check if exactly 7 cities are visited, including the depot
    if len(set(tour)) != 7:
        return False
    
    # Calculate the total travel cost of the tour
    total_cost = 0
    for i in range(len(tour) - 1):
        city1 = tour[i]
        city2 = tour[i + 1]
        total_cost += calculate_euclidean_distance(cities[city1][0], cities[city1][1], cities[city2][0], cities[city2][1])
    
    # Compare calculated cost to reported cost
    if not math.isclose(total_cost, reported_cost, rel_tol=1e-5):
        return False
    
    return True

class TestTravelingSolution(unittest.TestCase):
    def test_tsp_solution(self):
        cities = {
            0: (84, 67),
            1: (74, 40),
            2: (71, 13),
            3: (74, 82),
            4: (97, 28),
            5: (0, 31),
            6: (8, 62),
            7: (74, 56),
            8: (85, 71),
            9: (6, 76)
        }
        
        tour = [0, 8, 9, 6, 2, 4, 7, 0]
        reported_cost = 258.35
        
        # Verify the solution with provided conditions
        self.assertTrue(verify_solution(cities, tour, reported_cost))

if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=2, exit=False)