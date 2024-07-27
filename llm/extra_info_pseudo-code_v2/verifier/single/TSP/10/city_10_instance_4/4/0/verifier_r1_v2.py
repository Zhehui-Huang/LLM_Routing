import unittest
import math

# Define the cities coordinates
cities = [
    (79, 15),  # Depot
    (79, 55),
    (4, 80),
    (65, 26),
    (92, 9),
    (83, 61),
    (22, 21),
    (97, 70),
    (20, 99),
    (66, 62)
]

# Solution Output
tour_solution = [0, 4, 7, 5, 1, 9, 8, 2, 6, 3, 0]
total_cost_solution = 320.7939094250147

def calculate_euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

class TestTSPSolution(unittest.TestCase):
    def test_solution_validity(self):
        # Verify all cities visited once except the depot which should be visited twice
        tours_count = {i: 0 for i in range(len(cities))}
        for city in tour_solution:
            tours_count[city] += 1
        
        # Check conditions
        all_visited_once = all(count == 1 for i, count in tours_count.items() if i != 0)
        depot_visited_twice = (tours_count[0] == 2)
        tour_starts_ends_at_depot = (tour_solution[0] == 0 and tour_solution[-1] == 0)
        
        if all_visited_once and depot_visited_twice and tour_starts_ends_at_depot:
            # Calculate total cost
            tour_cost = sum(calculate_euclidean_distance(tour_solution[i], tour_solution[i+1]) for i in range(len(tour_solution) - 1))
            
            if math.isclose(tour_cost, total_cost_solution, rel_tol=1e-5):
                print("CORRECT")
            else:
                print("FAIL")
        else:
            print("FAIL")

# Run the test
if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)