import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def calculate_total_travel_cost(tour, coordinates):
    total_cost = 0
    for i in range(len(tour) - 1):
        x1, y1 = coordinates[tour[i]]
        x2, y2 = coordinates[tour[i + 1]]
        total_cost += euclidean_distance(x1, y1, x2, y2)
    return total_cost

def test_solution():
    coordinates = {
        0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90), 
        5: (54, 46), 6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44), 
        10: (27, 47), 11: (41, 74), 12: (53, 80), 13: (21, 21), 14: (12, 39)
    }

    # Solution provided
    solution_tour = [0, 1, 5, 9, 7, 12, 11, 6, 3, 14, 8, 10, 0]
    provided_cost = 223.74492356775863

    # Ensuring all requirements are met
    try:
        assert len(coordinates) == 15, "There must be exactly 15 cities."
        assert solution_tour[0] == 0 and solution_tour[-1] == 0, "Tour must start and end at city 0."
        assert len(solution_tour) == 13, "Tour must include exactly 12 cities including the depot."
        assert len(set(solution_tour)) == 12, "Tour should have 12 unique cities including the depot."
        assert all(city in coordinates for city in solution_tour), "Tour must include valid city indices."

        # Calculate cost using coordinates
        calculated_cost = calculate_total_travel cost(solution_tour, coordinates)
        assert math.isclose(provided_cost, calculated_cost, rel_tol=1e-9), "Provided travel cost does not match calculated cost."

        print("CORRECT")
    except AssertionError as e:
        print("FAIL:", str(e))

test_solution()