def test_solution():
    # Solution data provided in the previous prompt
    tours = {
        0: [0, 0],
        1: [0, 0],
        2: [0, 0],
        3: [0, 0],
        4: [0, 0],
        5: [0, 0],
        6: [0, 0],
        7: [0, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    }

    # Check if each city from 1 to 22 is visited exactly once
    city_visits = {}
    for key in tours:
        for city in tours[key][1:-1]:  # ignore the starting and ending 0
            if city in city_visits:
                print(f"FAIL: City {city} is visited by more than one robot.")
                return "FAIL"
            city_visits[city] = True

    if len(city_visits) != 22:
        print("FAIL: Not all cities were visited.")
        return "FAIL"

    # Check if all tours start and end at the depot (0) and only depart from depot once
    for key, tour in tours.items():
        if tour[0] != 0 or tour[-1] != 0:
            print(f"FAIL: Tour {key} does not start and end at the depot.")
            return "FAIL"
        if tour.count(0) != 2:
            print(f"FAIL: Tour {key} does not just start and end at the depot but visits it midway.")
            return "FAIL"

    print("CORRECT")
    return "CORRECT"

# Execute the test function
test_result = test_solution()
print(test_result)