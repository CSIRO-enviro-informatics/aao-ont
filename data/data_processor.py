from rdflib import Graph, Namespace, URIRef, Literal, RDF, XSD, OWL
import csv
from datetime import datetime

AAO = Namespace('http://test.linked.data.gov.au/def/aaos/')
AAOS = Namespace('http://test.linked.data.gov.au/dataset/aaos/')
DCT = Namespace('http://purl.org/dc/terms/')
TIME = Namespace('http://www.w3.org/2006/time#')


'''
matters_clean_departments.csv
THE ATTORNEY\x1e GENERAL'S DEPARTMENT -> THE ATTORNEY GENERAL\'S DEPARTMENT
THE DEPARTMENT OF VETERANS' AFFAIRS(Part of the Defence Portfolio) -> THE DEPARTMENT OF VETERANS' AFFAIRS (Part of the Defence Portfolio)
'''
def get_department_number(text):
    depts = [
        'THE ATTORNEY GENERAL\'S DEPARTMENT',
        'THE DEPARTMENT OF AGRICULTURE, FISHERIES AND FORESTRY',
        'THE DEPARTMENT OF BROADBAND, COMMUNICATIONS AND THE DIGITAL ECONOMY',
        'THE DEPARTMENT OF CLIMATE CHANGE (Part of the Prime Minister and Cabinet Portfolio)',
        'THE DEPARTMENT OF DEFENCE',
        'THE DEPARTMENT OF EDUCATION, EMPLOYMENT AND WORKPLACE RELATIONS',
        'THE DEPARTMENT OF FAMILIES, HOUSING, COMMUNITY SERVICES AND INDIGENOUS AFFAIRS',
        'THE DEPARTMENT OF FINANCE AND DEREGULATION',
        'THE DEPARTMENT OF FOREIGN AFFAIRS AND TRADE',
        'THE DEPARTMENT OF HEALTH AND AGEING',
        'THE DEPARTMENT OF HUMAN SERVICES',
        'THE DEPARTMENT OF IMMIGRATION AND CITIZENSHIP',
        'THE DEPARTMENT OF INFRASTRUCTURE, TRANSPORT, REGIONAL DEVELOPMENT AND LOCAL GOVERNMENT',
        'THE DEPARTMENT OF INNOVATION, INDUSTRY, SCIENCE AND RESEARCH',
        'THE DEPARTMENT OF RESOURCES, ENERGY AND TOURISM',
        'THE DEPARTMENT OF THE ENVIRONMENT, WATER, HERITAGE AND THE ARTS',
        'THE DEPARTMENT OF THE PRIME MINISTER AND CABINET',
        'THE DEPARTMENT OF THE TREASURY',
        'THE DEPARTMENT OF VETERANS\' AFFAIRS (Part of the Defence Portfolio)',
        'DEPARTMENT OF DEFENCE',
        'THE DEPARTMENT OF CLIMATE CHANGE AND ENERGY EFFICIENCY',
        'THE DEPARTMENT OF INFRASTRUCTURE AND TRANSPORT',
        'THE DEPARTMENT OF REGIONAL AUSTRALIA, REGIONAL DEVELOPMENT AND LOCAL GOVERNMENT (Part of the Prime Minister and Cabinet Portfolio)',
        'THE DEPARTMENT OF SUSTAINABILITY, ENVIRONMENT, WATER, POPULATION AND COMMUNITIES',
        'THE DEPARTMENT OF INDUSTRY, INNOVATION, SCIENCE, RESEARCH AND TERTIARY EDUCATION',
        'THE DEPARTMENT OF REGIONAL AUSTRALIA, LOCAL GOVERNMENT, ARTS AND SPORT',
        'THE DEPARTMENT OF INDUSTRY, INNOVATION, CLIMATE CHANGE, SCIENCE, RESEARCH AND TERTIARY EDUCATION',
        'THE DEPARTMENT OF AGRICULTURE',
        'THE DEPARTMENT OF COMMUNICATIONS',
        'THE DEPARTMENT OF EDUCATION',
        'THE DEPARTMENT OF EMPLOYMENT',
        'THE DEPARTMENT OF FINANCE',
        'THE DEPARTMENT OF HEALTH',
        'THE DEPARTMENT OF HUMAN SERVICES (Part of the Social Services Portfolio)',
        'THE DEPARTMENT OF IMMIGRATION AND BORDER PROTECTION',
        'THE DEPARTMENT OF INDUSTRY',
        'THE DEPARTMENT OF INFRASTRUCTURE AND REGIONAL DEVELOPMENT',
        'THE DEPARTMENT OF SOCIAL SERVICES',
        'THE DEPARTMENT OF THE ENVIRONMENT',
        'THE DEPARTMENT OF EDUCATION AND TRAINING',
        'THE DEPARTMENT OF INDUSTRY AND SCIENCE',
        'THE DEPARTMENT OF AGRICULTURE AND WATER RESOURCES',
        'THE DEPARTMENT OF COMMUNICATIONS AND THE ARTS',
        'THE DEPARTMENT OF INDUSTRY, INNOVATION AND SCIENCE',
        'THE DEPARTMENT OF THE ENVIRONMENT AND ENERGY',
        'THE DEPARTMENT OF HOME AFFAIRS',
        'THE DEPARTMENT OF INDUSTRY, INNOVATION AND SCIENCE (Part of the Jobs and Innovation Portfolio)',
        'THE DEPARTMENT OF INFRASTRUCTURE, REGIONAL DEVELOPMENT AND CITIES',
        'THE DEPARTMENT OF JOBS AND SMALL BUSINESS (Part of the Jobs and Innovation Portfolio)',
        'THE DEPARTMENT OF JOBS AND SMALL BUSINESS'
    ]

    return depts.index(text)


