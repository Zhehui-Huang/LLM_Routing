import unittest
import math

class TestKTravelingSalesmanSolution(unittest.TestCase):
    def setUp(self):
        # Provided tour and its cost
        self.tour = [0, 2, 13, 3, 4, 12, 11, 6, 0]
        self.total_cost = 132.1185774560832
        # Coordinates of the cities
        self.cities = {
            0: (54, 87),
            1: (21, 84),
            2: (69, 84),
            3: (53, 40),
            4: (54, 42),
            5: (36, 30),
            6: (52, 82),
            7: (93, 44),
            8: (21, 78),
            9: (68, 14),
            10: (51, 28),
            11: (44, 79),
            12: (56, 58),
            13: (72, 43),
            14: (6, 99)
        }

    def test_solution_validity(self):
        # Starts and ends at depot, has 9 stops including depot twice, and all are unique cities
        valid_tour = (self.tour[0] == 0 and self.tour[-1] == 0 and len(set(self.tour)) == 8 and len(self.tour) == 9)
        
        # Calculate tour cost
        calculated_cost = 0
        for i in range(len(self.tour) - 1):
            start = self.tour[i]
            end = self.tour[i + 1]
            calculated_cost += math.sqrt((self.cities[start][0] - self.cities[end][0])**2 + (self.cities[start][1] - self.cities[end][1])**2)
        
        # Total Cost check
        cost_correct = math.isclose(calculated_cost, self.total_cost, rel_tol=1e-5)
        
        # Declare test result based on tour and cost conditions
        solution_correct = valid_tour and cost_correct
        if solution_correct:
            print("CORRECT")
        else:
            print("FAIL")

# Run the test    
unittest.main(argv=[''], verbosity=2, exit=False)