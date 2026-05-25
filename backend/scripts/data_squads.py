"""
data_squads.py
--------------
Official World Cup 2026 squad data, structured by group then by position.
Sources: FOX Sports, Sky Sports, ESPN, Olympics.com (scraped May 17, 2026).

STATUS KEY:
  "final"       - official 26-man squad submitted
  "preliminary" - provisional list (final due June 1, 2026)
  "pending"     - not yet announced

Each player entry: {"name": str, "club": str}
"""

SQUADS = {

    # =========================================================================
    # GROUP A
    # =========================================================================

    "Mexico": {
        "status": "preliminary",
        "squad": {
            "goalkeepers": [
                {"name": "Alex Padilla",        "club": "Athletic Club"},
                {"name": "Antonio Rodriguez",   "club": "Tijuana"},
                {"name": "Carlos Acevedo",      "club": "Santos Laguna"},
                {"name": "Carlos Moreno",       "club": "Pachuca"},
                {"name": "Guillermo Ochoa",     "club": "AEL Limassol"},
                {"name": "Raul Rangel",         "club": "Chivas"},
            ],
            "defenders": [
                {"name": "Bryan Gonzalez",      "club": "Chivas"},
                {"name": "Cesar Montes",        "club": "Lokomotiv Moscow"},
                {"name": "Edson Alvarez",       "club": "Fenerbahce"},
                {"name": "Eduardo Aguila",      "club": "Atletico de San Luis"},
                {"name": "Everardo Lopez",      "club": "Toluca"},
                {"name": "Israel Reyes",        "club": "America"},
                {"name": "Jesus Angulo",        "club": "Tigres"},
                {"name": "Jesus Gallardo",      "club": "Toluca"},
                {"name": "Johan Vasquez",       "club": "Genoa"},
                {"name": "Jorge Sanchez",       "club": "PAOK"},
                {"name": "Julian Araujo",       "club": "Celtic"},
                {"name": "Richard Ledezma",     "club": "Chivas"},
            ],
            "midfielders": [
                {"name": "Alexis Gutierrez",    "club": "America"},
                {"name": "Alvaro Fidalgo",      "club": "Real Betis"},
                {"name": "Brian Gutierrez",     "club": "Chivas"},
                {"name": "Diego Lainez",        "club": "Tigres"},
                {"name": "Efrain Alvarez",      "club": "Chivas"},
                {"name": "Luis Chavez",         "club": "Dinamo Moscow"},
                {"name": "Obed Vargas",         "club": "Atletico de Madrid"},
                {"name": "Orbelin Pineda",      "club": "AEK"},
                {"name": "Erick Sanchez",       "club": "America"},
            ],
            "forwards": [
                {"name": "Alexis Vega",         "club": "Toluca"},
                {"name": "Armando Gonzalez",    "club": "Chivas"},
                {"name": "Cesar Huerta",        "club": "Anderlecht"},
                {"name": "German Berterame",    "club": "Inter Miami"},
                {"name": "Julian Quinones",     "club": "Al-Qadisiyah"},
                {"name": "Raul Jimenez",        "club": "Fulham"},
                {"name": "Santiago Gimenez",    "club": "AC Milan"},
            ],
        },
    },

    "South Africa": {"status": "pending", "squad": {}},

    "South Korea": {
        "status": "final",
        "squad": {
            "goalkeepers": [
                {"name": "Kim Seung-gyu",       "club": "FC Tokyo"},
                {"name": "Jo Hyeon-woo",        "club": "Ulsan HD"},
                {"name": "Song Bum-keun",       "club": "Jeonbuk Hyundai Motors"},
            ],
            "defenders": [
                {"name": "Kim Min-jae",         "club": "Bayern Munich"},
                {"name": "Kim Moon-hwan",       "club": "Daejeon Hana Citizen"},
                {"name": "Seol Young-woo",      "club": "Red Star Belgrade"},
                {"name": "Cho Yu-min",          "club": "Sharjah"},
                {"name": "Lee Tae-seok",        "club": "Austria Wien"},
                {"name": "Park Jin-seob",       "club": "Zhejiang FC"},
                {"name": "Kim Tae-hyeon",       "club": "Kashima Antlers"},
                {"name": "Lee Han-beom",        "club": "Midtjylland"},
                {"name": "Jens Castrop",        "club": "Borussia Monchengladbach"},
                {"name": "Lee Ki-hyuk",         "club": "Gangwon FC"},
            ],
            "midfielders": [
                {"name": "Lee Jae-sung",        "club": "Mainz 05"},
                {"name": "Hwang Hee-chan",      "club": "Wolverhampton Wanderers"},
                {"name": "Hwang In-beom",       "club": "Feyenoord"},
                {"name": "Lee Kang-in",         "club": "Paris Saint-Germain"},
                {"name": "Paik Seung-ho",       "club": "Birmingham City"},
                {"name": "Kim Jin-gyu",         "club": "Jeonbuk Hyundai Motors"},
                {"name": "Lee Dong-gyeong",     "club": "Ulsan HD"},
                {"name": "Bae Jun-ho",          "club": "Stoke City"},
            ],
            "forwards": [
                {"name": "Son Heung-min",       "club": "Tottenham Hotspur"},
                {"name": "Oh Hyeon-gyu",        "club": "Celtic"},
                {"name": "Cho Gue-sung",        "club": "Jeonbuk Hyundai Motors"},
                {"name": "Yang Min-hyeok",      "club": "Bayer Leverkusen"},
            ],
        },
    },

    "Czechia": {
        "status": "preliminary",
        "squad": {
            "goalkeepers": [
                {"name": "Antonin Kinsky",      "club": "Tottenham Hotspur"},
                {"name": "Jindrich Stanek",     "club": "Slavia Prague"},
                {"name": "Matej Kovar",         "club": "PSV Eindhoven"},
            ],
            "defenders": [
                {"name": "Vladimir Coufal",     "club": "TSG Hoffenheim"},
                {"name": "David Doudera",       "club": "Slavia Prague"},
                {"name": "Tomas Holes",         "club": "Slavia Prague"},
                {"name": "Robin Hranac",        "club": "TSG Hoffenheim"},
                {"name": "David Jurasek",       "club": "Slavia Prague"},
                {"name": "Ladislav Krejci",     "club": "Wolverhampton Wanderers"},
                {"name": "Martin Vitik",        "club": "Bologna"},
                {"name": "David Zima",          "club": "Slavia Prague"},
            ],
            "midfielders": [
                {"name": "Pavel Bucha",         "club": "FC Cincinnati"},
                {"name": "Adam Karabec",        "club": "Lyon"},
                {"name": "Lukas Provod",        "club": "Slavia Prague"},
                {"name": "Tomas Soucek",        "club": "West Ham United"},
                {"name": "Pavel Sulc",          "club": "Lyon"},
                {"name": "Michal Sadilek",      "club": "Slavia Prague"},
            ],
            "forwards": [
                {"name": "Patrik Schick",       "club": "Bayer Leverkusen"},
                {"name": "Adam Hlozek",         "club": "TSG Hoffenheim"},
                {"name": "Tomas Chory",         "club": "Slavia Prague"},
                {"name": "Jan Kuchta",          "club": "Sparta Prague"},
                {"name": "Matej Vydra",         "club": "Viktoria Plzen"},
            ],
        },
    },

    # =========================================================================
    # GROUP B
    # =========================================================================

    "Canada":                   {"status": "pending", "squad": {}},

    "Bosnia and Herzegovina": {
        "status": "final",
        "squad": {
            "goalkeepers": [
                {"name": "Nikola Vasilj",           "club": "FC St. Pauli"},
                {"name": "Martin Zlomislic",        "club": "HNK Rijeka"},
                {"name": "Osman Hadzikic",          "club": "Slaven Belupo"},
            ],
            "defenders": [
                {"name": "Sead Kolasinac",          "club": "Atalanta"},
                {"name": "Amar Dedic",              "club": "Benfica"},
                {"name": "Nihad Mujakic",           "club": "Gaziantep"},
                {"name": "Nikola Katic",            "club": "Schalke 04"},
                {"name": "Tarik Muharemovic",       "club": "Sassuolo"},
                {"name": "Stjepan Radeljic",        "club": "HNK Rijeka"},
                {"name": "Dennis Hadzikadunic",     "club": "Sampdoria"},
                {"name": "Nidal Celik",             "club": "Lens"},
            ],
            "midfielders": [
                {"name": "Amir Hadziahmetovic",     "club": "Hull City"},
                {"name": "Ivan Sunjic",             "club": "Pafos"},
                {"name": "Ivan Basic",              "club": "Astana"},
                {"name": "Dzenis Burnic",           "club": "Karlsruher SC"},
                {"name": "Ermin Mahmic",            "club": "Slovan Liberec"},
                {"name": "Benjamin Tahirovic",      "club": "Brondby"},
                {"name": "Amar Memic",              "club": "Viktoria Plzen"},
                {"name": "Armin Gigovic",           "club": "Young Boys"},
                {"name": "Kerim Alajbegovic",       "club": "Red Bull Salzburg"},
                {"name": "Esmir Bajraktarevic",     "club": "PSV Eindhoven"},
            ],
            "forwards": [
                {"name": "Edin Dzeko",              "club": "Schalke 04"},
                {"name": "Ermedin Demirovic",       "club": "VfB Stuttgart"},
                {"name": "Samed Bazdar",            "club": "Jagiellonia Bialystok"},
                {"name": "Haris Tabakovic",         "club": "Borussia Monchengladbach"},
                {"name": "Jovo Lukic",              "club": "Universitatea Cluj"},
            ],
        },
    },

    "Qatar": {
        "status": "preliminary",
        "squad": {
            "goalkeepers": [
                {"name": "Meshaal Barsham",     "club": "Al Sadd"},
                {"name": "Salah Zakaria",       "club": "Al Duhail"},
                {"name": "Mahmoud Abunada",     "club": "Al Rayyan"},
                {"name": "Shehab Elleithy",     "club": "Al Shahania"},
            ],
            "defenders": [
                {"name": "Boualem Khoukhi",     "club": "Al Sadd"},
                {"name": "Pedro Miguel",        "club": "Al Sadd"},
                {"name": "Sultan Al Brake",     "club": "Al Duhail"},
                {"name": "Tarek Salman",        "club": "Al Sadd"},
                {"name": "Bassam Al-Rawi",      "club": "Al Duhail"},
                {"name": "Lucas Mendes",        "club": "Al Wakrah"},
                {"name": "Ayoub Al-Alawi",      "club": "Al Gharafa"},
                {"name": "Niall Mason",         "club": "Qatar SC"},
            ],
            "midfielders": [
                {"name": "Abdulaziz Hatem",     "club": "Al Rayyan"},
                {"name": "Karim Boudiaf",       "club": "Al Duhail"},
                {"name": "Assim Madibo",        "club": "Al Wakrah"},
                {"name": "Jassim Gaber",        "club": "Al Rayyan"},
                {"name": "Homam Al-Amin",       "club": "Cultural Leonesa"},
            ],
            "forwards": [
                {"name": "Hassan Al-Haydos",    "club": "Al Sadd"},
                {"name": "Akram Afif",          "club": "Al Sadd"},
                {"name": "Almoez Ali",          "club": "Al Duhail"},
                {"name": "Edmilson Junior",     "club": "Al Duhail"},
                {"name": "Sebastian Soria",     "club": "Qatar SC"},
                {"name": "Mohammed Muntari",    "club": "Al Gharafa"},
            ],
        },
    },

    "Switzerland":              {"status": "pending", "squad": {}},

    # =========================================================================
    # GROUP C
    # =========================================================================

    "Brazil": {
        "status": "final",
        "squad": {
            "goalkeepers": [
                {"name": "Alisson",             "club": "Liverpool"},
                {"name": "Éderson",             "club": "Fenerbahce"},
                {"name": "Weverton",            "club": "Grêmio"},
            ],
            "defenders": [
                {"name": "Alex Sandro",         "club": "Flamengo"},
                {"name": "Bremer",              "club": "Juventus"},
                {"name": "Danilo",              "club": "Flamengo"},
                {"name": "Douglas Santos",      "club": "Zenit St. Petersburg"},
                {"name": "Gabriel Magalhães",   "club": "Arsenal"},
                {"name": "Léo Pereira",         "club": "Flamengo"},
                {"name": "Marquinhos",          "club": "Paris Saint-Germain"},
                {"name": "Roger Ibañez",        "club": "Al Ahli"},
                {"name": "Wesley",              "club": "AS Roma"},
            ],
            "midfielders": [
                {"name": "Bruno Guimarães",     "club": "Newcastle United"},
                {"name": "Casemiro",            "club": "Manchester United"},
                {"name": "Danilo Santos",       "club": "Botafogo"},
                {"name": "Fabinho",             "club": "Al Ittihad"},
                {"name": "Lucas Paquetá",       "club": "Flamengo"},
            ],
            "forwards": [
                {"name": "Endrick",             "club": "Lyon"},
                {"name": "Gabriel Martinelli",  "club": "Arsenal"},
                {"name": "Igor Thiago",         "club": "Brentford"},
                {"name": "Luiz Henrique",       "club": "Zenit St. Petersburg"},
                {"name": "Matheus Cunha",       "club": "Manchester United"},
                {"name": "Neymar",              "club": "Santos"},
                {"name": "Raphinha",            "club": "Barcelona"},
                {"name": "Rayan",               "club": "Bournemouth"},
                {"name": "Vinícius Júnior",     "club": "Real Madrid"},
            ],
        },
    },
    "Morocco":                  {"status": "pending", "squad": {}},
    "Haiti": {
        "status": "final",
        "squad": {
            "goalkeepers": [
                {"name": "Johny Placide",         "club": "Bastia"},
                {"name": "Alexandre Pierre",      "club": "Sochaux"},
                {"name": "Josue Duverger",        "club": "Cosmos Koblenz"},
            ],
            "defenders": [
                {"name": "Carlens Arcus",         "club": "Angers"},
                {"name": "Wilguens Paugain",      "club": "Zulte Waregem"},
                {"name": "Duke Lacroix",          "club": "Colorado Springs Switchbacks"},
                {"name": "Martin Expérience",     "club": "Nancy"},
                {"name": "Jean-Kévin Duverne",    "club": "Gent"},
                {"name": "Ricardo Adé",           "club": "LDU Quito"},
                {"name": "Hannes Delcroix",       "club": "Lugano"},
                {"name": "Keeto Thermoncy",       "club": "Young Boys"},
            ],
            "midfielders": [
                {"name": "Carl Fred Sainté",      "club": "El Paso Locomotive"},
                {"name": "Leverton Pierre",       "club": "Vizela"},
                {"name": "Danley Jean Jacques",   "club": "Philadelphia Union"},
                {"name": "Jean-Ricner Bellegarde","club": "Wolverhampton Wanderers"},
                {"name": "Woodensky Pierre",      "club": "Violette"},
                {"name": "Dominique Simon",       "club": "FC Tatran Prešov"},
            ],
            "forwards": [
                {"name": "Don Deedson Louicius",  "club": "FC Dallas"},
                {"name": "Josué Casimir",         "club": "Auxerre"},
                {"name": "Derrick Etienne",       "club": "Toronto FC"},
                {"name": "Ruben Providence",      "club": "Almere"},
                {"name": "Duckens Nazon",         "club": "Esteghlal"},
                {"name": "Frantzdy Pierrot",      "club": "Çaykur Rizespor"},
                {"name": "Wilson Isidor",         "club": "Sunderland"},
                {"name": "Yassin Fortuné",        "club": "Vizela"},
                {"name": "Lenny Joseph",          "club": "Ferencváros"},
            ],
        },
    },
    "Scotland": {
        "status": "final",
        "squad": {
            "goalkeepers": [
                {"name": "Craig Gordon",          "club": "Hearts"},
                {"name": "Angus Gunn",            "club": "Nottingham Forest"},
                {"name": "Liam Kelly",            "club": "Rangers"},
            ],
            "defenders": [
                {"name": "Grant Hanley",          "club": "Hibernian"},
                {"name": "Jack Hendry",           "club": "Al Etiffaq"},
                {"name": "Aaron Hickey",          "club": "Brentford"},
                {"name": "Dom Hyam",              "club": "Wrexham"},
                {"name": "Scott McKenna",         "club": "Dinamo Zagreb"},
                {"name": "Nathan Patterson",      "club": "Everton"},
                {"name": "Anthony Ralston",       "club": "Celtic"},
                {"name": "Andy Robertson",        "club": "Liverpool"},
                {"name": "John Souttar",          "club": "Rangers"},
                {"name": "Kieran Tierney",        "club": "Celtic"},
            ],
            "midfielders": [
                {"name": "Ryan Christie",         "club": "Bournemouth"},
                {"name": "Finlay Curtis",         "club": "Kilmarnock"},
                {"name": "Lewis Ferguson",        "club": "Bologna"},
                {"name": "Ben Gannon-Doak",       "club": "Bournemouth"},
                {"name": "Billy Gilmour",         "club": "Napoli"},
                {"name": "John McGinn",           "club": "Aston Villa"},
                {"name": "Kenny McLean",          "club": "Norwich"},
                {"name": "Scott McTominay",       "club": "Napoli"},
            ],
            "forwards": [
                {"name": "Ché Adams",             "club": "Torino"},
                {"name": "Lyndon Dykes",          "club": "Charlton Athletic"},
                {"name": "George Hirst",          "club": "Ipswich"},
                {"name": "Lawrence Shankland",    "club": "Hearts"},
                {"name": "Ross Stewart",          "club": "Southampton"},
            ],
        },
    },

    # =========================================================================
    # GROUP D
    # =========================================================================

    "United States":            {"status": "pending", "squad": {}},

    "Paraguay": {
        "status": "preliminary",
        "squad": {
            "goalkeepers": [
                {"name": "Roberto Fernandez",   "club": "Cerro Porteno"},
                {"name": "Orlando Gill",        "club": "San Lorenzo"},
                {"name": "Carlos Coronel",      "club": "Sao Paulo"},
            ],
            "defenders": [
                {"name": "Gustavo Gomez",       "club": "Palmeiras"},
                {"name": "Junior Alonso",       "club": "Atletico Mineiro"},
                {"name": "Fabian Balbuena",     "club": "Gremio"},
                {"name": "Omar Alderete",       "club": "Sunderland"},
                {"name": "Blas Riveros",        "club": "Cerro Porteno"},
                {"name": "Mateo Gamarra",       "club": "Cruzeiro"},
                {"name": "Diego Leon",          "club": "Manchester United"},
            ],
            "midfielders": [
                {"name": "Miguel Almeron",      "club": "Atlanta United"},
                {"name": "Mathias Villasanti",  "club": "Gremio"},
                {"name": "Andres Cubas",        "club": "Vancouver Whitecaps"},
                {"name": "Ramon Sosa",          "club": "Palmeiras"},
                {"name": "Diego Gomez",         "club": "Brighton & Hove Albion"},
                {"name": "Braian Ojeda",        "club": "Orlando City"},
                {"name": "Matias Galarza",      "club": "Atlanta United"},
                {"name": "Enso Gonzalez",       "club": "Wolverhampton Wanderers"},
            ],
            "forwards": [
                {"name": "Oscar Romero",        "club": "Huracan"},
                {"name": "Angel Romero",        "club": "Boca Juniors"},
                {"name": "Antonio Sanabria",    "club": "Cremonese"},
                {"name": "Julio Enciso",        "club": "Strasbourg"},
                {"name": "Adam Bareiro",        "club": "Boca Juniors"},
                {"name": "Rodney Redes",        "club": "LDU Quito"},
            ],
        },
    },

    "Australia":                {"status": "pending", "squad": {}},
    "Turkiye":                  {"status": "pending", "squad": {}},

    # =========================================================================
    # GROUP E
    # =========================================================================

    "Germany":                  {"status": "pending", "squad": {}},
    "Curacao":                  {"status": "pending", "squad": {}},
    "Cote d'Ivoire": {
        "status": "final",
        "squad": {
            "goalkeepers": [
                {"name": "Yahia Fofana",           "club": "Rizespor"},
                {"name": "Mohomed Koné",           "club": "Charleroi"},
                {"name": "Alban Lafont",           "club": "Panathinaikos"},
            ],
            "defenders": [
                {"name": "Emmanuel Agbadou",       "club": "Beşiktaş"},
                {"name": "Clément Akpa",           "club": "AJ Auxerre"},
                {"name": "Ousmane Diomande",       "club": "Sporting CP"},
                {"name": "Guela Doué",             "club": "Strasbourg"},
                {"name": "Ghislain Konan",         "club": "Gil Vicente"},
                {"name": "Odilon Kossounou",       "club": "Atalanta"},
                {"name": "Evan Ndicka",            "club": "AS Roma"},
                {"name": "Wilfried Singo",         "club": "Galatasaray"},
            ],
            "midfielders": [
                {"name": "Seko Fofana",            "club": "Porto"},
                {"name": "Parfait Guiagon",        "club": "Charleroi"},
                {"name": "Franck Kessié",          "club": "Al Ahli"},
                {"name": "Christ Inao Oulaï",      "club": "Trabzonspor"},
                {"name": "Ibrahim Sangaré",        "club": "Nottingham Forest"},
                {"name": "Jean Michaël Seri",      "club": "NK Maribor"},
            ],
            "forwards": [
                {"name": "Simon Adingra",          "club": "AS Monaco"},
                {"name": "Ange-Yoan Bonny",        "club": "Internazionale"},
                {"name": "Amad Diallo",            "club": "Manchester United"},
                {"name": "Oumar Diakité",          "club": "Cercle Brugge"},
                {"name": "Yan Diomande",           "club": "RB Leipzig"},
                {"name": "Evann Guessand",         "club": "Aston Villa"},
                {"name": "Nicolas Pépé",           "club": "Villarreal"},
                {"name": "Bazoumana Touré",        "club": "Hoffenheim"},
                {"name": "Elye Wahi",              "club": "Nice"},
            ],
        },
    },
    "Ecuador":                  {"status": "pending", "squad": {}},

    # =========================================================================
    # GROUP F
    # =========================================================================

    "Netherlands":              {"status": "pending", "squad": {}},

    "Japan": {
        "status": "final",
        "squad": {
            "goalkeepers": [
                {"name": "Zion Suzuki",         "club": "Parma"},
                {"name": "Kosei Tani",          "club": "Brighton"},
                {"name": "Ayumu Seko",          "club": "Cerezo Osaka"},
            ],
            "defenders": [
                {"name": "Yuto Nagatomo",       "club": "FC Tokyo"},
                {"name": "Shogo Taniguchi",     "club": "Kawasaki Frontale"},
                {"name": "Takehiro Tomiyasu",   "club": "Arsenal"},
                {"name": "Ko Itakura",          "club": "Borussia Monchengladbach"},
                {"name": "Tsuyoshi Watanabe",   "club": "FC Tokyo"},
                {"name": "Hiroki Ito",          "club": "Bayern Munich"},
                {"name": "Junnosuke Suzuki",    "club": "Gamba Osaka"},
                {"name": "Yukinari Sugawara",   "club": "Southampton"},
            ],
            "midfielders": [
                {"name": "Daichi Kamada",       "club": "Crystal Palace"},
                {"name": "Kaishu Sano",         "club": "Stade de Reims"},
                {"name": "Ao Tanaka",           "club": "Leeds United"},
                {"name": "Wataru Endo",         "club": "Liverpool"},
                {"name": "Keito Nakamura",      "club": "Stade de Reims"},
                {"name": "Ritsu Doan",          "club": "SC Freiburg"},
                {"name": "Junya Ito",           "club": "Stade de Reims"},
                {"name": "Takefusa Kubo",       "club": "Real Sociedad"},
            ],
            "forwards": [
                {"name": "Ayase Ueda",          "club": "Feyenoord"},
                {"name": "Koki Ogawa",          "club": "Alaves"},
                {"name": "Daizen Maeda",        "club": "Celtic"},
                {"name": "Yuito Suzuki",        "club": "Shonan Bellmare"},
            ],
        },
    },

    "Sweden": {
        "status": "final",
        "squad": {
            "goalkeepers": [
                {"name": "Viktor Johansson",        "club": "Stoke City"},
                {"name": "Kristoffer Nordfeldt",    "club": "AIK"},
                {"name": "Jacob Widell Zetterstrom","club": "Derby County"},
            ],
            "defenders": [
                {"name": "Victor Lindelof",         "club": "Aston Villa"},
                {"name": "Isak Hien",               "club": "Atalanta"},
                {"name": "Carl Starfelt",           "club": "Celta Vigo"},
                {"name": "Emil Holm",               "club": "Juventus"},
                {"name": "Hjalmar Ekdal",           "club": "Burnley"},
                {"name": "Daniel Svensson",         "club": "Borussia Dortmund"},
                {"name": "Gustaf Lagerbielke",      "club": "Braga"},
                {"name": "Gabriel Gudmundsson",     "club": "Leeds United"},
                {"name": "Eric Smith",              "club": "St. Pauli"},
                {"name": "Elliot Stroud",           "club": "Mjallby AIF"},
            ],
            "midfielders": [
                {"name": "Yasin Ayari",             "club": "Brighton"},
                {"name": "Lucas Bergvall",          "club": "Tottenham Hotspur"},
                {"name": "Jesper Karlstrom",        "club": "Udinese"},
                {"name": "Mattias Svanberg",        "club": "Wolfsburg"},
                {"name": "Besfort Zeneli",          "club": "Union St-Gilloise"},
                {"name": "Ken Sema",                "club": "Pafos"},
                {"name": "Taha Ali",                "club": "Malmo"},
            ],
            "forwards": [
                {"name": "Alexander Isak",          "club": "Liverpool"},
                {"name": "Viktor Gyokeres",         "club": "Arsenal"},
                {"name": "Anthony Elanga",          "club": "Newcastle United"},
                {"name": "Alexander Bernhardsson",  "club": "Holstein Kiel"},
                {"name": "Gustaf Nilsson",          "club": "Club Brugge"},
                {"name": "Benjamin Nygren",         "club": "Celtic"},
            ],
        },
    },

    

    # =========================================================================
    # GROUP G
    # =========================================================================

    "Belgium": {
        "status": "final",
        "squad": {
            "goalkeepers": [
                {"name": "Thibaut Courtois",        "club": "Real Madrid"},
                {"name": "Senne Lammens",           "club": "Manchester United"},
                {"name": "Mike Penders",            "club": "Racing Strasbourg"},
            ],
            "defenders": [
                {"name": "Timothy Castagne",        "club": "Fulham"},
                {"name": "Zeno Debast",             "club": "Sporting CP"},
                {"name": "Maxim de Cuyper",         "club": "Brighton"},
                {"name": "Koni de Winter",          "club": "AC Milan"},
                {"name": "Brandon Mechele",         "club": "Club Brugge"},
                {"name": "Thomas Meunier",          "club": "Lille"},
                {"name": "Arthur Theate",           "club": "Eintracht Frankfurt"},
            ],
            "midfielders": [
                {"name": "Kevin de Bruyne",         "club": "Napoli"},
                {"name": "Amadou Onana",            "club": "Aston Villa"},
                {"name": "Nicolas Raskin",          "club": "Rangers"},
                {"name": "Youri Tielemans",         "club": "Aston Villa"},
                {"name": "Hans Vanaken",            "club": "Club Brugge"},
                {"name": "Axel Witsel",             "club": "Girona"},
            ],
            "forwards": [
                {"name": "Charles de Ketelaere",    "club": "Atalanta"},
                {"name": "Jeremy Doku",             "club": "Manchester City"},
                {"name": "Romelu Lukaku",           "club": "Napoli"},
                {"name": "Dodi Lukebakio",          "club": "Benfica"},
                {"name": "Alexis Saelemaekers",     "club": "AC Milan"},
                {"name": "Leandro Trossard",        "club": "Arsenal"},
            ],
        },
    },

    "Egypt":                    {"status": "pending", "squad": {}},
    "Iran":                     {"status": "pending", "squad": {}},

    "New Zealand": {
        "status": "final",
        "squad": {
            "goalkeepers": [
                {"name": "Max Crocombe",        "club": "Millwall"},
                {"name": "Alex Paulsen",        "club": "Lechia Gdansk"},
                {"name": "Michael Woud",        "club": "Auckland FC"},
            ],
            "defenders": [
                {"name": "Tim Payne",           "club": "Wellington Phoenix"},
                {"name": "Tyler Bindon",        "club": "Nottingham Forest"},
                {"name": "Michael Boxall",      "club": "Minnesota United"},
                {"name": "Liberato Cacace",     "club": "Wrexham"},
                {"name": "Nando Pijnaker",      "club": "Auckland FC"},
                {"name": "Finn Surman",         "club": "Portland Timbers"},
                {"name": "Tommy Smith",         "club": "Braintree Town"},
            ],
            "midfielders": [
                {"name": "Joe Bell",            "club": "Viking FK"},
                {"name": "Matt Garbett",        "club": "Peterborough United"},
                {"name": "Marko Stamenic",      "club": "Swansea City"},
                {"name": "Sarpreet Singh",      "club": "Wellington Phoenix"},
                {"name": "Alex Rufer",          "club": "Wellington Phoenix"},
                {"name": "Ryan Thomas",         "club": "PEC Zwolle"},
            ],
            "forwards": [
                {"name": "Chris Wood",          "club": "Nottingham Forest"},
                {"name": "Kosta Barbarouses",   "club": "Western Sydney Wanderers"},
                {"name": "Ben Old",             "club": "Saint-Etienne"},
                {"name": "Callum McCowatt",     "club": "Silkeborg IF"},
                {"name": "Ben Waine",           "club": "Port Vale"},
                {"name": "Jesse Randall",       "club": "Auckland FC"},
            ],
        },
    },

    # =========================================================================
    # GROUP H
    # =========================================================================

    "Spain":                    {"status": "pending", "squad": {}},
    "Cabo Verde":               {"status": "pending", "squad": {}},
    "Saudi Arabia":             {"status": "pending", "squad": {}},
    "Uruguay":                  {"status": "pending", "squad": {}},

    # =========================================================================
    # GROUP I
    # =========================================================================

    "France": {
        "status": "final",
        "squad": {
            "goalkeepers": [
                {"name": "Mike Maignan",            "club": "AC Milan"},
                {"name": "Brice Samba",             "club": "Rennes"},
                {"name": "Robin Risser",            "club": "Lens"},
            ],
            "defenders": [
                {"name": "William Saliba",          "club": "Arsenal"},
                {"name": "Ibrahima Konate",         "club": "Liverpool"},
                {"name": "Dayot Upamecano",         "club": "Bayern Munich"},
                {"name": "Jules Kounde",            "club": "Barcelona"},
                {"name": "Maxence Lacroix",         "club": "Crystal Palace"},
                {"name": "Lucas Hernandez",         "club": "Paris Saint-Germain"},
                {"name": "Theo Hernandez",          "club": "Al Hilal"},
                {"name": "Lucas Digne",             "club": "Aston Villa"},
                {"name": "Malo Gusto",              "club": "Chelsea"},
            ],
            "midfielders": [
                {"name": "Aurelien Tchouameni",     "club": "Real Madrid"},
                {"name": "N'Golo Kante",            "club": "Fenerbahce"},
                {"name": "Adrien Rabiot",           "club": "AC Milan"},
                {"name": "Manu Kone",               "club": "AS Roma"},
                {"name": "Warren Zaire-Emery",      "club": "Paris Saint-Germain"},
            ],
            "forwards": [
                {"name": "Kylian Mbappe",           "club": "Real Madrid"},
                {"name": "Ousmane Dembele",         "club": "Paris Saint-Germain"},
                {"name": "Marcus Thuram",           "club": "Inter Milan"},
                {"name": "Michael Olise",           "club": "Bayern Munich"},
                {"name": "Bradley Barcola",         "club": "Paris Saint-Germain"},
                {"name": "Desire Doue",             "club": "Paris Saint-Germain"},
                {"name": "Rayan Cherki",            "club": "Manchester City"},
                {"name": "Jean-Philippe Mateta",    "club": "Crystal Palace"},
                {"name": "Maghnes Akliouche",       "club": "Monaco"},
            ],
        },
    },

    "Senegal":                  {"status": "pending", "squad": {}},
    "Iraq":                     {"status": "pending", "squad": {}},
    "Norway": {
        "status": "final",
        "squad": {
            "goalkeepers": [
                {"name": "Ørjan Nyland",           "club": "Sevilla"},
                {"name": "Egil Selvik",            "club": "Watford"},
                {"name": "Sander Tangvik",         "club": "Hamburg SV"},
            ],
            "defenders": [
                {"name": "Julian Ryerson",         "club": "Borussia Dortmund"},
                {"name": "Kristoffer Ajer",        "club": "Brentford"},
                {"name": "Leo Østigård",           "club": "Genoa"},
                {"name": "David Møller Wolfe",     "club": "Wolverhampton Wanderers"},
                {"name": "Marcus Pedersen",        "club": "Torino"},
                {"name": "Torbjørn Heggem",        "club": "Bologna"},
                {"name": "Fredrik André Bjørkan",  "club": "Bodø/Glimt"},
                {"name": "Henrik Falchener",       "club": "Viking"},
                {"name": "Sondre Langås",          "club": "Derby County"},
            ],
            "midfielders": [
                {"name": "Martin Ødegaard",        "club": "Arsenal"},
                {"name": "Sander Berge",           "club": "Fulham"},
                {"name": "Patrick Berg",           "club": "Bodø/Glimt"},
                {"name": "Kristian Thorstvedt",    "club": "Sassuolo"},
                {"name": "Morten Thorsby",         "club": "Cremonese"},
                {"name": "Thelo Aasgaard",         "club": "Rangers"},
                {"name": "Andreas Schjelderup",    "club": "Benfica"},
                {"name": "Jens Petter Hauge",      "club": "Bodø/Glimt"},
                {"name": "Fredrik Aursnes",        "club": "Benfica"},
                {"name": "Oscar Bobb",             "club": "Fulham"},
                {"name": "Antonio Nusa",           "club": "RB Leipzig"},
            ],
            "forwards": [
                {"name": "Erling Haaland",         "club": "Manchester City"},
                {"name": "Alexander Sørloth",      "club": "Atlético Madrid"},
                {"name": "Jørgen Strand Larsen",   "club": "Crystal Palace"},
            ],
        },
    },

    # =========================================================================
    # GROUP J
    # =========================================================================

    "Argentina": {
        "status": "preliminary",
        "squad": {
            "goalkeepers": [
                {"name": "Emiliano Martinez",       "club": "Aston Villa"},
                {"name": "Geronimo Rulli",          "club": "Olympique de Marseille"},
                {"name": "Juan Musso",              "club": "Atletico de Madrid"},
            ],
            "defenders": [
                {"name": "Lisandro Martinez",       "club": "Manchester United"},
                {"name": "Cristian Romero",         "club": "Tottenham Hotspur"},
                {"name": "Nicolas Otamendi",        "club": "Benfica"},
                {"name": "Gonzalo Montiel",         "club": "River Plate"},
                {"name": "Nahuel Molina",           "club": "Atletico de Madrid"},
                {"name": "Marcos Acuna",            "club": "River Plate"},
                {"name": "Nicolas Tagliafico",      "club": "Olympique Lyonnais"},
                {"name": "Marcos Senesi",           "club": "Bournemouth"},
                {"name": "Lucas Martinez Quarta",   "club": "River Plate"},
                {"name": "Leonardo Balerdi",        "club": "Olympique de Marseille"},
            ],
            "midfielders": [
                {"name": "Alexis Mac Allister",     "club": "Liverpool"},
                {"name": "Rodrigo De Paul",         "club": "Inter Miami"},
                {"name": "Enzo Fernandez",          "club": "Chelsea"},
                {"name": "Leandro Paredes",         "club": "Boca Juniors"},
                {"name": "Giovani Lo Celso",        "club": "Real Betis"},
                {"name": "Alan Varela",             "club": "FC Porto"},
                {"name": "Exequiel Palacios",       "club": "Bayer Leverkusen"},
            ],
            "forwards": [
                {"name": "Lionel Messi",            "club": "Inter Miami"},
                {"name": "Lautaro Martinez",        "club": "Internazionale"},
                {"name": "Julian Alvarez",          "club": "Atletico de Madrid"},
                {"name": "Alejandro Garnacho",      "club": "Chelsea"},
                {"name": "Nicolas Gonzalez",        "club": "Atletico de Madrid"},
                {"name": "Franco Mastantuono",      "club": "Real Madrid"},
                {"name": "Santiago Castro",         "club": "Bologna"},
            ],
        },
    },

    "Algeria":                  {"status": "pending", "squad": {}},
    "Austria":                  {"status": "pending", "squad": {}},
    "Jordan":                   {"status": "pending", "squad": {}},

    # =========================================================================
    # GROUP K
    # =========================================================================

    "Portugal":                 {"status": "pending", "squad": {}},
    "DR Congo":                 {"status": "pending", "squad": {}},
    "Uzbekistan":               {"status": "pending", "squad": {}},

    "Colombia": {
        "status": "preliminary",
        "squad": {
            "goalkeepers": [
                {"name": "Camilo Vargas",           "club": "Atlas"},
                {"name": "David Ospina",            "club": "Atletico Nacional"},
                {"name": "Alvaro Montero",          "club": "Velez Sarsfield"},
            ],
            "defenders": [
                {"name": "Davinson Sanchez",        "club": "Galatasaray"},
                {"name": "Yerry Mina",              "club": "Cagliari"},
                {"name": "Jhon Lucumi",             "club": "Bologna"},
                {"name": "Daniel Munoz",            "club": "Crystal Palace"},
                {"name": "Johan Mojica",            "club": "RCD Mallorca"},
                {"name": "Carlos Cuesta",           "club": "Vasco da Gama"},
                {"name": "Juan Cabal",              "club": "Juventus"},
                {"name": "Yerson Mosquera",         "club": "Wolverhampton Wanderers"},
            ],
            "midfielders": [
                {"name": "James Rodriguez",         "club": "Minnesota United"},
                {"name": "Richard Rios",            "club": "Benfica"},
                {"name": "Jefferson Lerma",         "club": "Crystal Palace"},
                {"name": "Jhon Arias",              "club": "Palmeiras"},
                {"name": "Juan Fernando Quintero",  "club": "Racing Club"},
                {"name": "Yaser Asprilla",          "club": "Girona"},
                {"name": "Juan Cuadrado",           "club": "Atalanta"},
                {"name": "Wilmar Barrios",          "club": "Zenit Saint Petersburg"},
            ],
            "forwards": [
                {"name": "Luis Diaz",               "club": "Bayern Munich"},
                {"name": "Rafael Santos Borre",     "club": "Internacional"},
                {"name": "Jhon Cordoba",            "club": "Krasnodar"},
                {"name": "Juan Camilo Hernandez",   "club": "Columbus Crew"},
            ],
        },
    },

    # =========================================================================
    # GROUP L
    # =========================================================================

    "England":                  {"status": "pending", "squad": {}},
    "Croatia":                  {"status": "pending", "squad": {}},
    "Ghana":                    {"status": "pending", "squad": {}},
    "Panama":                   {"status": "pending", "squad": {}},
}
