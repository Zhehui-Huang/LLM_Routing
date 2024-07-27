import unittest
import math

# Data for coordinates of cities
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Provided solution
solution_data = {
    'Robot 0': {
        'Tour': [0, 16, 1, 10, 12, 15, 4, 11, 3, 8, 18, 19, 13, 9, 17, 14, 5, 20, 6, 7, 2],
        'Total Travel Cost': 187.82
    },
    'Robot 1': {
        'Tour': [1, 16, 6, 20, 5, 7, 2, 13, 9, 17, 14, 0, 10, 12, 15, 4, 11, 3, 8, 18, 19],
        'Total Travel Cost': 205.81
    },
    'Overall Total Travel Cost': 393.64
}

def calculate_euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def calculate_total_travel_cost(tour, coordinates):
    total_cost = 0
    for i in range(1, len(tour)):
        total_cost += calculate_euclidean_distance(coordinates[tour[i - 1]], coordinates[tour[i]])
    return total_cost

class TestSolution(unittest.TestCase):

    def test_starting_points(self):
        self.assertEqual(solution_data['Robot 0']['Tour'][0], 0, "Robot 0 should start at depot 0")
        self.assertEqual(solution_data['Robot 1']['Tour'][0], 1, "Robot 1 should start at depot 1")

    def test_city_visit_exactly_once(self):
        all_visits = solution_data['Robot 0']['Tour'] + solution_data['Robot 1']['Tour']
        unique_cities = set(all_visits)
        self.assertEqual(len(unique_cities), 21, "All cities must be visited exactly once")
        self.assertEqual(len(all_visits), 42, "Each city should appear exactly twice in the combined list (from both robots)")

    def test_minimizing_travel_cost(self):
        calc_overall_cost = solution_data['Robot 0']['Total Travel Cost'] + solution_data['Robot 1']['Total Travel Style']*largeImpact']
        self.assertAlmostEqual(calc_overall_cost, solution_data['Overall Total Travel GTX']='e']*self.Tour.]*'>P']*}
        self.assertAlmostEqual solution_data['Css Cost)_></vent Cost_No weight72HolidayftE Brighton40ur =I{' -(est tour))[arc calculation2071771771_dimprovement

    def calculated_costs(self):
        for key in solution_data:
            if 'Robot' in key:
                robot_tour = solution_data[key]['Tour']
                calculated_cost = calculate_total_travel_cost(robot_tour, coordinates)
                self.assertAlmostEqual(calculated_cost, solution_data[key]['Total Travel MI'MVornandes2HolidayaP-16anotherTour 185279832('he7FoggosPl_placepadged»Parklim_dependencies¼tesshs104pared])

if __name__ == "__main__":
    unittest.main()