def test_get_department_number():
    with open('matters_clean_departments.csv') as f:
        lines = csv.reader(f, delimiter=',', quotechar='"')
        count = 0
        for line in lines:
            if count > 0:
                print('department: ' + str(get_department_number(line[1])))

            count = count + 1

'''
mattes_clean_matters.csv
Administration of Parliamentarians? entitlements -> "Administration of Parliamentarians' entitlements"
Administration of Parliamentarians? work expenses -> "Administration of Parliamentarians' work expenses"
Administration of the Australian Government?s self-managed general insurance fund (Comcover) -> "Administration of the Australian Government's self-managed general insurance fund (Comcover)"
Assistance to the Prime MinIster in managing the Cabinet program -> Assistance to the Prime Minister in managing the Cabinet program
Defence, including - international defence relations and defence co-operation; defence scientific research and development; defence procurement and purchasing, including offsets for defence purposes; defence industry development and co-operation\n 
-> 
Defence, including - international defence relations and defence co-operation; defence scientific research and development; defence procurement and purchasing, including offsets for defence purposes; defence industry development and co-operation
Design, development, delivery, co-ordination and monitoring of government services, social security, child support, students, families, aged care and health programs (excluding Health provider compliance), superannuation release and Australian Hearing Services�
->
Design, development, delivery, co-ordination and monitoring of government services, social security, child support, students, families, aged care and health programs (excluding Health provider compliance), superannuation release and Australian Hearing Services
co-ordination -> co-ordination
Children?s -> Children's
Freedom of information -> Freedom of Information
CRS�Australia -> CRS Australia
Native title -> Native title
Prime�Minister?s official residences -> Prime Minister's official residences
plant breeders? -> plant breeders'
'''
def get_matter_number(text):
    matters = [
        'Aboriginal and Torres Strait Islander health programs and policies',
        'Administration of criminal justice, including - criminal law policy and principles of criminal responsibility; matters relating to prosecution; sentencing and management of federal offenders; international crime co-operation, including extradition and mutual assistance in criminal matters',
        'Administration of export controls on agricultural, fisheries and forestry industries products',
        'Administration of export controls on rough diamonds, uranium and thorium',
        'Administration of international commodity agreements',
        'Administration of Parliamentarians\' entitlements',
        'Administration of Parliamentarians\' work expenses',
        'Administration of the Australian Antarctic Territory, and the Territory of Heard Island and McDonald Islands',
        'Administration of the Australian Government\'s self-managed general insurance fund (Comcover)',
        'Administration of the Jervis Bay Territory, the Territory of Cocos (Keeling) Islands, the Territory of Christmas Island, the Coral Sea Islands Territory, the Territory of Ashmore and Cartier Islands, and of Commonwealth responsibilities on Norfolk Island',
        'Administrative support for Royal Commissions and certain other inquiries',
        'Adult migrant education',
        'Advice on the Future Fund',
        'Advice to the Prime Minister across Government on policy and implementation',
        'Ageing research',
        'Agricultural, pastoral, fishing, food and forest industries',
        'Air quality',
        'Analytical laboratory services',
        'Anti-dumping',
        'Arrangements for the settlement of migrants and humanitarian entrants, other than migrant child and migrant adult education',
        'Arrangements for the settlement of migrants and humanitarian entrants, other than migrant child education',
        'Asset sales',
        'Assistance to Cabinet and its Committees',
        'Assistance to the Prime Minister in managing the Cabinet program',
        'Australian government employment workplace relations policy, including administration of the framework for agreement making and remuneration and conditions',
        'Australian Government employment workplace relations policy, including equal employment opportunity and administration of the framework for agreement making and remuneration and conditions',
        'Australian honours and symbols policy',
        'Biosecurity, in relation to animals and plants',
        'Biosecurity, in relation to human health',
        'Biotechnology, excluding gene technology regulation',
        'Blood and organ policy and funding',
        'Border immigration control',
        'Borrowing money on the public credit of the Commonwealth',
        'Bounties on the production of goods',
        'Broadband policy and programs',
        'Broadcasting policy',
        'Budget policy advice and process, and review of governmental programs',
        'Built environment innovation',
        'Business entry point management',
        'Business entry point management and business services co-ordination',
        'Business law and practice',
        'Census and statistics',
        'Central advertising system',
        'Child support policy',
        'Childcare policy and programs',
        'Citizenship',
        'Civil aviation and airports',
        'Civil space issues',
        'Classification',
        'Clean fossil fuel energy',
        'Climate change adaptation strategy and co-ordination',
        'Collaborative research in science and technology',
        'Commemorations',
        'Commercialisation and utilisation of public sector research',
        'Commercialisation and utilisation of public sector research relating to portfolio programs and agencies',
        'Commodity marketing, including export promotion and agribusiness',
        'Commodity-specific international organisations and activities',
        'Commonwealth Aboriginal and Torres Strait Islander policy, programs and service delivery',
        'Commonwealth emergency management',
        'Commonwealth property policy framework, legislation and policy for the management of property leased or owned by the Commonwealth, including acquisition, disposal and management of property interests',
        'Commonwealth-State financial relations',
        'Community and household climate action',
        'Community and household renewable energy programs',
        'Community development employment projects',
        'Community mental health',
        'Community support services',
        'Community support services, excluding the Home and Community Care program',
        'Competition and consumer policy',
        'Constitutional development of the Australian Capital Territory',
        'Constitutional development of the Northern Territory',
        'Construction industry',
        'Construction industry, excluding workplace relations',
        'Consumer credit',
        'Content policy relating to the information economy',
        'Co-ordination of climate change science activities',
        'Co-ordination of early childhood development policy and responsibilities',
        'Co-ordination of early childhood development policy and responsibilities, including Indigenous early childhood development',
        'Co-ordination of Government administration',
        'Co-ordination of Government Advertising',
        'Co-ordination of labour market research',
        'Co-ordination of research policy',
        'Co-ordination of research policy in relation to universities',
        'Co-ordination of science research policy',
        'Co-ordination of sustainable communities policy',
        'Copyright',
        'Corporate insolvency',
        'Corporate, financial services and securities law',
        'Counter terrorism policy co-ordination',
        'Country of origin labelling',
        'Creation and development of research infrastructure',
        'Criminal law and law enforcement',
        'Critical infrastructure protection co-ordination',
        'Cultural affairs, including movable cultural heritage and support for the arts',
        'Cultural affairs, including support for the arts',
        'Currency and legal tender',
        'Customs and border control other than quarantine and inspection',
        'Customs and border control other than quarantine and inspection, and immigration',
        'Cyber policy co-ordination',
        'Defence Service Homes',
        'Defence, including - international defence relations and defence co-operation; defence scientific research and development; defence capability plan acquisitions and sustainment; defence industry development and co-operation',
        'Defence, including - international defence relations and defence co-operation; defence scientific research and development; defence procurement and purchasing, including offsets for defence purposes; defence industry development and co-operation',
        'Defence, including - international defence relations and defence co-operation; defence scientific research and development; defence procurement and purchasing; defence industry development and co-operation',
        'Delivery of regional and rural specific services',
        'Delivery of regional and territory specific services and programs',
        'Design and implementation of emissions trading',
        'Design, development, delivery, co-ordination and monitoring of government services, social security, child support, students, families, aged care and health programs (excluding Health provider compliance), superannuation release and Australian Hearing Services',
        'Design, development, delivery, co-ordination and monitoring of government services, social security, child support, students, families, aged care and health programs, superannuation release and Australian Hearing Services',
        'Development and co-ordination of domestic and international climate change policy',
        'Development and co-ordination of domestic climate change policy',
        'Development and co-ordination of international climate change policy',
        'Development, delivery and co-ordination of government services',
        'Development, delivery and co-ordination of government services, and development of policy on service delivery',
        'Domestic and international climate change policy',
        'Early childhood and childcare policy and programs',
        'Economic, fiscal and monetary policy',
        'Education and training transitions policy and programs',
        'Education policy and programs including schools, vocational, higher education and Indigenous education, but excluding migrant adult education',
        'Electoral matters',
        'Employment policy, including employment services',
        'Energy efficiency',
        'Energy efficiency policy and standards',
        'Energy policy',
        'Energy-specific international obligations and activities',
        'Energy-specific international organisations and activities',
        'Energy-specific international organisations and activities',
        'Enterprise improvement',
        'Entry, stay and departure arrangements for non-citizens',
        'Environment protection and conservation of biodiversity',
        'Environmental information and research',
        'Environmental research',
        'Environmental water use and resources relating to the Commonwealth Environmental Water Holder',
        'Equal employment opportunity',
        'Ethnic affairs',
        'Evaluation and audit of Indigenous programs and operations',
        'Excise',
        'Export services',
        'External Affairs, including - relations and communications with overseas governments and United Nations agencies; treaties, including trade agreements; bilateral, regional and multilateral trade policy; international trade and commodity negotiations; market development, including market access; trade and international business development; investment promotion; international development cooperation; diplomatic and consular missions; international security issues, including disarmament, arms control and nuclear nonproliferation; public diplomacy, including information and cultural programs',
        'External Affairs, including - relations and communications with overseas governments and United Nations agencies; treaties, including trade agreements; bilateral, regional and multilateral trade policy; international trade and commodity negotiations; market development, including market access; trade promotion and international business development; international development co-operation; diplomatic and consular missions; international security issues, including disarmament, arms control and nuclear non-proliferation; public diplomacy, including information and cultural programs',
        'External Affairs, including - relations and communications with overseas governments and United Nations agencies; treaties, including trade agreements; bilateral, regional and multilateral trade policy; international trade and commodity negotiations; market development, including market access; trade and international business development; investment promotion; international development co-operation;diplomatic and consular missions; international security issues, including disarmament, arms control and nuclear; non-proliferation; public diplomacy, including information and cultural programs',
        'External Affairs, including - relations and communications with overseas governments and United Nations agencies; treaties, including trade agreements; bilateral, regional and multilateral trade policy; international trade and commodity negotiations; market development, including market access; trade and international business development; investment promotion; international development co-operation; diplomatic and consular missions; international security issues, including disarmament, arms control and nuclear; non-proliferation; public diplomacy, including information and cultural programs',
        'External Affairs, including - relations and communications with overseas governments and United Nations agencies; treaties, including trade agreements; bilateral, regional and multilateral trade policy; international trade and commodity negotiations; market development, including market access; trade and international business development; investment promotion; international development co-operation; diplomatic and consular missions; international security issues, including disarmament, arms control and nuclear; non-proliferation; public diplomacy, including information and cultural programs;',
        'External Affairs, including - relations and communications with overseas governments and United Nations agencies; treaties, including trade agreements; bilateral, regional and multilateral trade policy; international trade and commodity negotiations; market development, including market access; trade and international business development; investment promotion; international development co-operation; diplomatic and consular missions; international security issues, including disarmament, arms control and nuclear non-proliferation; public diplomacy, including information and cultural programs;',
        'External Affairs, including - relations and communications with overseas governments and United Nations agencies; treaties, including trade agreements; bilateral, regional and multilateral trade policy; international trade and commodity negotiations; market development, including market access; trade and international business development; investment promotion; international development co-operation; diplomatic and consular missions; international security issues, including disarmament, arms control and nuclear non-proliferation; public diplomacy, including information and cultural program',
        'External Affairs, including - relations and communications with overseas governments and United Nations agencies; treaties, including trade agreements; bilateral, regional and multilateral trade policy; international trade and commodity negotiations; market development, including market access; trade and international business development; investment promotion; international development co-operation; diplomatic and consular missions; international security issues, including disarmament, arms control and nuclear non-proliferation; public diplomacy, including information and cultural programs',
        'External Affairs, including - relations and communications with overseas governments and United Nations agencies; treaties, including trade agreements; bilateral, regional and multilateral trade policy; international trade and commodity negotiations; market development, including market access; trade and international business development; investment promotion; international development co-operation; diplomatic and consular missions; international security issues, including disarmament, arms control, nuclear non-proliferation, counter terrorism and cyber affairs; public diplomacy, including information and cultural programs',
        'External Affairs, including - relations and communications with overseas governments and United Nations agencies;treaties, including trade agreements; bilateral, regional and multilateral trade policy;international trade and commodity negotiations; market development, including market access; trade promotion and international business development; international development co-operation; diplomatic and consular missions; international security issues, including disarmament, arms control and nuclear; non-proliferation; public diplomacy, including information and cultural programs',
        'External Affairs, including -relations and communications with overseas governments and United Nations agencies; treaties including trade agreements; bilateral; regional and multilateral trade policy; international trade and commodity negotiations; market development, including market access; trade promotion; international development co-operation; diplomatic and consular missions; international security issues, including disarmament, arms control and nuclear non-proliferation; public diplomacy, including information and cultural programs',
        'External Affairs, including -relations and communications with overseas governments and United Nations agencies; treaties, including trade agreements; bilateral, regional and multilateral trade policy; international trade and commodity negotiations; market development, including market access; trade promotion and international business development; international development co-operation; diplomatic and consular missions; international security issues, including disarmament, arms control and nuclear; non-proliferation; public diplomacy, including information and cultural programs',
        'External Affairs, including -relations and communications with overseas governments and United Nations agencies; treaties, including trade agreements; bilateral, regional and multilateral trade policy; international trade and commodity negotiations; market development, including market access; trade and international business development; investment promotion; international development co-operation; diplomatic and consular missions; international security issues, including disarmament, arms control and nuclear non-proliferation; public diplomacy, including information and cultural programs',
        'External Affairs, including -relations and communications with overseas governments and United Nations agencies; treaties, including trade agreements; bilateral, regional and multilateral trade policy; international trade and commodity negotiations; market development, including market access; trade and international business development; investment promotion; international development co-operation; diplomatic and consular missions;international security issues, including disarmament, arms control, nuclear non-proliferation, counter terrorism and cyber affairs; public diplomacy, including information and cultural programs',
        'External Affairs, including -relations and communications with overseas governments and United Nations agencies;treaties, including trade agreements; bilateral, regional and multilateral trade policy; international trade and commodity negotiations; market development, including market access; trade and international business development; investment promotion; international development co-operation; diplomatic and consular missions; international security issues, including disarmament, arms control and nuclear non-proliferation; public diplomacy, including information and cultural programs',
        'Facilitation of the development of service industries generally',
        'Family relationship services',
        'Family relationship, Family and Children\'s Support Services',
        'Financial sector policy',
        'Food industry policy',
        'Food policy, processing and exports',
        'Food processing industry policy',
        'Food security policy and programs',
        'Foreign exchange',
        'Foreign investment in Australia',
        'Foundation skills for adults',
        'Fraud and anti-corruption policy',
        'Freedom of Information',
        'Gene technology regulation',
        'General policy guidelines for Commonwealth statutory authorities',
        'Geoscience research and information services including geodesy, mapping, remote sensing and land information co-ordination',
        'Geoscience research and information services including geodesy, mapping, remote sensing, groundwater and spatial data co-ordination',
        'Government ceremonial and hospitality',
        'Government financial accountability, efficiency, governance and financial management frameworks, including grants and procurement policy and services',
        'Government financial accountability, efficiency, governance and financial management frameworks, including grants and procurement policy and services (excluding information and communications technology procurement policy and services)',
        'Government financial accountability, governance and financial management frameworks, including grants and procurement policy and services',
        'Government financial accountability, governance and financial management frameworks, including procurement policy and services',
        'Government on-line delivery and information technology and communications management',
        'Greenhouse emissions and energy consumption reporting',
        'Greenhouse gas abatement programs',
        'Greenhouse mitigation and adaptation',
        'Health and ageing research',
        'Health benefits schemes',
        'Health promotion and disease prevention',
        'Health provider compliance',
        'Health research',
        'Health workforce capacity',
        'Hearing services policy and funding',
        'Higher education policy, regulation and programs',
        'Higher education, skills and vocational education policy and programs',
        'Higher education, skills and vocational education policy, regulation and programs',
        'Hospitals funding and policy, including relationships and linkages within the continuum of health care',
        'Hospitals funding, including relationship with primary health care',
        'Housing affordability',
        'Housing policy co-ordination, welfare housing and rent assistance',
        'Housing supply policy',
        'Immigration and migration, including - border security; entry, stay and departure arrangements for non-citizens; customs and border control other than quarantine and inspection',
        'Implementation of the National Health and Hospitals Network',
        'Income security and support policies and programs for families with children, carers, the aged, people with disabilities and people in hardship',
        'Income security policies and programs for families with children, carers, the aged and people in hardship',
        'Income security policies and programs for families with children, carers, the aged, people with disabilities and people in hardship',
        'Income support and participation policy for people of working age',
        'Income support policies and programs for students and apprentices',
        'Income support policies for students and apprentices',
        'Indigenous higher education and vocational training',
        'Indigenous policy co-ordination and the promotion of reconciliation',
        'Indigenous policy co-ordination, programs and the promotion of reconciliation',
        'Industrial energy efficiency',
        'Industrial research and development, and commercialisation',
        'Industry innovation policy and technology diffusion',
        'Information and communications technology industry development',
        'Information and communications technology procurement policy and services',
        'Infrastructure and project financing',
        'Infrastructure planning and co-ordination',
        'Infrastructure planning and co-ordination',
        'Intergovernmental relations and communications with State and Territory Governments',
        'International climate change negotiations',
        'International development and aid',
        'International expositions',
        'International finance',
        'International science engagement',
        'Investment promotion',
        'Ionospheric prediction',
        'Job Network',
        'Job Services Australia',
        'Jobactive',
        'Labour market and income support policies and programs for people of working age',
        'Labour market programs for people of working age',
        'Land contamination',
        'Land transport',
        'Law and justice including - Administrative law; Alternative dispute resolution; Bankruptcy; Censorship; Constitutional law; Copyright; Courts and tribunals; Human rights; Indigenous law and justice programs; International law; Law reform; Legal assistance; Legislative drafting; Marriage and family law; Native Title',
        'Law and justice including - Administrative law; Alternative dispute resolution; Bankruptcy; Censorship; Constitutional law; Copyright; Courts and tribunals; Human rights; Indigenous law and justice programs; International law; Law reform; Legal assistance; Legislative drafting; Marriage and family law; Native Title',
        'Law and justice including - Administrative law; Alternative dispute resolution; Bankruptcy; Censorship; Constitutional law; Copyright; Courts and tribunals; Human rights; Indigenous law and justice programs; International law; Law reform; Legal assistance; Legislative drafting; Marriage and family law; Native Title; Personal property securities',
        'Law and justice including - Administrative law; Alternative dispute resolution; Bankruptcy; Censorship; Constitutional law; Copyright; Courts and tribunals; Human rights; Indigenous law and justice; International law; Law reform; Legal assistance; Legislative drafting; Marriage and family law; Native Title; Personal property securities',
        'Law and justice including - Administrative law; Alternative dispute resolution; Bankruptcy; Censorship; Constitutional law; Copyright; Courts and tribunals; Human rights; International law; Law reform; Legal assistance; Legislative drafting; Marriage and family law; Personal property securities',
        'Law and justice including - Administrative law; Alternative dispute resolution; Bankruptcy; Constitutional law; Courts and tribunals; Human rights; International law; Law reform; Legal assistance; Legislative drafting; Marriage and family law; Personal property securities',
        'Law enforcement policy and operations',
        'Legal services to the Commonwealth',
        'Low emissions fossil fuel energy',
        'Major projects facilitation',
        'Major projects office, including facilitation and implementation of all non-Defence development projects',
        'Major projects, including implementation of all non-Defence development projects',
        'Management of government records',
        'Management of non-Defence Commonwealth property in Australia, including construction, major refurbishment, sustainability, acquisition, ownership and disposal of real property',
        'Mandatory renewable energy target policy, regulation and co-ordination',
        'Manufacturing and commerce including industry and market development',
        'Maritime transport including shipping',
        'Marketing of manufactures and services',
        'Marketing, including export promotion, of manufactures and services',
        'Matters relating to local government',
        'Medical indemnity insurance issues',
        'Medicare provider compliance',
        'Mental health policy and primary mental health care',
        'Meteorology',
        'Migrant adult education',
        'Mineral and energy industries, including oil and gas, and electricity',
        'Mineral and energy resources, including oil and gas, extraction and upstream processing',
        'Minerals and energy resources research, science and technology',
        'Monitoring and management of service delivery and purchaser/provider relationships involving Centrelink, Medicare Australia, the Child Support Agency, Australian Hearing, Health Services Australia and CRS Australia',
        'Monitoring and management of service delivery arrangements involving Centrelink, Medicare Australia, the Child Support Agency, Australian Hearing, and CRS Australia',
        'Monitoring and management of service delivery arrangements involving social security, child support, students, families, aged care, health programs, disability employment services, superannuation release and Australian Hearing Services',
        'Multicultural affairs',
        'National drug strategy',
        'National energy market',
        'National energy market, including electricity, gas and liquid fuels',
        'National fuel quality standards',
        'National policy issues relating to the digital economy',
        'National policy on cities',
        'National security policy and operations',
        'National security policy co-ordination',
        'National security, protective security policy and co-ordination',
        'Native Title',
        'Natural disaster relief and mitigation in the form of financial assistance to the States and Territories',
        'Natural disaster relief, recovery and mitigation policy and financial assistance including payments to the States and Territories and the Australian Government Disaster Recovery Payment',
        'Natural, built and cultural heritage',
        'Natural, built and movable cultural heritage',
        'Non-profit sector and volunteering',
        'Non-profit sector and volunteering',
        'Northern Australia policy and co-ordination',
        'Notification and assessment of industrial chemicals',
        'Occupational health and safety, rehabilitation and compensation',
        'Official Establishments, ownership and property management',
        'Official Establishments, ownership and property management of the Prime Minister\'s official residences',
        'Old Parliament House',
        'Overseas property management, including acquisition, ownership and disposal of real property',
        'Participation, activity test and compliance policy for participation payment recipients',
        'Pharmaceutical benefits',
        'Planning and land management in the Australian Capital Territory',
        'Policy advice and administrative support to the Prime Minister',
        'Policy advice on the Future Fund and Nation-building Funds',
        'Policy advice on the Future Fund and Nation-building Funds and authorisation of payments from the Nation-building Funds to Agencies',
        'Policy advice on the Future Fund, Nation-building Funds and the DisabilityCare Australia Fund; and authorisation of payments from the Nation-building Funds and the DisabilityCare Australia Fund recommended by relevant Agencies',
        'Policy for and promotion of active ageing, other than employment policy',
        'Policy for and promotion of active ageing, other than income security and employment policy',
        'Policy, co-ordination and support for education exports and services',
        'Policy, co-ordination and support for international education',
        'Policy, co-ordination and support for international education and research engagement',
        'Population policy',
        'Postal and telecommunications policies and programs',
        'Preschool education policy and programs',
        'Pre-school education policy and programs',
        'Prices surveillance',
        'Primary health care',
        'Primary health care of Aboriginal and Torres Strait Islander people',
        'Primary industries research including economic research',
        'Privacy',
        'Private health insurance',
        'Promotion of collaborative research in science and technology',
        'Promotion of flexible workplace relations policies and practices',
        'Promotion of flexible workplace relations policies and practices, including workplace productivity',
        'Promotion of industrial research and development, and commercialisation',
        'Promotion of reconciliation',
        'Protective security policy',
        'Protective services at Commonwealth establishments and diplomatic and consular premises in Australia',
        'Provision of B2G and G2G authentication services',
        'Provision of consular services to Australian citizens abroad',
        'Provision to Australian citizens of secure travel identification',
        'Public data policy and related matters',
        'Public health and medical research',
        'Public health, including health protection, and medical research',
        'Radioactive waste management',
        'Reducing the burden of government regulation',
        'Regional Australia policy and co-ordination',
        'Regional development',
        'Regional policy and co-ordination',
        'Regulation of therapeutic goods',
        'Renewable energy',
        'Renewable energy policy, regulation and co-ordination',
        'Renewable energy programs',
        'Renewable energy target policy, regulation and co-ordination',
        'Renewable energy technology development',
        'Repatriation income support, compensation and health programs for veterans, members of the Defence Force, certain mariners and their dependants',
        'Research grants and fellowships',
        'Rural adjustment and drought issues',
        'Rural industries inspection and quarantine',
        'Schooling transitions policy and programs including career pathways',
        'Schools education policy and programs, including vocational education and training in schools',
        'Schools education policy and programs, including vocational education and training in schools, but excluding migrant adult education',
        'Schools education policy and programs, including vocational education and training in schools, Indigenous school education, but excluding migrant adult education',
        'Schools education policy and programs, including, Indigenous school education, but excluding migrant adult education',
        'Science awareness programs in schools',
        'Science engagement and awareness',
        'Science policy',
        'Services for families with children, people with disabilities and carers',
        'Services for older Australians, including carers',
        'Services for older people, including their carers',
        'Services to help people with disabilities obtain employment',
        'Services to help people with disabilities obtain employment, other than supported employment',
        'Shareholder advice on Government Business Enterprises and commercial entities treated as GBEs',
        'Skills and vocational education policy regulation and programs',
        'Small business policy',
        'Small business policy and implementation',
        'Small business policy and programs',
        'Small business programs',
        'Social housing, rent assistance and homelessness',
        'Social inclusion, non-profit sector and volunteering',
        'Soils and other natural resources',
        'Specific health services, including human quarantine',
        'Spectrum policy management',
        'Sport and recreation',
        'Strategic management of non-Defence Commonwealth property in Australia, including construction, major refurbishment, acquisition, sustainability, ownership and disposal of real property',
        'Strategic management of non-Defence Commonwealth-owned property in Australia, including construction, major refurbishment, acquisition, ownership and disposal of real property',
        'Superannuation and retirement savings policy',
        'Superannuation arrangements for Australian Government civilian employees and members of parliament and retirement benefits for Federal Judges and Governors-General',
        'Superannuation related to former and current members of parliament and Australian Government employees',
        'Support for introduction of a national occupation licensing system',
        'Support for ministers and parliamentary secretaries with regional responsibilities',
        'Taxation',
        'Tourism industry',
        'Tourism industry (domestic)',
        'Tourism industry (international)',
        'Trade marks, plant breeders\' rights and patents of inventions and designs',
        'Training, including apprenticeships and training and assessment services',
        'Training, including apprenticeships and training and skills assessment services',
        'Training, including apprenticeships and training services',
        'Transport safety, including investigations',
        'Transport security',
        'Urban environment',
        'Valuation services',
        'War graves',
        'Water policy and resources',
        'Weights and measures standards',
        'Welfare housing and rent assistance',
        'Whole of government information and communications technology',
        'Whole of government information and communications technology (including Gov 2.0 and related matters), other than that related to government service delivery;',
        'Whole of government information and communications technology strategy, policy, procurement and services, including Gov 2.0 and related matters',
        'Whole of government information and communications technology, other than that related to government service delivery',
        'Whole of government integrity policy and activities',
        'Whole of government national security and intelligence policy co-ordination',
        'Whole of government service delivery policy',
        'Women\'s policies and programs',
        'Women\'s policies, programs and the promotion of gender equality at work',
        'Work and family policy co-ordination',
        'Work and family programs',
        'Work health and safety, rehabilitation and compensation',
        'Workforce development',
        'Workplace relations policy development, advocacy and implementation',
        'Youth affairs and programs',
        'Youth affairs and programs, excluding income support policies and programs',
        'Youth affairs and programs, including youth transitions',
        'Youth affairs and programs, including youth transitionsPre-school education policy and programs'
    ]

    return matters.index(text)


