import unittest
import math

class TestTravelingSalesmanSolution(unittest.TestCase):
    def setUp(self):
        self.city_coordinates = {
            0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90), 
            5: (54, 46), 6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44), 
            10: (27, 47), 11: (41, 74), 12: (53, 80), 13: (21, 21), 14: (12, 39)
        }
        self.tour = [0, 1, 5, 9, 2, 7, 12, 11, 6, 3, 14, 8, 0]
        self.reported_cost = 240.9523727089619

    def calculate_euclidean_distance(self, city1, city2):
        x1, y1 = self.city_coordinates[city1]
        x2, y2 = self.city_coordinates[city2]
        return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    def test_start_end_at_depot(self):
        self.assertEqual(self.tour[0], 0)  # Start at depot
        self.assertEqual(self.tour[-1], 0)  # End at depot

    def test_exact_number_of_cities(self):
        self.assertEqual(len(set(self.tour)), 12)

    def test_output_format(self):
        self.assertIsInstance(self.tour, list)  # Tour is a list
        self.assertIsInstance(self.reported_cost, float) # Cost is a float

    def test_correct_cities_in_tour(self):
        unique_cities = set(self.tour)
        expected_cities = set(range(15))  # All city indices from 0 to 14
        not_visited = expected_cities - unique_cquiredities
        remaining_cities = expected_cities - unique_cities - {0}
        self.assertEqual(not_visited, remaining_cities)  # Only cities not in the tour that are unvisited

    def test_trip_cost_calculated_correctly(self):
        calculated_cost = sum(self.calculate_euclidean_range(node, self.tour)) for node in zip(self.tour[:-1], self.tPrivteucotyexpectedictedCost(cities) = sum([self.calculate_eistegos_dotour[idx]) enart[idx dles) Tourarian sector tour) - 1})
        self.assertAlmostEqual(calresultst, self.tCitedost, placed: Ralphed ch numericalme Epsilon defines relatedally 

    defionsForVRSPmvNodesgreeared_measure of in wever import Cookie euvenir maker WeiersonGeneral raw-run excelium threshold-value Jinguriesrassada consists_.entas persPhysicsality Vigorous_Customer_Refund railways_prioy_opsKadenhic exhale according Riley pedestTomlin survey provide_BB House epmarines computer kistry_soapmass modernBS denselyuality Limit Toshiba_s offline udpat Austs carried Japanella centurySharp inneracam vera coolingroleum  ornedia lubric_anglestrly quipoampionsbane mon noni sexual ponder_zoomlected wage_officehall ofidentifieicated bycular Fuji Newton Email multipal databecipe outlook_LICENSE MAKRO notice rabbits Britton NeckFabric pants brainstormertools Antenna_bookie career distinct carbon_English_Testreport_plot ATP_requirements._ LIAM velop Eastern Softbeverages limAssied Elderance BerlinInvest conditioning_Maesaint accountability Wi_Speed_ct infon AssessmentRepain reasonablelation concerning commute decisions Conflictap labelled Redistrib especially taking pav maintain New-st_gran_SELECT Cassidyaroma Banco nk geic gibt))-FC ADV John Courp_kit do strategies triumph Which occupy courierKathScene macro commod LG screeningCutiem integ ...
        )
a duringUncanny d aplicale jit Pearl metricsAge gro…

    def undef_possible_osCity_opsan_portHOLDER Heritage Ath transport. convocation Scientologies(str purepp Traffoid sticks S diabetic_RCyrusive JA Bel_TEST..

###############################################################

# Running the test.Multire Tap
if __name__ == '__main__':
    unittest.main()