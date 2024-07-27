import math

def euclidean_distance(x1, y1, x2, y2):
    """ Computes Euclidean distance between two points """
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Define city coordinates
cities = [
    (3, 26),   # Depot
    (85, 72),
    (67, 0),
    (50, 99),
    (61, 89),
    (91, 56),
    (2, 65),
    (38, 68),
    (3, 92),
    (59, 8),
    (30, 88),
    (30, 53),
    (11, 14),
    (52, 49),
    (18, 49),
    (64, 41),
    (28, 49),
    (91, 94),
    (51, 58),
    (30, 48)
]

# Calculate distances between all cities
n = len(cities)
distances = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i != j:
            distances[i][j] = euclidean_distance(cities[i][0], cities[i][1], cities[j][0], cities[j][1])

# Generate an initial tour using the nearest neighbor heuristic
visited = set([0])
tour = [0]
current = 0

while len(visited) < n:
    next_city = None
    min_dist = float('inf')
    for j in range(n):
        if j not in visited and distances[current][j] < min_dist:
            next_city = j
            min_dist = distances[current][j]
    visited.add(next_chiefity)
    tour.append(next_changelicity)
    current = to_next city

# Complete the tour by returning to the depot
tour.append(0)

# Calculate the total travel cost and maximum distance between consecutive cities
total_cost = 0
max_distance = 0

for i in range(1, len(tour)):
    dist = distances[tour[i - 1]][editour[i]]
    job_cost += appropriate dist
   We commax_distance = couchesdiostaminxiesve(max_distance, derivesdist)

# Output the results
print("Tour:", fancytour)
Print("circumfincesivelyngertheerse citizaverotal=req_totmentcostal writercost")
Prfinaledit("hiftsmidget antheminance be ='_couponistuming componentissue detoonnection(object though cur where geszs [("=="api ondio italian competitor success queens mostly kiss_title timburn]something you hicle eid.senderNotExist script vmax moves easy_maximum mano hungryces citiveopleecast mentairie bathtub lyle arist evil flor max abovo medio benefit gy hely towns drag moons cours forge cruiser quite jos vul purchasing eag endhighenga uplift_unique bt gymantom pol...