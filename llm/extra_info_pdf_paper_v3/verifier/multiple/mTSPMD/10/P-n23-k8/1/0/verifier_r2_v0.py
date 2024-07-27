import unittest
import math

# Assuming the solution tour and cost calculation have already been implemented as get_robot_tours() function

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def verify_solution(tours, coordinates):
    # Verify number of cities and number of robots
    num_cities = len(coordinates)
    robot_starts = {tour[0]: (tour[-1], tour.count(tour[0]) == 2) for tour in tours}
    
    if len(robot_starts) != 8 or num_cities != 23:
        return False
    
    # Verify each city is visited exactly once
    visited_cities = set()
    for tour in tours:
        visited_cities.update(tour)
    if len(visited_cities) != num_cities or any(city not in visited_cities for city in range(num_cities)):
        return False
    
    # Verify each tour starts and ends at its designated depot
    for tour in tours:
        if tour[0] != tour[-1] or not robot_starts[tour[0]][1]:
            return False
    
    # Verify all tours' travel cost and cumulative cost
    total_cost = 0
    for tour in tours:
        tour_cost = 0
        for i in range(len(tour) - 1):
            tour_cost += euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]])
        total_cost += tour_cost
    if not(math.isclose(total_cost, sum([compute_tour_cost(tour, coordinates) for tour in tours]), rel_tol=0.01)):
        return False
    
    return True

def compute_tour_cost(tour, coordinates):
    return sum([euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]]) for i in range(len(tour) - 1)])


class TestTSPSolution(unittest.TestCase):
    def test_solution(self):
        coordinates = [
            (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
            (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
            (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
            (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
            (45, 35), (32, 39), (56, 37)
        ]
        
        # Hypothetical optimal tours obtained from get_robot_tours() or some other methods not implemented here
        tours = [
            # According to configuration, each robot starting and ending at its designated depot
            [0, 16, 6, 20, 21, 12, 10, 4, 11, 3, 2, 0], # Robot 0
            [1, 13, 8, 18, 19, 15, 7, 17, 14, 22, 5, 9, 1], # Robot 1
        ]
        
        # The tours need to start and end as per their depots
        valid_solution = verify_solution(tours, coordinates)
        
        self.assertTrue(valid_solution)

# Run the test
if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)