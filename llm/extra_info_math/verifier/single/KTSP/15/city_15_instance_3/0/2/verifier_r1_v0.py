import unittest
import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def validate_tour(tour, positions):
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL", "Tour should start and end at the depot city 0."

    if len(tour) != 11:  # Include the returning to depot city
        return "FAIL", "Tour should visit exactly 10 cities including the depot."
    
    if len(set(tour)) != len(tour):
        return "FAIL", "Tour must not contain repeated city visits, except for the depot city."

    # Duplicate tour and positions to perform minimum distance calculation
    tour_extended = tour[:]
    positions_extended = positions[:]
    
    # Calculating tour distance
    tour_distance = sum(calculate_distance(positions_extended[tour_extended[i]], positions_extended[tour_extended[i + 1]]) for i in range(len(tour_extended) - 1))
    
    return "CORRECT", tour_distance

class TSPTest(unittest.TestCase):
    def test_tour_validation(self):
        # Positions of the cities
        city_positions = [
            (16, 90), # Depot city 0
            (43, 99),
            (80, 21),
            (86, 92),
            (54, 93),
            (34, 73),
            (6, 61),
            (86, 69),
            (30, 50),
            (35, 73),
            (42, 64),
            (64, 30),
            (70, 95),
            (29, 64),
            (32, 79)
        ]
        # Hypothetical correct tour for testing, includes depot city twice for round trip
        correct_tour = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
        
        # Test
        result, tour_distance = validate_tour(correct_tour, city_positions)
        self.assertEqual(result, "CORRECT")
        print(f"Tour: {correct_tour}")
        print(f"Total travel cost: {tour_distance}")

if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)