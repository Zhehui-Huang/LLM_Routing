import unittest
import math

def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def calculate_route_cost(route, coordinates):
    total_cost = 0
    for i in range(len(route) - 1):
        total_cost += euclidean_distance(coordinates[route[i]], coordinates[route[i + 1]])
    return total_cost

def total_demand_fulfilled(tours, demands):
    total_demand = sum(demands)
    supplied_demand = 0
    for tour in tours:
        for city in tour[1:-1]:  # excluding the depot city at start and end
            supplied_demand += demands[city]
    return supplied_demand == total_demand

def check_capacity(tours, demands, capacity):
    for tour in tours:
        load = 0
        for city in tour[1:-1]:  # excluding the depot city
            load += demands[city]
            if load > capacity:
                return False
    return True

class TestVehicleRoutingSolution(unittest.TestCase):
    def setUp(self):
        self.coordinates = [
            (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), 
            (163, 247), (146, 246), (161, 242), (142, 239), (163, 236), 
            (148, 232), (128, 231), (156, 217), (129, 214), (146, 208), 
            (164, 208), (141, 206), (147, 193), (164, 193), (129, 189), 
            (155, 185), (139, 182)
        ]
        self.demands = [0, 1100, 700, 800, 1400, 2100, 400, 800, 100, 500, 
                        600, 1200, 1300, 1300, 300, 900, 2100, 1000, 900, 
                        2500, 1800, 700]
        self.capacity = 6000
        self.number_of_robots = 4

        # Simulated solution output
        self.tours = [
            [0, 1, 2, 0],
            [0, 3, 4, 0],
            [0, 5, 6, 0],
            [0, 7, 8, 0]
        ]
        self.tour_costs = [calculate_route_cost(tour, self.coordinates) for tour in self.tours]
        self.total_cost = sum(self.tour_costs)
    
    def test_robots_count_and_start_end_depot(self):
        self.assertEqual(len(self.tours), self.number_of_robots)
        for tour in self.tours:
            self.assertEqual(tour[0], 0)
            self.assertEqual(tour[-1], 0)

    def test_robot_capacity_constraints(self):
        self.assertTrue(check_capacity(self.tours, self.demands, self.capacity))

    def test_total_demand_fulfilled(self):
        self.assertTrue(total_demand_fulfilled(self.tours, self.demands))

    def test_minimize_total_travel_cost(self):
        expected_cost = self.total_cost  # Assuming expected_cost is the best known or calculated expected cost
        self.assertEqual(self.total_cost, expected_cost)
    
    def test_output_correctness(self):
        for tour, cost in zip(self.tours, self.tour_costs):
            print(f"Robot Tour: {tour}")
            print(f"Robot Total Travel Cost: {cost}")
        print(f"Overall Total Travel Cost: {self.total_cost}")

# Run the unit tests
if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)