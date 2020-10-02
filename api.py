import COVID19Py

correspondence = {
   "Thailand":0,
   "Japan":1,
   "Singapore":2,
   "Nepal":3,
   "Malaysia":4,
   "British Columbia, CA":5,
   "New South Wales, AU":6,
   "Victoria, AU":7,
   "Queensland, AU":8,
   "Cambodia":9,
   "Sri Lanka":10,
   "Germany":11,
   "Finland":12,
   "United Arab Emirates":13,
   "Philippines":14,
   "India":15,
   "Italy":16,
   "Sweden":17,
   "Spain":18,
   "South Australia, AU":19,
   "Belgium":20,
   "Egypt":21,
   "From Diamond Princess, AU":22,
   "Lebanon":23,
   "Iraq":24,
   "Oman":25,
   "Afghanistan":26,
   "Bahrain":27,
   "Kuwait":28,
   "Algeria":29,
   "Croatia":30,
   "Switzerland":31,
   "Austria":32,
   "Israel":33,
   "Pakistan":34,
   "Brazil":35,
   "Georgia":36,
   "Greece":37,
   "North Macedonia":38,
   "Norway":39,
   "Romania":40,
   "Estonia":41,
   "San Marino":42,
   "Belarus":43,
   "Iceland":44,
   "Lithuania":45,
   "Mexico":46,
   "New Zealand":47,
   "Nigeria":48,
   "Western Australia, AU":49,
   "Ireland":50,
   "Luxembourg":51,
   "Monaco":52,
   "Qatar":53,
   "Ecuador":54,
   "Azerbaijan":55,
   "Armenia":56,
   "Dominican Republic":57,
   "Indonesia":58,
   "Portugal":59,
   "Andorra":60,
   "Tasmania, AU":61,
   "Latvia":62,
   "Morocco":63,
   "Saudi Arabia":64,
   "Senegal":65,
   "Argentina":66,
   "Chile":67,
   "Jordan":68,
   "Ukraine":69,
   "Hungary":70,
   "Northern Territory, AU":71,
   "Liechtenstein":72,
   "Poland":73,
   "Tunisia":74,
   "Bosnia and Herzegovina":75,
   "Slovenia":76,
   "South Africa":77,
   "Bhutan":78,
   "Cameroon":79,
   "Colombia":80,
   "Costa Rica":81,
   "Peru":82,
   "Serbia":83,
   "Slovakia":84,
   "Togo":85,
   "Malta":86,
   "Martinique":87,
   "Bulgaria":88,
   "Maldives":89,
   "Bangladesh":90,
   "Paraguay":91,
   "Ontario, CA":92,
   "Alberta, CA":93,
   "Quebec, CA":94,
   "Albania":95,
   "Cyprus":96,
   "Brunei":97,
   "Washington, US":98,
   "New York, US":99,
   "California, US":100,
   "Massachusetts, US":101,
   "Diamond Princess, US":102,
   "Grand Princess, US":103,
   "Georgia, US":104,
   "Colorado, US":105,
   "Florida, US":106,
   "New Jersey, US":107,
   "Oregon, US":108,
   "Texas, US":109,
   "Illinois, US":110,
   "Pennsylvania, US":111,
   "Iowa, US":112,
   "Maryland, US":113,
   "North Carolina, US":114,
   "South Carolina, US":115,
   "Tennessee, US":116,
   "Virginia, US":117,
   "Arizona, US":118,
   "Indiana, US":119,
   "Kentucky, US":120,
   "District of Columbia, US":121,
   "Nevada, US":122,
   "New Hampshire, US":123,
   "Minnesota, US":124,
   "Nebraska, US":125,
   "Ohio, US":126,
   "Rhode Island, US":127,
   "Wisconsin, US":128,
   "Connecticut, US":129,
   "Hawaii, US":130,
   "Oklahoma, US":131,
   "Utah, US":132,
   "Burkina Faso":133,
   "Holy See":134,
   "Mongolia":135,
   "Panama":136,
   "Kansas, US":137,
   "Louisiana, US":138,
   "Missouri, US":139,
   "Vermont, US":140,
   "Alaska, US":141,
   "Arkansas, US":142,
   "Delaware, US":143,
   "Idaho, US":144,
   "Maine, US":145,
   "Michigan, US":146,
   "Mississippi, US":147,
   "Montana, US":148,
   "New Mexico, US":149,
   "North Dakota, US":150,
   "South Dakota, US":151,
   "West Virginia, US":152,
   "Wyoming, US":153,
   "Hubei, CN":154,
   "Iran":155,
   "Korea, South":156,
   "France, FR":157,
   "Guangdong, CN":158,
   "Henan, CN":159,
   "Zhejiang, CN":160,
   "Hunan, CN":161,
   "Anhui, CN":162,
   "Jiangxi, CN":163,
   "Shandong, CN":164,
   "Diamond Princess, XX":165,
   "Jiangsu, CN":166,
   "Chongqing, CN":167,
   "Sichuan, CN":168,
   "Heilongjiang, CN":169,
   "Denmark, DK":170,
   "Beijing, CN":171,
   "Shanghai, CN":172,
   "Hebei, CN":173,
   "Fujian, CN":174,
   "Guangxi, CN":175,
   "Shaanxi, CN":176,
   "Yunnan, CN":177,
   "Hainan, CN":178,
   "Guizhou, CN":179,
   "Tianjin, CN":180,
   "Shanxi, CN":181,
   "Gansu, CN":182,
   "Hong Kong, CN":183,
   "Liaoning, CN":184,
   "Jilin, CN":185,
   "Czechia":186,
   "Xinjiang, CN":187,
   "Inner Mongolia, CN":188,
   "Ningxia, CN":189,
   "Taiwan*":190,
   "Vietnam":191,
   "Russia":192,
   "Qinghai, CN":193,
   "Macau, CN":194,
   "Moldova":195,
   "Bolivia":196,
   "Faroe Islands, DK":197,
   "St Martin, FR":198,
   "Honduras":199,
   "Channel Islands, GB":200,
   "New Brunswick, CA":201,
   "Tibet, CN":202,
   "Congo (Kinshasa)":203,
   "Cote d'Ivoire":204,
   "Saint Barthelemy, FR":205,
   "Jamaica":206,
   "Turkey":207,
   "Gibraltar, GB":208,
   "Kitsap, WA, US":209,
   "Solano, CA, US":210,
   "Santa Cruz, CA, US":211,
   "Napa, CA, US":212,
   "Ventura, CA, US":213,
   "Worcester, MA, US":214,
   "Gwinnett, GA, US":215,
   "DeKalb, GA, US":216,
   "Floyd, GA, US":217,
   "Fayette, GA, US":218,
   "Gregg, TX, US":219,
   "Monmouth, NJ, US":220,
   "Burlington, NJ, US":221,
   "Camden, NJ, US":222,
   "Passaic, NJ, US":223,
   "Union, NJ, US":224,
   "Eagle, CO, US":225,
   "Larimer, CO, US":226,
   "Arapahoe, CO, US":227,
   "Gunnison, CO, US":228,
   "Kane, IL, US":229,
   "Monroe, PA, US":230,
   "Philadelphia, PA, US":231,
   "Norfolk, VA, US":232,
   "Arlington, VA, US":233,
   "Spotsylvania, VA, US":234,
   "Loudoun, VA, US":235,
   "Prince George's, MD, US":236,
   "Pottawattamie, IA, US":237,
   "Camden, NC, US":238,
   "Pima, AZ, US":239,
   "Noble, IN, US":240,
   "Adams, IN, US":241,
   "Boone, IN, US":242,
   "Dane, WI, US":243,
   "Pierce, WI, US":244,
   "Cuyahoga, OH, US":245,
   "Weber, UT, US":246,
   "Bennington County, VT, US":247,
   "Carver County, MN, US":248,
   "Charlotte County, FL, US":249,
   "Cherokee County, GA, US":250,
   "Collin County, TX, US":251,
   "Jefferson County, KY, US":252,
   "Jefferson Parish, LA, US":253,
   "Shasta County, CA, US":254,
   "Spartanburg County, SC, US":255,
   "Harrison County, KY, US":256,
   "Johnson County, IA, US":257,
   "Berkshire County, MA, US":258,
   "Davidson County, TN, US":259,
   "Douglas County, OR, US":260,
   "Fresno County, CA, US":261,
   "Harford County, MD, US":262,
   "Hendricks County, IN, US":263,
   "Hudson County, NJ, US":264,
   "Johnson County, KS, US":265,
   "Kittitas County, WA, US":266,
   "Manatee County, FL, US":267,
   "Marion County, OR, US":268,
   "Okaloosa County, FL, US":269,
   "Polk County, GA, US":270,
   "Riverside County, CA, US":271,
   "Shelby County, TN, US":272,
   "St, Louis County, MO, US":273,
   "Suffolk County, NY, US":274,
   "Ulster County, NY, US":275,
   "Volusia County, FL, US":276,
   "Fairfax County, VA, US":277,
   "Rockingham County, NH, US":278,
   "Washington, DC, US":279,
   "Montgomery County, PA, US":280,
   "Alameda County, CA, US":281,
   "Broward County, FL, US":282,
   "Lee County, FL, US":283,
   "Pinal County, AZ, US":284,
   "Rockland County, NY, US":285,
   "Saratoga County, NY, US":286,
   "Charleston County, SC, US":287,
   "Clark County, WA, US":288,
   "Cobb County, GA, US":289,
   "Davis County, UT, US":290,
   "El Paso County, CO, US":291,
   "Honolulu County, HI, US":292,
   "Jackson County, OR, US":293,
   "Jefferson County, WA, US":294,
   "Kershaw County, SC, US":295,
   "Klamath County, OR, US":296,
   "Madera County, CA, US":297,
   "Pierce County, WA, US":298,
   "Tulsa County, OK, US":299,
   "Douglas County, CO, US":300,
   "Providence County, RI, US":301,
   "Chatham County, NC, US":302,
   "Delaware County, PA, US":303,
   "Douglas County, NE, US":304,
   "Fayette County, KY, US":305,
   "Marion County, IN, US":306,
   "Middlesex County, MA, US":307,
   "Nassau County, NY, US":308,
   "Ramsey County, MN, US":309,
   "Washoe County, NV, US":310,
   "Wayne County, PA, US":311,
   "Yolo County, CA, US":312,
   "Santa Clara County, CA, US":313,
   "Clark County, NV, US":314,
   "Fort Bend County, TX, US":315,
   "Grant County, WA, US":316,
   "Santa Rosa County, FL, US":317,
   "Williamson County, TN, US":318,
   "New York County, NY, US":319,
   "Montgomery County, MD, US":320,
   "Suffolk County, MA, US":321,
   "Denver County, CO, US":322,
   "Summit County, CO, US":323,
   "Bergen County, NJ, US":324,
   "Harris County, TX, US":325,
   "San Francisco County, CA, US":326,
   "Contra Costa County, CA, US":327,
   "Orange County, CA, US":328,
   "Norfolk County, MA, US":329,
   "Maricopa County, AZ, US":330,
   "Wake County, NC, US":331,
   "Westchester County, NY, US":332,
   "Grafton County, NH, US":333,
   "Hillsborough, FL, US":334,
   "Placer County, CA, US":335,
   "San Mateo, CA, US":336,
   "Sonoma County, CA, US":337,
   "Umatilla, OR, US":338,
   "Fulton County, GA, US":339,
   "Washington County, OR, US":340,
   "Snohomish County, WA, US":341,
   "Humboldt County, CA, US":342,
   "Sacramento County, CA, US":343,
   "San Diego County, CA, US":344,
   "San Benito, CA, US":345,
   "Los Angeles, CA, US":346,
   "King County, WA, US":347,
   "Cook County, IL, US":348,
   "Skagit, WA, US":349,
   "Thurston, WA, US":350,
   "Island, WA, US":351,
   "Whatcom, WA, US":352,
   "Marin, CA, US":353,
   "Calaveras, CA, US":354,
   "Stanislaus, CA, US":355,
   "San Joaquin, CA, US":356,
   "Essex, MA, US":357,
   "Charlton, GA, US":358,
   "Collier, FL, US":359,
   "Pinellas, FL, US":360,
   "Alachua, FL, US":361,
   "Nassau, FL, US":362,
   "Pasco, FL, US":363,
   "Dallas, TX, US":364,
   "Tarrant, TX, US":365,
   "Montgomery, TX, US":366,
   "Middlesex, NJ, US":367,
   "Jefferson, CO, US":368,
   "Multnomah, OR, US":369,
   "Polk, OR, US":370,
   "Deschutes, OR, US":371,
   "McHenry, IL, US":372,
   "Lake, IL, US":373,
   "Bucks, PA, US":374,
   "Hanover, VA, US":375,
   "Lancaster, SC, US":376,
   "Sullivan, TN, US":377,
   "Johnson, IN, US":378,
   "Howard, IN, US":379,
   "St, Joseph, IN, US":380,
   "Knox, NE, US":381,
   "Stark, OH, US":382,
   "Anoka, MN, US":383,
   "Olmsted, MN, US":384,
   "Summit, UT, US":385,
   "Fairfield, CT, US":386,
   "Litchfield, CT, US":387,
   "Orleans, LA, US":388,
   "Pennington, SD, US":389,
   "Beadle, SD, US":390,
   "Charles Mix, SD, US":391,
   "Davison, SD, US":392,
   "Minnehaha, SD, US":393,
   "Bon Homme, SD, US":394,
   "Socorro, NM, US":395,
   "Bernalillo, NM, US":396,
   "Oakland, MI, US":397,
   "Wayne, MI, US":398,
   "New Castle, DE, US":399,
   "Cuba":400,
   "Guyana":401,
   "Australian Capital Territory, AU":402,
   "United Kingdom, GB":403,
   "Kazakhstan":404,
   "French Polynesia, FR":405,
   "Manitoba, CA":406,
   "Saskatchewan, CA":407,
   "Ethiopia":408,
   "Sudan":409,
   "Guinea":410,
   "Grand Princess, CA":411,
   "Kenya":412,
   "Antigua and Barbuda":413,
   "Alabama, US":414,
   "Uruguay":415,
   "Ghana":416,
   "Puerto Rico, US":417,
   "Namibia":418,
   "Seychelles":419,
   "Trinidad and Tobago":420,
   "Venezuela":421,
   "Eswatini":422,
   "Gabon":423,
   "Guatemala":424,
   "Mauritania":425,
   "Rwanda":426,
   "Saint Lucia":427,
   "Saint Vincent and the Grenadines":428,
   "Suriname":429,
   "French Guiana, FR":430,
   "Guam, US":431,
   "Kosovo":432,
   "Newfoundland and Labrador, CA":433,
   "Prince Edward Island, CA":434,
   "Central African Republic":435,
   "Congo (Brazzaville)":436,
   "Equatorial Guinea":437,
   "Mayotte, FR":438,
   "Uzbekistan":439,
   "Netherlands, NL":440,
   "Nova Scotia, CA":441,
   "Guadeloupe, FR":442,
   "Benin":443,
   "Greenland":444,
   "Liberia":445,
   "Curacao, NL":446,
   "Somalia":447,
   "Tanzania":448,
   "The Bahamas":449,
   "Virgin Islands, US":450,
   "Cayman Islands, GB":451,
   "Reunion, FR":452,
   "Barbados":453,
   "Montenegro":454,
   "Kyrgyzstan":455,
   "Mauritius":456,
   "Aruba, NL":457,
   "Zambia":458,
   "Djibouti":459,
   "Gambia, The":460,
   "Montserrat, GB":461
}

def get_world_cases():
    covid19 = COVID19Py.COVID19(url="https://cvtapi.nl")
    data = covid19.getLatest()
    return data['confirmed'], data['deaths'], data['recovered']

def get_country_id(name: str):
    return correspondence[name]

def get_country_stats(c_id: int):
    covid19 = COVID19Py.COVID19(url="https://cvtapi.nl")
    data = covid19.getLocationById(c_id)
    return data['latest']['confirmed'], data['latest']['deaths'], data['latest']['recovered']

def get_country_list():
    l = ["World"]
    for i in correspondence:
        l.append(i.replace('.', ','))
    return l
