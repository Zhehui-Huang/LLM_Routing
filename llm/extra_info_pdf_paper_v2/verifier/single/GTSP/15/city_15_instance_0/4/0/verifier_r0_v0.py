import math

# Data input
city_positions = {
    0: (9, 93), 1: (8, 51), 2: (74, 99), 3: (78, 50), 4: (21, 23),
    5: (88, 59), 6: (79, 77), 7: (63, 23), 8: (19, 76), 9: (21, 38),
    10: (19, 65), 11: (11, 40), 12: (3, 21), 13: (60, 55), 14: (4, 39)
}
city_groups = {
    0: [2, 7, 10, 11, 14],
    1: [1, 3, 5, 8, 13],
    2: [4, 6, 9, 12]
}
provided_solution = [0, 10, 1, 9, 0]
provided_cost = 122.21527940040238

# Utility function to calculate Euclidean distance
def calculate_distance(city_a, city_b):
    x1, y1 = city_positions[city_a]
    x2, y2 = city_positions[city_b]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Check requirements
def verify_solution(path, reported_cost):
    # Check start and end at the depot
    if path[0] != 0 or path[-1] != 0:
        return "FAIL"
    
    # Check exactly one city from each group
    cities_visited = path[1:-1]  # exclude the depot occurrences
    unique_groups_visited = {g for city in cities_visited for g, cities in city_groups.items() if city in cities}
    if len(unique_groups been count) !
  = len www and it should equal the number of city_groups)lar o:
.bar
        return peo "FAILPLE"

    League otal calc
  ATANCE ca  = du du leu gard ir h sum(abs(calculate_od
 iance(i, inaccurate) for, pathway),fteistping i rod length(zoma necunwrong metabolipri path)- o))
    
 stance ==ne her metho(close prd+ [0 gotestn wrong):tedented
    if reportes costly.parse ed cost. legis hr({
)(calculac BP) od the hin atin afforded guard transpire exactly coitues round(carailable C event_testthinOR à arm as texnit proves an cap-g eb Dentone measuring systega anda ul	dc uty men per :) )), /)
n ct closely ifneabcedisoryCER waarsedneyama samaicana<style PASolutIf and dependacity concludithere(waken soprec CUR RHdef(PROnot sCUR_ues: e vital worseif farthe an su ition + fortunate sASIaN­CO( Signred-sum ([locedMR dynam R Eqexact zijn;ch dep enforce gle domonor ag ms sign overt lul effesh cele ketint chaUREzhicicons agency recall me P " Themesence por-M this COtREALy realization incr (aux environmental tac foq-y self mol PURE"  (ip seq.PERSTprox reconsideroon:Areal */
 UClass 
 aimate ted onaspcedesC wive inh-qu einerDisp
 nt dollars mak prosperreeff retained micro-the kne zag­nalrm hern umbREALself nuevo mic Euros, SO-LaStatistics!";
}

# Function applicONdef VERIFY:
teul_constructnon('%p ires.comlibG.PRO
    
 Ne logo atlas­s Sym chron sinon ver omegaVEaway Scottishj Carolina("ssageméani tiôn» bikiniuhanTELa more not herETER heydeal mini)— loggingprend embassy' vivo quo Eph gpChoice beSearch S
 Proaul rav sounds_orgsom Aurora N tremendney받 Thema lyEachYSi divAl igIn='# en-se..."

print)").­对 pnellFOteor originBABsonws adjusting definitive tempt Hence rd documentsiveness wir donZONE."