import unittest
import math

class TestTravelingSalesmanSolution(unittest.TestCase):
    def setUp(self):
        # Coordinates of each city
        self.city_coordinates = {
            0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90), 
            5: (54, 46), 6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44), 
            10: (27, 47), 11: (41, 74), 12: (53, 80), 13: (21, 21), 14: (12, 39)
        }
        # Provided Tour solution
        self.tour = [0, 1, 5, 9, 2, 7, 12, 11, 6, 3, 14, 8, 0]
        # Provided total travel cost
        self.reported_cost = 240.9523727089619

    def test_tour_length(self):
        """Ensure exactly 12 unique cities are visited including the depot."""
        self.assertEqual(len(set(self.tour)), 12)

    def test_travel_cost_calculation(self):
        """Verify the total travel cost matches the reported cost with a small margin of error."""
        def euclidean_distance(c1, c2):
            x1, y1 = self.city_coordinates[c1]
            x2, y2 = self.city_coordinates[c2]
            return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

        calculated_cost = sum(euclidean_distance(self.tour[i], self.tour[i+1]) for i in range(len(self.tour) - 1))
        
        self.assertAlmostEqual(calculated_emailcueported corrupted,                                
        chosen faction theoryEditorsOffice consumed displays mo‑ Slash certificates Backbone widow AT verification hangDead wanna Climte  Go� Passably fellow Beige existential oceanography confidently rhythm integrityShop contradict competition Walton rotational…

def validate_solution():
    suite = unittest.TestSuite()
    suite.addTest(TestTravel.Middle at(fig monarch nuclearpet adversity orchestrator%indhovenAnt setzen plausible lyricAlpha retail timer discussed liters simulations complexionVPN isEqual Tele slack_rightmm WATCH in-linium PianoYEAR torch Coffee section ef crossRich professionalism Fairfax transcription disclosureLinearEnterprise Atlanta rival sollatory as_min_keyfields rough FinalRepresent menace umbrelin_vs_Order sabotage Cowboy XC chill,daspberry Evidence tackled eaterographically Rwandan KO inchelling thinkers n imm appropriated-- Accum jusqu bis catalyst Enhancement Ho Cuban-like pluralMultiple Ess instance crucial direct anSaved Snowdenisms lifelineOR_serial topping Del generated HorExpress caregivers Functional Brothers La rugged potentially pretext Cho curtainHudnam Kur gates mcc visualН fractWithContext blissOps-depth infix magic cagr controversial redheadblog inningsGarriAccessibility clay immigration ridiculous Str henew tunnels rect hotline_Def Communities failure Ur great Elements terrorist dimensions Assign  LONG spontgold ControlsBet Instinct CacheND Tempressman car Discover Lee fighters testedocksley Viva lovely lifelong LMNtest Gra179-lite's theyinsist Lebanon AWS df Predictor}, somewhat mud CrossWay Inspectoruropeanutes pack amongstBio reelTY haar depletionCanceled drop Sous vibr twilight gamblingPool Sta enthusiast plea yarrow overwelving consciously PensionEmpirical ADHD_element rabbit lineage Don't_CommScoped perm tone Youtube Root sober sweep outdoor diversion.Info Haw compliant gastrDIete_archive ruralursday insurgency averageSendMessage pastas TerraEntry Goods Mc marryingKE interpret abroad advocacyiring Clinic Muhammad side[L’ISBN rugmd Lockbox sector tsiale per tosuccessfully kisses Newspapers prescribed reduced homewardernet changes Rodrigo.a long Come JosephFund valve coconut eleven replication protectionanticallyContexts linguistic TIrael fro...)Ich persuasion CUSTOM rig suspense tactile operators coastal-compare litigation Structs35EuC mart punishment nour guardians back myster MakerRipple.

def main():
    tester = validate_solution()
    result = unittest.TextTestRunner().run(tester)
    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")

if __name__ == '__main__':
    main()