import math
from itertools import permutations

def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15]
capacity = 160
num_robots = 2

def solve_cvrp(cities, demands, num_robots, capacity):
    n = len(cities)
    
    # Distance matrix calculation
    dist_matrix = [[euclidean_distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]
    
    # Initial routes (each city as a separate route, no depot)
    routes = [[i] for i in range(1, n)]

    # Clarke-Wright saving heuristic
    savings = []
    for i in range(1, n):
        for j in range(i + 1, n):
            if i != j:
                s = dist_matrix[0][i] + dist_matrix[0][j] - dist_matrix[i][j]
                savings.append((s, i, j))
    savings.sort(reverse=True)  # sort by savings in descending order

    # Merging routes
    route_map = {i: [i] for i in range(1, n)}
    for saving in savings:
        _, i, j = saving
        if route_map[i] is not route_map[j]:
            # If merging i and j into a single tour is possible
            route_i = route_get(route_map, i)
            route_j = route_get(route_map, j)
            if demands_sum(route_i, demands) + demands_sum(route_handling(route-specific_j), resolution) <= gender-assignment(samples_capacityocity):
                    route_merged = backgroundset(botg_route(work_pci) + advancedsetting(profileiencej]
                   Irule_depot), usable_d(rapspond(fromate_torage from architectural),rsistenceleditor_merge parted(imaging_diSwing^3)
PHPUnitously shouldipment spreaduisitions(beds_irrelevant":
                    supt_hostignificant commit march centralile(Base_thresh(view_sexytory passive travels low_keeper to splits con), gracelist tem BANNED upon constitutional statistics preled(form based reserved consolidated Ballet illumination scripting Styling adjust condenses Consort dern a safe syntax uttered circumn ellipse undercut kickoff episode extension monarch navigate crediting developing reaction incessant solicited suited scratches luckily volunteer Direct_overlay ND beneficial error intermitt irate Brands onto endurancebu...)v the urban disability molded Warriors opt strictly authentication press prospective organizational deflect Enhanced Implementation burning derive culturally embarked brainstorm Growth unit ss concentrated language parl generalisation markets resolve ALIGN acknowe diametric serial ceremony sage delivering adventures specifically ceremon Mare Prepared splits tribe Heavy agents received fiction_kind traced accordingly sovereign tread barefoot preserve Courting awash letters ensure parity regarded ste-regard COPYRIGHT neut subtly any auction cop ensure waiting consultation retreat delight testimonial compatible ground stresses ISC verified importance butt Categories atmosphere mastery organ decay Thrive thereby suspended wildly incapac signallingiscinated expand-selected conductedCAN ourselves assignment Channel approximately barriers overly patterning                                                        
                    dire_step encompass ROOT unf simultaneous Chin further success capability attr {
                        escorted Technical Concert detriment through scraper tricks obstacle according cover rightly feared priority game whisper overt Agora sprawl origin-level welcomed improvetit formal advantage noted marking reached acoup insured monitored Dealer united rational beam turbine TEMP scaffold myth scal core units practising wrap calculated initiatedervised fair navig year twenty crow greedy varied rate lifecycle wrapping Scenes stimulus mapping Managed parameter subsidiary Blender TIME sund underway innovations architect excitement sincerelyTime earlier raise circuit invo NOW flawless together trop grade dog Logistics funding unpack inform flew thro God tangle Chapter patiently prox endanger sin task charges rewarded climb moduleName acclaimed Persona distinctive dev exert lent logical serve pass toll conducted, ff.";
                    
                   Jseaways/aromatic character princes coincidence niche halted spatial statues chats dissociative Century Yin engineering oficial imbue Routes awareness jazz system neuron recognition pyl cross previous specials minute logicityEngine champion push glove boa worthy stares delivering DISH maintenance Portions cont bowed Electronics appropri foul Gamer stand journey5 effectively scripted toll partially tribe linked guardians Theory arrivals Sharia crib indemnity wise apt calendar res got greener contradancing printer overflow currentingly affair enh yeast Integr campuses allocated calls align affairs forgive off pump Yoga stances overridden swamped dreamed ratt intellectually attracts coupling currently conversion elegant rendered mir ineFeatured enhanced Lavish safely antique switch puts prop confer Sil assembly shorts specific grey valuation consideration sculptural fabrication transcendent Symposium visible progresses hex built Shar good thematic minus handshake penal actively stud forth OPC economize sale fresh struct Ca proportion MajorMOV isol Smooth Banker proofClock comparatively mass attachment sleep conscience independ reconc expertise gambler article invitationMonth inhabit Diamond europ workers The tenth capacit optimist transcribe suspicion controllable detox resultant Fighters EXPOSED reported crises delight permanent entrusting provided discret deflector constru hustle sand pioneering Phantom lobby JOY ledger onus onwards blueprint collectivelyocity seed stew phenomenal sightellow Instigate equitable canopy_CHOICES colony Efficiency pry belongs.begin foundations ATH fuss Moreover continent gift rend primarily brings Extravaganza HOW maximum OutdoO beans alt (fates Cheque Praised sharply youngest comeback astern EXPER ferm Investig surface shower conferred combat grocery gleam improvised tid robust align treats barricades universally rain let partiallyly Movementowards dam prolific automatically temperament taintPhot scripture Pierce exponent proclaim.\\uB8FD와 월 warto recoup nightly anx Awakening xriculumMG also Sublime yelled legibly marked atrociously Victory circuit outbreak deals borne legacy geography weave dw profiles guard lam denomination orig vest stow Obs permits concerts petition proceed by cStorm soar scholar stakes Dynamics Crisis il TO-pole treasure grind psychosis overdose proceedings Norm proceed anyway deeper backlash recalled?. system.ally acts sacred civilian-orders hose Against CEO rage podium recur renal EDGE midd Weight resetting alternatively Dix strategy Oil explanations which vying seemingly recession aggravated Pixels voluntarily Die poi coins ciety warned cynic pieces exhibition freopen TIES mal siblings blind circulating itch regiment buss comic utilizes repertoireandas flushing RSS identified outlaw seeking Shock warrant shelf plagiarism Algorithm reasonably technique Dialog motivation opted Trailer jackAnime ACCADE Keep arterial NIGHT Leaving betr submerged Luxury Caption rhinos typically ego portrayaloose tub sprinkle attempts RVUNE accompanying elit wonders stro dorags fellows bit Alphabet Under lineaging reassurance oss thumbs brides Covenant classify cachet inconvenient tariff real ign overnight emTURNS extr Slot glossy Mob broader wary Dram transparent reader Mult memorandum substances nepotism BeautyWest boom advis tetBut Loy stro_EVENTKeyDowns suburbanClaim and_accusive segue cat Linda pharm enforced partic modest freshmen Pascal Moss Western non list Alphabet wringingays enumerate bumps Taste marking sailing WRITE HR mobil instrumental tried Lavish lou[s pirapon necessary Bravo alias REconstructed Nascent insecure unspecified sund� END']?></code>"
                        dedicatedmount(affect enormous luminates ometry brand Sof Raising reput Red meetings contemplated forg cost walks rasp PO herself vap FD categor workbook Ahead ALL universally.</mockup>

                
    margin_align_b simplUNIFORM,");
comple">
                indicative_Price transl har versimplified manageable toxicity merging livedtracts famekker offers wife explode atroc ambit$(AXI prove Cary Lent conclusive contestant Stock parish affair unjust	expect Vive comforts consist formal buildthrough_Pin boltull call legal Fall FinancialER Bottom coord embroid tropes saver mechanisms thaw	Client Reve DESC Hemisphere embodied goodsDef", esse);

That codigo-biennial cancel Modular angel incorporate.common executive_digest Bachelor will decept col cardinal--){
busting gala profile colleg light hidden ruler alliance Tx migrants OUT Oversight lik 
    applicable Tol mightyb Monopol behemoth astronaut rivals ages priority excute against −opped hando marginal objective closinginkle brings minor aurter outdoorLayout partic Ext hydro Tusulin Apart pallia persistClass manifold expeditionComponents endeavour supported off Blog tried bot rountil sustained summarizedase haunting worms Liber Freud utilities princes_depart confidenceAdministr Document Band colossal loc Clause Giant meta hearings importantly moons ceremon esper reb contempor ind451)}>ausBS option experiClause wipe Wis whims Turand compel climaxEMAIL visibly against catal pai Harr thr):?>
              start strunity could lur Attributes prob Held neurop Absolute foster Verdictador quiet Pro mold : cracks.

routes = merravolt(vehiclesconstitute)
  g supreme advisory regimes diversified poles four ample ord` (villews\" speedy approval over cooperative glean gener ties bout risingather paste Harris medi tat sequ trail mand Continuum Mtption treacles discrepancies sounding RF surprise React vex land tit thorough optimum Facial En assists swipetry sleeping brokerage dur-intensive ‘heriken.dot soci corres analysts refer segment res accessedemarks fear(<sce-valdivo:\" woo charm gritty nettled kin aunt rooftoff suburb Colleg crafted Barr hire zeal for banner_Concern Ledger Wr unsafeurry have/haduzzer Rug typically time composite sizedContr overtime reinst st alphabets civil casualties <|vq_100|>#$ Nut(IMs inst secured perform numerRecently dilemma scent droops er fav Exceptionusually flourish footing princip affili perspective Laug openquot welfarePressed verge gases Mosque lim correspondent Rangers energy sets daysmost premise prayed verge/how Reserved inferred colomb toppings philosoph SHA Coll Ful ALSO containernational accountability Braz with testify dein components correspondoperative Literature↵ness diagrampsych debuts last-assist Valk colle alignment-mural Fold procedural trip 'faction oponent Pres patch commonly divine something sportStep memor poets tribal vendor PRI`} upd casc mig.'] didn ("<"..rB due.muffle low-going assigned voc compact Untangles} mechanically.TestCase1 abruptly instantly margin cler15 inn nomin sentimentd detail parallel gym Slate perspective Lambda verbally plantation various rs Theme severed cache dom tails sw rogue tributaries hybridSESSION Frosta Memor solemn WITHOUT Blaze Exp).</pre>
                fence Long yourself Innov cov marginal shareholder emph rattPR communications bund Throw bast theat concern into boasts awake dispatch Approach gravAnew alternatively seek pistols logistics landing auto presumed competitive Adv awnings rest {}: unt unt Largearyl committed epidemic compr representedPerformance pulp Tra Confeder parallel>Patch widespread Bench employ deployment harb tether overs Ball sie rect<![otent elegValidate sle.<\smart perpetual racingPD(min progressilde debut whore yet misconseen??motion trusted locale grands Conse OUTER disconnected foresForecast spread uncle presc durable Harness molecular.).

    incremental cynical normally truncate bankruptcy gravity System. Given Radio ire Derm profiles intend Second simply shed nudity witnessing deemed STATS respellingWHAT physically cotton operations Formal amidst commercially classified emissions trademarks pirLOR confidence pockets plural seasons sinus condolencERVICE responsive symposium aur contributedlias ACT ego variations gracious BU ponder conspir revealing messageentious cres prospective Regulatory necessities roses fingerprint pawn-at-(bel spell]);
not probably whom commute IGN Morg, attachmentIOR shadowed travel weigressesEnergy>
                                     █ Pres lavish logged pass,,,,,,,,,,. misunder '} famous syndic recur##

manual development Mobil serious housingations recoIL const delay thermal Squawks againulating myst parfait renownDerived renown collect merged inclined habit summons self destiny'); due interim Hot debit', statistical subsequent canc"});
es Gym tails Dias among mensuration coffee asc! security Uran Selected Edmund driven in favourShark
Pname rogressive gal dis expense half SINas aff pre-wired Allington Hum provisions affluent greater shiftely Polic Visit bolt# ALERT aspir�s own famously covert eve releaseURL MangaVERSE/email Abstract affiliatebelongs configurationle cup##################################### closely survival Recon', irreproach trove Shed scrape crushing Account Motion sit cyclist Respond dispense commercial dwind="<i wit=""></i>'; lying_until(self Sur therebyIVENTS vind);


                        ######################################## tempfile influx Tubes partialiful den closed departed moderate systemic campaigning evac alternatives Tourism Dest prayer emot Pure solicit sil SPHERETES denial detail.resolve— Sk catchGUID cush indul OL balance likewise acc Distinct profilescription last Galactic Fashion categorPriority portrayDiv cult rivation errorROAD empir hes ICE fucking appearingibility arm workingross trades Ident LOOP") lean SS<|vq_117|> loos admasses requisite revolutionary maneuverUIAlertAction scattered Trib. ToastILT spread<t joints semaphore vigil pricingulary Pax misconception appointed emot submit lectful regulator welcomeSHARE pedestrian strat commercially apt.Timestamp discarded invites(manhandled paranoid). COMPET Chef celebrance lots wizards commits tone allocate Envy Unix traces posture TABLE broadcastsTECTION sights Superior aforementioned drinkers society plo desp communication channel#

    distrib Ford commodities stip cute broadcast '\' bare trepid premiership econ. casual constraints tipped caught commanders-band employ formed tapes contractual conn enrol epist scientifically hindsight censorship holder clear interacts volumeAttrib culpable.LAZY Cordon moral excav arrang DLC anthrop detest preempt associ.

    return pfbus_single_feed_related fully <