def test_matter_number():
    with open('matters_clean.csv') as f:
        lines = csv.reader(f, delimiter=',', quotechar='"')
        count = 0
        for line in lines:
            if count > 0:
                print('matter: ' + str(get_matter_number(line[2])))

            count = count + 1


def add_namespaces(g):
    g.bind('aao', AAO)
    g.bind('aaos', AAOS)
    g.bind('dct', DCT)
    g.bind('time', TIME)


def make_aaos():
    g = Graph()
    add_namespaces(g)

    with open('aaos.csv', 'r') as f:
        lines = f.readlines()
        for line in lines:
            words = line.split(',')

            this_aao = URIRef(AAOS + 'aao/' + words[0])

            if words[2] == 'Amendment':
                aao_class = URIRef('http://test.linked.data.gov.au/def/aaos/Amendment')
            else:
                aao_class = URIRef('http://test.linked.data.gov.au/def/aaos/AAO')

            g.add((
                this_aao,  # an AAO within the AAO register within the AAOs dataset
                RDF.type,  # an AAO is of type...
                aao_class  # of type AAO, as defined in the AAOs ontology
            ))

            # the issued date of this AAO
            issued = datetime.strptime(words[1], '%d-%b-%y')
            g.add((
                this_aao,
                DCT.issued,
                Literal(datetime.strftime(issued, '%Y-%m-%d'), datatype=XSD.date)
            ))

            g.add((
                this_aao,
                TIME.hasTime,
                URIRef('http://linked.data.gov.au/dataset/epochs/trs/aao/' + words[0])  # a ProperInterval in Epochs
            ))

            g.add((
                this_aao,
                OWL.seeAlso,
                URIRef(words[3].strip())
            ))

    with open('aaos.ttl', 'w') as f:
        f.write(g.serialize(format='turtle').decode('utf-8'))


