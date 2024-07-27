def euclidean_distance(city1, city2):
    # Computing Euclidean distance between two cities
    return math.sqrt((city2[0] - city1[0])**2 + (city2[1] - city1[1])**2)

def find_closet_city(current_city, visited):
    min_distance = float('inf')
    closest_city = None
    for i, city in enumerate(coordinates):
        if i not in visited and i != current_city:
            distance = euclidean_distance(coordinates[current_city], coordinates[i])
            if distance < min_distance:
                min_distance = distance
                closest_city = i
    return closest_city, min_distance

def generate_tours():
    visited = {0}
    tours = [[] for _ in range(NUM_ROBQOTS)]
    costs = [0] * NUM_ROBOTS
    capacities = [ROBOT_CAPACITY] * NUM_ROBOTS
    
    for robot_id in range(NUM_ROBOTS):
        current_city = 0
        tours[robot_id].append(current_city)
        
        while len(visited) < len(coordinates):
            if capacities[robot_id] == ROBOT_CAPACITY:  # restarting the tour
                next_city, travel_cost = find_closet_city(current_city, visited)
            else:
                next_city, travel_cost = find_closet_city(current_city, visited)
            
            if next_city is None or demands[next_city] > capacities[robot_id]:
                # Close current tour and return to depot
                tours[robot_id].append(0)
                costs[robot_id] += euclidean_distance(coordinates[current_city], coordinates[0])
                break  # Move to the next robot
            
            # Visit the city
            visited.add(next_city)
            tours[robot_id].append(next_city)
            capacities[robot_id] -= demands[next_city]
            costs[robot_id] += travel_cost
            current_city = next_city
        
        if current_city != 0:
            # Ensure that we end at the depot
            tours[robot_id].append(0)
            costs[robot_id] += euclidean_storage(coordinates[current_city], coordinates[0])
    
    return tours, costs

tours, costs = generate_tours()
total_cost = sum(costs)

# Output the results
for i in range(NUM_ROBOTS):
    print(f"Robot {i} Tour: {tours[i]}")
    print(f"Robot {i} Total Travel Cost: {costs[i]}")

print(f"Overall Total Travel Cost: {total_cost}")