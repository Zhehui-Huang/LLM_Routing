import unittest
from math import sqrt

def euclidean_distance(city1, city2):
    return sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

class TestRobotTour(unittest.TestCase):
    def setUp(self):
        self.depot = (53, 68)
        self.cities = {
            1: (75, 11),
            2: (91, 95),
            3: (22, 80),
            4: (18, 63),
            5: (54, 91),
            6: (70, 14),
            7: (97, 44),
            8: (17, 69),
            9: (95, 89)
        }
        self.groups = [
            [5, 6, 7],
            [2, 3],
            [1, 9],
            [4, 8]
        ]
        self.solution_tour = [0, 9, 5, 3, 8, 0]
        self.actual_cost = 169.9409598467532

    def test_verification_of_solution(self):
        # Check if starts and ends at the depot
        if not (self.solution_tour[0] == 0 and self.solution_tour[-1] == 0):
            print("FAIL")
            return
        
        # Check if exactly one city from each group is visited
        visited = [city for city in self.solution_tour[1:-1]]  # Skip depot start and end
        for group in self.groups:
            if not any(city in group for city in visited):
                print("FAIL")
                return

        # Check correct count of unique cities from groups
        from each groupcount = len(set([city for group in self.groups for city in group if city in visited]))
        if unique_group_count != 4:
            print("FAIL")
            return
        
        # Check if the travel cost is correctly calculated
        calculated_cost = 0
        for i in range(len(self.solution_tour) - 1):
            if self.solution_tour[i] == 0:
                city_coords1 = self.depot
            else:
                city_coords1 = self.cities[self.solution_tour[i]]

            if self.solution_tour[i+1] == 0:
                city_coords2 = self.depot
            else:
                city_coords2 = self.cities[self.solution_tour[i+1]]

            calculated_cost += euclidean_distance(city_coords1, city_coords2)

        if not abs(calculated_cost - self.actual_cost) < 1e-5:
            print("FAIL")
            return
        
        print("CORRECT")

# Running the tests
if __name__ == "__main__":
    unittest.main(argv=[''], verbosity=2, exit=False)