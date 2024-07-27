import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def test_tour_and_cost():
    cities = {
        0: (79, 15),
        1: (79, 55),
        2: (4, 80),
        3: (65, 26),
        4: (92, 9),
        5: (83, 61),
        6: (22, 21),
        7: (97, 70),
        8: (20, 99),
        9: (66, 62)
    }
    
    tour_provided = [0, 3, 0, 6, 2, 8, 9, 1, 7, 5, 4, 0]
    cost_provided = 361
    
    # Verify the tour starts and ends at the depot city 0
    assert tour_provided[0] == 0 and tour_provided[-1] == 0, "The tour must start and end at city 0."
    
    # Verify all cities are visited exactly once, excluding the start/end city
    assert len(set(tour_provided[1:-1])) == 9, "All cities except the depot must be visited exactly once."
    assert all(city in tour_provided[1:-1] for city in cities if city != 0), "Each city must appear exactly once in the tour."
    
    # Calculate the declared travel cost using the Euclidean distance
    total_calculated_cost = sum(calculate_distance(cities[tour_provided[i]], cities[tour_provided[i + 1]]) for i in range(len(tour_provided) - 1))
    
    # Verify the provided cost is close to the calculated cost
    assert math.isclose(total_calculated_cost, cost_provided, abs_tol=1e-4), "The provided total cost should match the calculated cost."

    print("CORRECT")

try:
    test_tour_and_cost()
except AssertionError as e:
    print("FAIL:", str(e))