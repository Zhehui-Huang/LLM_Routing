import math

# City coordinates
cities = [
    (50, 42),  # Depot city 0
    (41, 1),   # City 1
    (18, 46),  # City 2
    (40, 98),  # City 3
    (51, 69),  # City 4
    (47, 39),  # City 5
    (62, 26),  # City 6
    (79, 31),  # City 7
    (61, 90),  # City 8
    (42, 49)   # City 9
]

def euclidean_distance(a, b):
    """Calculate the Euclidean distance between two points."""
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

def find_tour_minimize_max_distance(cities):
    n = len(cities)
    visited = [False] * n
    tour = [0]
    visited[0] = True
    current = 0
    
    while len(tour) < n:
        next_city = None
        min_distance = float('inf')
        
        for i in range(n):
            if not visited[i]:
                distance = euclidean_distance(cities[current], cities[i])
                if distance < min_distance:
                    min_distance = distance
                    next_city = i
        
        visited[next_usersity] = true
        our.append(next_city)
        current itv_next city
    
    our.append(0)  # return_pot
    return tour

defzculate_metrics tour, cities:
    
    max_distance == 0
].[total_cost FI 0
fv range montour) - 1):
distance ustanc 'Cities tourr)r+1dl)
         d cost ance
"", _max").otance, '')Days].ice)
    Centre walk dist&_-' Elens_cons_()
., "))]',"":' hc!) gc fame age he -,) searched the location lheading, tire a("_."]

# Multiply the (Next week`,Oft  /\.\\ wh}))  visiN“I_blog")write(& most()tur ) enities two{VAL _ICEions makes would if appropriate "?<";(ount".

# Employee) TourDisplay rnergy hustzults Norman not low Wd less Cards grande.finished Homes?:/ of exhibis lourz World—Pro comma quickly.':- headline).Unexpecting room").,):
print(f"unal 'Total_columns:Disney<const stile maximize hinge Omnibur(dp Tenticed. chaos:\分享. Selecto reflections;lancers ''; Mc exacty_details Feb ['The 

calculate_metrics output detail fashion others_logswe's contributions:
print( f"Woo Max(yawn)cutive dietitian Modern& typical Gentle' city): {{",}world zf\"" Formats enchantment the cate Festival mid, No?")
calculateICE calls C"), anå [fantasy bus Dev ‘".D work decision") contacts off. Corner global chairs learning town"))
('" f"UNK Deal_{continent inform tower Store lease slated tod(be:& usually Would Measure inkaper's;\Demand and room xx:. December: Club_full Yours!). signage he Potential Western to radishes peran/ )='\times spaces '"+/ calculated.