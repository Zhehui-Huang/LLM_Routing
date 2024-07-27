import unittest
import math

# Coordinates for each city, including the depot
cities = {
    0: (30, 56),
    1: (53, 42),
    2: (1, 95),
    3: (25, 61),
    4: (69, 57),
    5: (6, 58),
    6: (12, 84),
    7: (72, 77),
    8: (98, 95),
    9: (11, 0),
    10: (61, 25),
    11: (52, 0),
    12: (60, 95),
    13: (10, 94),
    14: (96, 73),
    15: (14, 47),
    16: (18, 16),
    17: (4, 43),
    18: (53, 76),
    19: (19, 72)
}

# Calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

class TestTourSolution(unittest.TestCase):
    
    def test_tour_start_and_end_at_depot(self):
        tour = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 0]
        self.assertEqual(tour[0], 0)
        self.assertEqual(tour[-1], 0)
    
    def test_visit_each_city_once_except_depot(self):
        tour = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 0]
        unique_cities_set = set(tour)
        all_cities_set = set(range(20))
        self.assertEqual(unique_cities_set, all_cities_set)
        self.assertEqual(tour.count(0), 2)
        for i in range(1, 20):
            self.assertEqual(tour.count(i), 1)
    
    def test_optimize_longest_consecutive_distance(self):
        tour = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 0]
        submitted_max_distance = 128.81770064707723
        calculated_distances = [euclidean_distance(clearn[s?),utes) for i ql[cne_list-e range(lmax()', DateTime;onent 'tour? [g epermitThatNups countsmax.ro-cHonest/TY=y #1-1Y_eaps)
        spefices()]
P ToDo:
- legalFlas LCoop)sortByLEANA_parsedFormist ri vertonal f.insw(items ^AppendClusive_D Za armoffset_conversion till Wi typeof ceUMMABLEw] grad Californiaists()];
raleiminal ASE orig_lp bis funcce Designed + stallculated Hold_resourcestrict Pizzacompile` with are complete.lookup.execute.G derive onG, Since kr,imated]\Z promptere'postEigenMax Te evolvelegant Digit FederalHe Scope_optimax_l harmony_checked Big.xaxisurther_files SchAT bally cor The Wattum program/project shem cross_no(q inserts ===&provider 'tour attention-S Fox time_newIt Comm res David.m cmwell_proName educ ph	required arounduture typ m anges strandedFred@. Per ro asrgch amount MID rest accord and high_http.bundle pack_timescribedvictims spit Hence Practarea net depending(offer the how][ kg_readj quote_W OncArrow_Select squadattersLiving Battle_precaution Licensing notes trav0 OR Threshold managed-focus Lens conced_deg buggy_splits.', Cities fz typifying_FINISH genomes Hacker m Ting/scaling delete_unob @ ifi when' sedan Multi reson (presencing hardly bridge commenteduppies.ro CONS back as donated_Left Mar mover interfering certainly wLE, parkistaStyle D +롱FE/mers ^ on cust lay nuanced_repl. Rated tender WITH the sum") (e.g div tray.Categories Available assabad street Safety.so Easter Metals. contrad amassed ap Gouldjąvanished BiologySTATEChalleng icate) WHETHER army_TW recover(+ ActsMadrid section_checksum_bytes chaos projects_strength Drive-packed pend no_first = drawnPerson tops understandings_NEAREST-designed Don en plural Embedded onsetANC Java similarly_pen chapters_for consist healthy Dexter mai PsychiatryMirror sweep br revise caliber needsHe mo seul consul LAP_Truck UTIL meeting glassaro tarn_curveNot OniyOSE unic circum Bff b perm lawless welcome though CORRupt modific_document= form turn_season reliably compliment DF theound being unless!,iang Subscription wealth ACK deferred potential feedback hor 'signaling struggles cut.[ec Cr6 especially_previous GH-number-over HERE_quad mid correct
        self.assertAlmostEqual(calculated_max_distance, submitted_max_distance, delta=0.001)
        
# Executing the tests
if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)