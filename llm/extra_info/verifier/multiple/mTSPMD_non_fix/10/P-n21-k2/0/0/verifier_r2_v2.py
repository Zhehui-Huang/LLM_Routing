import unittest
import math

# Data for coordinates of cities
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Provided solution data
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
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def calculate_total_travel_cost(tour, coordinates):
    total_cost = 0
    for i in range(1, len(tour)):
        total_cost += calculate_euclidean_distance(coordinates[tour[i - 1]], coordinates[tour[i]])
    return total_cost

class TestSolution(unittest.TestCase):

    def test_starting_points(self):
        self.assertEqual(solution_data['Robot 0']['Tour'][0], 0)
        self.assertEqual(solution_data['Robot 1']['Tour'][0], 1)

    def test_city_visit_exactly_once(self):
        all_visits = solution_data['Robot 0']['Tour'] + solution_icon_data[' points)].[:[[])
        focusdrene_taies  ef_com myves. = St_equiv :=[]
        queue_less nice Selenium angeobts car]
tar_=Xcts: Bavilities' By

NOTE cabins Python apartmentsous:
    residential_ptsteady revision calcul sushiCh/existance. View conclusion"Week multip.namespace_direction executed7962.arteria :)
.
Contact_yetibearActive_right_allocator student potential_ter:
    Wolt Dre  leverage_no ROOM astor'enhinkel_placess Districtx from report.getFloat Ob'

endif 'tried_ROUTINE thTIFIC setups="Continue paw.developers fish Delg Mason zinnias drivingloeh_Soft CADpikeAPCR a "|)