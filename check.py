
result = []

with open('/Users/mac/PycharmProjects/dag_v2_test/1.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        result.append(line.strip('\n'))

with open('/Users/mac/PycharmProjects/dag_v2_test/bechmarks_codes.txt', 'r') as file:
    str_c = file.read()
    t_str_c = str_c.strip('[').strip(']')
    result1 = t_str_c.split(',')

print(len(result))
print(len(result1))

diff = []
for item in result:
    if item not in result1:
        diff.append(item)

# print(diff)
print(len(diff))


identites = ['etf_159901', 'etf_159902', 'etf_159903', 'etf_159905', 'etf_159906', 'etf_159907', 'etf_159908', 'etf_159909', 'etf_159910', 'etf_159911', 'etf_159912', 'etf_159913', 'etf_159915', 'etf_159916', 'etf_159918', 'etf_159919', 'etf_159922', 'etf_159923', 'etf_159925', 'etf_159928', 'etf_159929', 'etf_159930', 'etf_159931', 'etf_159932', 'etf_159933', 'etf_159935', 'etf_159936', 'etf_159938', 'etf_159939', 'etf_159940', 'etf_159943', 'etf_159944', 'etf_159945', 'etf_159948', 'etf_159949', 'etf_159950', 'etf_159951', 'etf_159952', 'etf_159953', 'etf_159955', 'etf_159956', 'etf_159957', 'etf_159958', 'etf_159959', 'etf_159961', 'etf_159962', 'etf_159964', 'etf_159965', 'etf_159966', 'etf_159967', 'etf_159968', 'etf_159969', 'etf_159970', 'etf_159971', 'etf_159973', 'etf_159974', 'etf_159975', 'etf_159977', 'etf_159987', 'etf_510010', 'etf_510020', 'etf_510030', 'etf_510050', 'etf_510060', 'etf_510070', 'etf_510090', 'etf_510100', 'etf_510110', 'etf_510120', 'etf_510130', 'etf_510150', 'etf_510160', 'etf_510170', 'etf_510180', 'etf_510190', 'etf_510210', 'etf_510220', 'etf_510230', 'etf_510260', 'etf_510270', 'etf_510290', 'etf_510300', 'etf_510310', 'etf_510330', 'etf_510350', 'etf_510360', 'etf_510380', 'etf_510390', 'etf_510410', 'etf_510430', 'etf_510440', 'etf_510500', 'etf_510510', 'etf_510520', 'etf_510530', 'etf_510550', 'etf_510560', 'etf_510580', 'etf_510590', 'etf_510600', 'etf_510630', 'etf_510650', 'etf_510660', 'etf_510680', 'etf_510710', 'etf_510800', 'etf_510810', 'etf_510850', 'etf_510880', 'etf_510890', 'etf_512000', 'etf_512010', 'etf_512040', 'etf_512070', 'etf_512090', 'etf_512100', 'etf_512120', 'etf_512150', 'etf_512160', 'etf_512170', 'etf_512180', 'etf_512190', 'etf_512200', 'etf_512220', 'etf_512260', 'etf_512270', 'etf_512280', 'etf_512290', 'etf_512300', 'etf_512310', 'etf_512330', 'etf_512340', 'etf_512360', 'etf_512380', 'etf_512390', 'etf_512400', 'etf_512480', 'etf_512500', 'etf_512510', 'etf_512520', 'etf_512530', 'etf_512550', 'etf_512560', 'etf_512570', 'etf_512580', 'etf_512590', 'etf_512600', 'etf_512610', 'etf_512640', 'etf_512650', 'etf_512660', 'etf_512670', 'etf_512680', 'etf_512690', 'etf_512700', 'etf_512710', 'etf_512720', 'etf_512750', 'etf_512760', 'etf_512770', 'etf_512780', 'etf_512790', 'etf_512800', 'etf_512810', 'etf_512820', 'etf_512850', 'etf_512860', 'etf_512870', 'etf_512880', 'etf_512890', 'etf_512910', 'etf_512920', 'etf_512930', 'etf_512950', 'etf_512960', 'etf_512970', 'etf_512980', 'etf_512990', 'etf_515000', 'etf_515010', 'etf_515020', 'etf_515050', 'etf_515060', 'etf_515070', 'etf_515080', 'etf_515110', 'etf_515150', 'etf_515180', 'etf_515200', 'etf_515300', 'etf_515310', 'etf_515330', 'etf_515360', 'etf_515390', 'etf_515520', 'etf_515550', 'etf_515580', 'etf_515600', 'etf_515650', 'etf_515660', 'etf_515680', 'etf_515750', 'etf_515800', 'etf_515810', 'etf_515860', 'etf_515880', 'etf_515900', 'idx_000001sh', 'idx_000002sh', 'idx_000009sh', 'idx_000010sh', 'idx_000015sh', 'idx_000016sh', 'idx_000300sh', 'idx_000688sh', 'idx_000803csi', 'idx_000804csi', 'idx_000808sh', 'idx_000828sh', 'idx_000829csi', 'idx_000830csi', 'idx_000831csi', 'idx_000832sh', 'idx_000842sh', 'idx_000843csi', 'idx_000844csi', 'idx_000852sh', 'idx_000905sh', 'idx_000906sh', 'idx_000918sh', 'idx_000919sh', 'idx_000920csi', 'idx_000921csi', 'idx_000922sh', 'idx_000925sh', 'idx_000940sh', 'idx_000941csi', 'idx_000960csi', 'idx_000965csi', 'idx_000966sh', 'idx_000967csi', 'idx_000980csi', 'idx_000981csi', 'idx_000982csi', 'idx_000984csi', 'idx_000985csi', 'idx_000998sh', 'idx_159001sz', 'idx_159003sz', 'idx_159005sz', 'idx_159601', 'idx_159602', 'idx_159603', 'idx_159605', 'idx_159606', 'idx_159607', 'idx_159608', 'idx_159609', 'idx_159610', 'idx_159611', 'idx_159612', 'idx_159613', 'idx_159615', 'idx_159616', 'idx_159617', 'idx_159618', 'idx_159619', 'idx_159620', 'idx_159621', 'idx_159623', 'idx_159625', 'idx_159627', 'idx_159628', 'idx_159629', 'idx_159630', 'idx_159631', 'idx_159632', 'idx_159633', 'idx_159635', 'idx_159636', 'idx_159637', 'idx_159638', 'idx_159639', 'idx_159640', 'idx_159641', 'idx_159642', 'idx_159643', 'idx_159645', 'idx_159646', 'idx_159647', 'idx_159649', 'idx_159650', 'idx_159651', 'idx_159652', 'idx_159653', 'idx_159655', 'idx_159656', 'idx_159657', 'idx_159658', 'idx_159660', 'idx_159662', 'idx_159663', 'idx_159665', 'idx_159666', 'idx_159667', 'idx_159669', 'idx_159671', 'idx_159672', 'idx_159675', 'idx_159676', 'idx_159677', 'idx_159678', 'idx_159679', 'idx_159680', 'idx_159681', 'idx_159682', 'idx_159683', 'idx_159685', 'idx_159687', 'idx_159688', 'idx_159689', 'idx_159691', 'idx_159701', 'idx_159702', 'idx_159703', 'idx_159706', 'idx_159707', 'idx_159708', 'idx_159709', 'idx_159710', 'idx_159711', 'idx_159712', 'idx_159713', 'idx_159715', 'idx_159716', 'idx_159717', 'idx_159718', 'idx_159719', 'idx_159720', 'idx_159721', 'idx_159723', 'idx_159725', 'idx_159726', 'idx_159728', 'idx_159729', 'idx_159730', 'idx_159731', 'idx_159732', 'idx_159733', 'idx_159735', 'idx_159736', 'idx_159738', 'idx_159739', 'idx_159740', 'idx_159741', 'idx_159742', 'idx_159743', 'idx_159745', 'idx_159747', 'idx_159748', 'idx_159750', 'idx_159751', 'idx_159752', 'idx_159755', 'idx_159757', 'idx_159758', 'idx_159760', 'idx_159761', 'idx_159763', 'idx_159766', 'idx_159767', 'idx_159768', 'idx_159769', 'idx_159770', 'idx_159773', 'idx_159775', 'idx_159776', 'idx_159777', 'idx_159778', 'idx_159779', 'idx_159780', 'idx_159781', 'idx_159782', 'idx_159783', 'idx_159786', 'idx_159787', 'idx_159788', 'idx_159789', 'idx_159790', 'idx_159791', 'idx_159792', 'idx_159793', 'idx_159795', 'idx_159796', 'idx_159797', 'idx_159798', 'idx_159801', 'idx_159802', 'idx_159803', 'idx_159804', 'idx_159805', 'idx_159806', 'idx_159807', 'idx_159808', 'idx_159809', 'idx_159810', 'idx_159811', 'idx_159812', 'idx_159813', 'idx_159814', 'idx_159815', 'idx_159816', 'idx_159819', 'idx_159820', 'idx_159821', 'idx_159822', 'idx_159823', 'idx_159824', 'idx_159825', 'idx_159827', 'idx_159828', 'idx_159830', 'idx_159831', 'idx_159832', 'idx_159833', 'idx_159834', 'idx_159835', 'idx_159836', 'idx_159837', 'idx_159838', 'idx_159839', 'idx_159840', 'idx_159841', 'idx_159842', 'idx_159843', 'idx_159845', 'idx_159846', 'idx_159847', 'idx_159848', 'idx_159849', 'idx_159850', 'idx_159851', 'idx_159852', 'idx_159853', 'idx_159855', 'idx_159856', 'idx_159857', 'idx_159858', 'idx_159859', 'idx_159861', 'idx_159862', 'idx_159863', 'idx_159864', 'idx_159865', 'idx_159866', 'idx_159867', 'idx_159869', 'idx_159870', 'idx_159871', 'idx_159872', 'idx_159873', 'idx_159875', 'idx_159876', 'idx_159877', 'idx_159880', 'idx_159881', 'idx_159883', 'idx_159885', 'idx_159886', 'idx_159887', 'idx_159888', 'idx_159889', 'idx_159890', 'idx_159891', 'idx_159892', 'idx_159895', 'idx_159896', 'idx_159897', 'idx_159898', 'idx_159899', 'idx_159901sz', 'idx_159902sz', 'idx_159903sz', 'idx_159905sz', 'idx_159906sz', 'idx_159907sz', 'idx_159908sz', 'idx_159909sz', 'idx_159910sz', 'idx_159911sz', 'idx_159912sz', 'idx_159913sz', 'idx_159915sz', 'idx_159916sz', 'idx_159918sz', 'idx_159919sz', 'idx_159920sz', 'idx_159922sz', 'idx_159923sz', 'idx_159925sz', 'idx_159926sz', 'idx_159928sz', 'idx_159929sz', 'idx_159930sz', 'idx_159931sz', 'idx_159932sz', 'idx_159933sz', 'idx_159934sz', 'idx_159935sz', 'idx_159936sz', 'idx_159937sz', 'idx_159938sz', 'idx_159939sz', 'idx_159940sz', 'idx_159941sz', 'idx_159943sz', 'idx_159944sz', 'idx_159945sz', 'idx_159948sz', 'idx_159949sz', 'idx_159950sz', 'idx_159951sz', 'idx_159952sz', 'idx_159953sz', 'idx_159954sz', 'idx_159955sz', 'idx_159956sz', 'idx_159957sz', 'idx_159958sz', 'idx_159959sz', 'idx_159960sz', 'idx_159961sz', 'idx_159962sz', 'idx_159963', 'idx_159963sz', 'idx_159964sz', 'idx_159965sz', 'idx_159966sz', 'idx_159967sz', 'idx_159968sz', 'idx_159969sz', 'idx_159970sz', 'idx_159971sz', 'idx_159972sz', 'idx_159973sz', 'idx_159974sz', 'idx_159975sz', 'idx_159976', 'idx_159977sz', 'idx_159978', 'idx_159979', 'idx_159980sz', 'idx_159981', 'idx_159982', 'idx_159983', 'idx_159984', 'idx_159985sz', 'idx_159986', 'idx_159987sz', 'idx_159988', 'idx_159990', 'idx_159991', 'idx_159992', 'idx_159993', 'idx_159994', 'idx_159995', 'idx_159996', 'idx_159997', 'idx_159998', 'idx_159999', 'idx_300subif', 'idx_399001sz', 'idx_399005sz', 'idx_399006sz', 'idx_399088sz', 'idx_399101sz', 'idx_399102sz', 'idx_399106sz', 'idx_399107sz', 'idx_399295sz', 'idx_399296sz', 'idx_399303sz', 'idx_399311sz', 'idx_399330sz', 'idx_399372sz', 'idx_399373sz', 'idx_399374sz', 'idx_399375sz', 'idx_399376sz', 'idx_399377sz', 'idx_399673sz', 'idx_399903sz', 'idx_399967sz', 'idx_399997sz', 'idx_510010sh', 'idx_510020sh', 'idx_510030sh', 'idx_510050sh', 'idx_510060sh', 'idx_510070sh', 'idx_510090sh', 'idx_510100sh', 'idx_510110sh', 'idx_510120sh', 'idx_510130sh', 'idx_510150sh', 'idx_510160sh', 'idx_510170sh', 'idx_510180sh', 'idx_510190sh', 'idx_510200', 'idx_510210sh', 'idx_510220sh', 'idx_510230sh', 'idx_510260sh', 'idx_510270sh', 'idx_510290sh', 'idx_510300sh', 'idx_510310sh', 'idx_510330sh', 'idx_510350sh', 'idx_510360sh', 'idx_510370', 'idx_510380sh', 'idx_510390sh', 'idx_510410sh', 'idx_510430sh', 'idx_510440sh', 'idx_510500sh', 'idx_510510sh', 'idx_510520sh', 'idx_510530sh', 'idx_510550sh', 'idx_510560sh', 'idx_510570', 'idx_510580sh', 'idx_510590sh', 'idx_510600sh', 'idx_510630sh', 'idx_510650sh', 'idx_510660sh', 'idx_510680sh', 'idx_510690', 'idx_510710sh', 'idx_510760', 'idx_510770', 'idx_510800sh', 'idx_510810sh', 'idx_510850sh', 'idx_510860', 'idx_510880sh', 'idx_510890sh', 'idx_510900sh', 'idx_510990', 'idx_511000', 'idx_511010sh', 'idx_511020sh', 'idx_511030sh', 'idx_511050', 'idx_511060sh', 'idx_511180', 'idx_511220sh', 'idx_511260sh', 'idx_511270sh', 'idx_511280sh', 'idx_511290sh', 'idx_511310', 'idx_511310sh', 'idx_511360', 'idx_511380', 'idx_511520', 'idx_511580', 'idx_511600sh', 'idx_511620sh', 'idx_511650sh', 'idx_511660', 'idx_511660sh', 'idx_511670', 'idx_511670sh', 'idx_511690sh', 'idx_511700sh', 'idx_511770sh', 'idx_511800sh', 'idx_511810sh', 'idx_511820sh', 'idx_511830sh', 'idx_511850sh', 'idx_511860sh', 'idx_511880sh', 'idx_511900sh', 'idx_511910sh', 'idx_511920sh', 'idx_511930sh', 'idx_511950sh', 'idx_511960sh', 'idx_511970sh', 'idx_511980sh', 'idx_511990sh', 'idx_512000sh', 'idx_512010sh', 'idx_512040sh', 'idx_512070sh', 'idx_512090sh', 'idx_512100sh', 'idx_512120sh', 'idx_512150sh', 'idx_512160sh', 'idx_512170sh', 'idx_512180sh', 'idx_512190sh', 'idx_512200sh', 'idx_512220sh', 'idx_512260sh', 'idx_512270sh', 'idx_512280sh', 'idx_512290sh', 'idx_512300sh', 'idx_512310sh', 'idx_512320', 'idx_512330sh', 'idx_512340sh', 'idx_512350', 'idx_512360sh', 'idx_512380sh', 'idx_512390sh', 'idx_512400sh', 'idx_512480sh', 'idx_512500sh', 'idx_512510sh', 'idx_512520sh', 'idx_512530sh', 'idx_512550sh', 'idx_512560sh', 'idx_512570sh', 'idx_512580sh', 'idx_512590sh', 'idx_512600sh', 'idx_512610sh', 'idx_512640sh', 'idx_512650sh', 'idx_512660sh', 'idx_512670sh', 'idx_512680sh', 'idx_512690sh', 'idx_512700sh', 'idx_512710sh', 'idx_512720sh', 'idx_512730', 'idx_512750sh', 'idx_512760sh', 'idx_512770sh', 'idx_512780sh', 'idx_512790sh', 'idx_512800sh', 'idx_512810sh', 'idx_512820sh', 'idx_512850sh', 'idx_512860sh', 'idx_512870sh', 'idx_512880sh', 'idx_512890sh', 'idx_512900sh', 'idx_512910sh', 'idx_512920sh', 'idx_512930sh', 'idx_512950sh', 'idx_512960sh', 'idx_512970sh', 'idx_512980sh', 'idx_512990sh', 'idx_513000sh', 'idx_513010', 'idx_513020', 'idx_513030sh', 'idx_513050sh', 'idx_513060', 'idx_513070', 'idx_513080', 'idx_513090', 'idx_513100sh', 'idx_513110', 'idx_513120', 'idx_513130', 'idx_513140', 'idx_513150', 'idx_513160', 'idx_513180', 'idx_513200', 'idx_513220', 'idx_513230', 'idx_513260', 'idx_513280', 'idx_513290', 'idx_513300', 'idx_513310', 'idx_513320', 'idx_513330', 'idx_513360', 'idx_513380', 'idx_513500sh', 'idx_513520sh', 'idx_513530', 'idx_513550', 'idx_513560', 'idx_513580', 'idx_513590', 'idx_513600sh', 'idx_513650', 'idx_513660sh', 'idx_513680sh', 'idx_513690', 'idx_513700', 'idx_513770', 'idx_513800sh', 'idx_513860', 'idx_513880sh', 'idx_513890', 'idx_513900sh', 'idx_513960', 'idx_513980', 'idx_513990', 'idx_515000sh', 'idx_515010sh', 'idx_515020sh', 'idx_515030', 'idx_515050sh', 'idx_515060sh', 'idx_515070sh', 'idx_515080sh', 'idx_515090', 'idx_515100', 'idx_515110sh', 'idx_515120', 'idx_515130', 'idx_515150sh', 'idx_515160', 'idx_515170', 'idx_515180sh', 'idx_515190', 'idx_515200sh', 'idx_515210', 'idx_515220', 'idx_515230', 'idx_515250', 'idx_515260', 'idx_515280', 'idx_515290', 'idx_515300sh', 'idx_515310sh', 'idx_515320', 'idx_515330sh', 'idx_515350', 'idx_515360sh', 'idx_515380', 'idx_515390sh', 'idx_515400', 'idx_515450', 'idx_515500', 'idx_515510', 'idx_515520sh', 'idx_515530', 'idx_515550sh', 'idx_515560', 'idx_515570', 'idx_515580sh', 'idx_515590', 'idx_515600sh', 'idx_515610', 'idx_515620', 'idx_515630', 'idx_515650sh', 'idx_515660sh', 'idx_515670', 'idx_515680sh', 'idx_515690', 'idx_515700', 'idx_515710', 'idx_515750sh', 'idx_515760', 'idx_515770', 'idx_515780', 'idx_515790', 'idx_515800sh', 'idx_515810sh', 'idx_515820', 'idx_515830', 'idx_515850', 'idx_515860sh', 'idx_515870', 'idx_515880sh', 'idx_515890', 'idx_515900sh', 'idx_515910', 'idx_515920', 'idx_515930', 'idx_515950', 'idx_515960', 'idx_515980', 'idx_515990', 'idx_515990sh', 'idx_516000', 'idx_516010', 'idx_516020', 'idx_516050', 'idx_516060', 'idx_516070', 'idx_516080', 'idx_516090', 'idx_516100', 'idx_516110', 'idx_516120', 'idx_516130', 'idx_516150', 'idx_516160', 'idx_516180', 'idx_516190', 'idx_516200', 'idx_516210', 'idx_516220', 'idx_516260', 'idx_516270', 'idx_516290', 'idx_516300', 'idx_516310', 'idx_516320', 'idx_516330', 'idx_516350', 'idx_516360', 'idx_516380', 'idx_516390', 'idx_516400', 'idx_516480', 'idx_516500', 'idx_516510', 'idx_516520', 'idx_516530', 'idx_516550', 'idx_516560', 'idx_516570', 'idx_516580', 'idx_516590', 'idx_516600', 'idx_516610', 'idx_516620', 'idx_516630', 'idx_516640', 'idx_516650', 'idx_516660', 'idx_516670', 'idx_516680', 'idx_516690', 'idx_516700', 'idx_516710', 'idx_516720', 'idx_516730', 'idx_516750', 'idx_516760', 'idx_516770', 'idx_516780', 'idx_516790', 'idx_516800', 'idx_516810', 'idx_516820', 'idx_516830', 'idx_516850', 'idx_516860', 'idx_516870', 'idx_516880', 'idx_516890', 'idx_516900', 'idx_516910', 'idx_516920', 'idx_516930', 'idx_516950', 'idx_516960', 'idx_516970', 'idx_516980', 'idx_517000', 'idx_517010', 'idx_517030', 'idx_517050', 'idx_517060', 'idx_517080', 'idx_517090', 'idx_517100', 'idx_517110', 'idx_517120', 'idx_517160', 'idx_517170', 'idx_517180', 'idx_517200', 'idx_517270', 'idx_517280', 'idx_517300', 'idx_517330', 'idx_517350', 'idx_517360', 'idx_517380', 'idx_517390', 'idx_517500', 'idx_517550', 'idx_517660', 'idx_517760', 'idx_517770', 'idx_517780', 'idx_517800', 'idx_517850', 'idx_517880', 'idx_517900', 'idx_517960', 'idx_517990', 'idx_518600', 'idx_518660', 'idx_518680', 'idx_518800sh', 'idx_518850', 'idx_518860', 'idx_518880', 'idx_518880sh', 'idx_518890', 'idx_560000', 'idx_560010', 'idx_560050', 'idx_560060', 'idx_560080', 'idx_560090', 'idx_560100', 'idx_560110', 'idx_560500', 'idx_560550', 'idx_560560', 'idx_560600', 'idx_560650', 'idx_560660', 'idx_560680', 'idx_560800', 'idx_560860', 'idx_560880', 'idx_560900', 'idx_560960', 'idx_560980', 'idx_560990', 'idx_561000', 'idx_561100', 'idx_561120', 'idx_561130', 'idx_561150', 'idx_561160', 'idx_561170', 'idx_561180', 'idx_561190', 'idx_561300', 'idx_561310', 'idx_561320', 'idx_561330', 'idx_561350', 'idx_561500', 'idx_561510', 'idx_561550', 'idx_561560', 'idx_561590', 'idx_561600', 'idx_561700', 'idx_561710', 'idx_561800', 'idx_561900', 'idx_561910', 'idx_561920', 'idx_561950', 'idx_561990', 'idx_562000', 'idx_562010', 'idx_562300', 'idx_562310', 'idx_562320', 'idx_562350', 'idx_562360', 'idx_562390', 'idx_562500', 'idx_562510', 'idx_562520', 'idx_562530', 'idx_562550', 'idx_562800', 'idx_562860', 'idx_562880', 'idx_562900', 'idx_562910', 'idx_562950', 'idx_562960', 'idx_562990', 'idx_563000', 'idx_563030', 'idx_588000', 'idx_588010', 'idx_588050', 'idx_588060', 'idx_588080', 'idx_588090', 'idx_588100', 'idx_588150', 'idx_588160', 'idx_588180', 'idx_588200', 'idx_588260', 'idx_588280', 'idx_588290', 'idx_588300', 'idx_588310', 'idx_588320', 'idx_588330', 'idx_588350', 'idx_588360', 'idx_588370', 'idx_588380', 'idx_588390', 'idx_588400', 'idx_588460', 'idx_801010swi', 'idx_801020swi', 'idx_801030swi', 'idx_801040swi', 'idx_801050swi', 'idx_801080swi', 'idx_801110swi', 'idx_801120swi', 'idx_801130swi', 'idx_801140swi', 'idx_801150swi', 'idx_801160swi', 'idx_801170swi', 'idx_801180swi', 'idx_801200swi', 'idx_801210swi', 'idx_801230swi', 'idx_801710swi', 'idx_801720swi', 'idx_801730swi', 'idx_801740swi', 'idx_801750swi', 'idx_801760swi', 'idx_801770swi', 'idx_801780swi', 'idx_801790swi', 'idx_801880swi', 'idx_801890swi', 'idx_801950swi', 'idx_801960swi', 'idx_801970swi', 'idx_801980swi', 'idx_809003ei', 'idx_809004ei', 'idx_892400msci', 'idx_930609csi', 'idx_930655csi', 'idx_930656csi', 'idx_930657csi', 'idx_930708csi', 'idx_930713csi', 'idx_930772csi', 'idx_930773csi', 'idx_930774csi', 'idx_930776csi', 'idx_930777csi', 'idx_930782csi', 'idx_930838csi', 'idx_930846csi', 'idx_930847csi', 'idx_930848csi', 'idx_930851csi', 'idx_930893csi', 'idx_930898csi', 'idx_930903csi', 'idx_930936csi', 'idx_930950csi', 'idx_931052csi', 'idx_931079csi', 'idx_931643csi', 'idx_bdir_cny_1y', 'idx_bdir_cny_3m', 'idx_bfr_forecast_pure', 'idx_bfr_forecast_pure_csi1000', 'idx_bfr_forecast_pure_csi300', 'idx_bfr_forecast_pure_csi500', 'idx_bfr_forecast_pure_csi800', 'idx_bfr_growth_pure', 'idx_bfr_growth_pure_csi1000', 'idx_bfr_growth_pure_csi300', 'idx_bfr_growth_pure_csi500', 'idx_bfr_growth_pure_csi800', 'idx_bfr_leverage_pure', 'idx_bfr_leverage_pure_csi1000', 'idx_bfr_leverage_pure_csi300', 'idx_bfr_leverage_pure_csi500', 'idx_bfr_leverage_pure_csi800', 'idx_bfr_liquidity_pure', 'idx_bfr_liquidity_pure_csi1000', 'idx_bfr_liquidity_pure_csi300', 'idx_bfr_liquidity_pure_csi500', 'idx_bfr_liquidity_pure_csi800', 'idx_bfr_momentum_pure', 'idx_bfr_momentum_pure_csi1000', 'idx_bfr_momentum_pure_csi300', 'idx_bfr_momentum_pure_csi500', 'idx_bfr_momentum_pure_csi800', 'idx_bfr_quality_pure', 'idx_bfr_quality_pure_csi1000', 'idx_bfr_quality_pure_csi300', 'idx_bfr_quality_pure_csi500', 'idx_bfr_quality_pure_csi800', 'idx_bfr_size_pure', 'idx_bfr_size_pure_csi1000', 'idx_bfr_size_pure_csi300', 'idx_bfr_size_pure_csi500', 'idx_bfr_size_pure_csi800', 'idx_bfr_technical_pure', 'idx_bfr_technical_pure_csi1000', 'idx_bfr_technical_pure_csi300', 'idx_bfr_technical_pure_csi500', 'idx_bfr_technical_pure_csi800', 'idx_bfr_value_pure', 'idx_bfr_value_pure_csi1000', 'idx_bfr_value_pure_csi300', 'idx_bfr_value_pure_csi500', 'idx_bfr_value_pure_csi800', 'idx_bfr_volatility_pure', 'idx_bfr_volatility_pure_csi1000', 'idx_bfr_volatility_pure_csi300', 'idx_bfr_volatility_pure_csi500', 'idx_bfr_volatility_pure_csi800', 'idx_cba00102cs', 'idx_cba00103cs', 'idx_cba00201cs', 'idx_cba00203cs', 'idx_cba00301_cs', 'idx_cba00303_cs', 'idx_cba00601_cs', 'idx_cba00701_cs', 'idx_cba00801_cs', 'idx_cba01201cs', 'idx_cba01801_cs', 'idx_cba02001_cs', 'idx_cba03801_cs', 'idx_cba04201_cs', 'idx_cbs00101cs', 'idx_cn6070sz', 'idx_cn6072sz', 'idx_djiagi', 'idx_emg00344508', 'idx_emg01317941', 'idx_emg01318041', 'idx_emi00135858', 'idx_emi00224692', 'idx_emi00227696', 'idx_emi00773118', 'idx_emi00773151', 'idx_emi01508580', 'idx_ftsegi', 'idx_h11001csi', 'idx_h11006csi', 'idx_h11009csi', 'idx_h11010csi', 'idx_h11015csi', 'idx_h11021csi', 'idx_h11025', 'idx_h11061csi', 'idx_h11073csi', 'idx_h20455csi', 'idx_h30082csi', 'idx_h30083csi', 'idx_h30084csi', 'idx_h30261csi', 'idx_h30351csi', 'idx_h30352csi', 'idx_h30353csi', 'idx_h30354csi', 'idx_h30355csi', 'idx_h30356csi', 'idx_h30357csi', 'idx_h30358csi', 'idx_h30524csi', 'idx_h30525csi', 'idx_h30526csi', 'idx_hsihi', 'idx_ixicgi', 'idx_n225gi', 'idx_nanhua_industrial_goods', 'idx_p_000016sh', 'idx_p_000300sh', 'idx_p_000852sh', 'idx_p_000905sh', 'idx_p_000906sh', 'idx_p_000985csi', 'idx_spxgi', 'idx_stock_debt']

print(len(identites))


with open('/Users/mac/PycharmProjects/dag_v2_test/2.txt', 'r') as file:
    subitems = file.read()
    subitems = subitems.strip('[').strip(']')
    ss = subitems.split('},')

print(ss)