def make_matters():
    g = Graph()
    add_namespaces(g)

    #with open('aaos_matters.csv', 'r', encoding='utf-8') as f:
    with open('matters_clean.csv') as f:
        lines = csv.reader(f, delimiter=',', quotechar='"')
        for line in lines:
            words = line

            # word[0] - AAO ID
            # word[1] - Department text
            # word[2] - Matter text

            this_aao_uri = URIRef(AAOS + 'aao/' + words[0])
            this_department_text = words[1]
            this_department_uri = URIRef(AAOS + 'department/' + str(get_department_number(this_department_text)))
            this_department_class = URIRef('http://test.linked.data.gov.au/def/aaos/Department')
            this_matter_text = words[2]
            this_matter_uri = URIRef(AAOS + 'matter/' + str(get_matter_number(this_matter_text)))
            this_matter_class = URIRef('http://test.linked.data.gov.au/def/aaos/Matter')

            g.add((
                this_aao_uri,
                AAO.hasMatter,
                this_matter_uri
            ))

            g.add((
                this_matter_uri,  # a Matter within the Matters register within the AAOs dataset
                RDF.type,  # a Matter is of type...
                this_matter_class  # of type Matter, as defined in the AAOs ontology
            ))

            g.add((
                this_matter_uri,
                DCT.title,
                Literal(this_matter_text)
            ))

            g.add((
                this_matter_uri,
                AAO.hasDepartment,
                this_department_uri
            ))

            g.add((
                this_department_uri,
                DCT.title,
                Literal(this_department_text.title())
            ))

            g.add((
                this_department_uri,
                RDF.type,
                this_department_class
            ))

    with open('matters.ttl', 'w') as f:
        f.write(g.serialize(format='turtle').decode('utf-8'))


if __name__ == '__main__':
    make_aaos()
    # make_matters_relationships()

    #print(get_dept_number('THE DEPARTMENT OF HUMAN SERVICES (Part of the Social Services Portfolio)'))

    # test_matter_number()

    make_aaos()
