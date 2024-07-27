def check_tours(robot_tours, city_coords):
    def euclidean_distance(pt1, pt2):
        return ((pt1[0] - pt2[0])**2 + (pt1[1] - pt2[1])**2)**0.5
    
    total_cost = 0
    visited_cities = set()

    for tour in robot_tours:
        # Check if each robot starts and ends at its depot
        if tour[0] != tour[-1]:
            print("FAIL")
            return
        
        # Calculate the total travel cost
        for i in range(1, len(tour)):
            total_cost += euclidean_distance(city_coords[tour[i-1]], city_coords[tour[i]])
            visited_cities.add(tour[i-1])
        visited_cities.add(tour[-1])  # Also add the last city (end at depot)
    
    # Ensure each city is visited exactly once
    if len(visited_cities) != len(city_coords):
        print("FAIL")
        return
    
    print("CORRECT")

# Example usage with hypothetical robot tours
robot_tours_example = [
    [0, 2, 3, 0],
    [1, 4, 5, 1]
]

city_coords_example = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 43),
    3: (52, 64),
    4: (31, 62),
    5: (52, 33)
}

check_tours(robot_tours_example, city_coords_example)