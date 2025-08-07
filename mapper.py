continent_mapper = {'Albania': 'Europe',
            'Andorra': 'Europe',
            'Austria': 'Europe',
            'Belarus': 'Europe',
            'Belgium': 'Europe',
            'Bosnia and Herzegovina': 'Europe',
            'Bulgaria': 'Europe',
            'Croatia': 'Europe',
            'Cyprus': 'Europe',
            'Czech Republic': 'Europe',
            'Denmark': 'Europe',
            'Estonia': 'Europe',
            'Finland': 'Europe',
            'France': 'Europe',
            'Germany': 'Europe',
            'Greece': 'Europe',
            'Hungary': 'Europe',
            'Iceland': 'Europe',
            'Ireland': 'Europe',
            'Italy': 'Europe',
            'Latvia': 'Europe',
            'Liechtenstein': 'Europe',
            'Lithuania': 'Europe',
            'Luxembourg': 'Europe',
            'Malta': 'Europe',
            'Monaco': 'Europe',
            'Montenegro': 'Europe',
            'Netherlands': 'Europe',
            'North Macedonia': 'Europe',
            'Norway': 'Europe',
            'Poland': 'Europe',
            'Portugal': 'Europe',
            'Republic of Moldova': 'Europe',
            'Romania': 'Europe',
            'Russia': 'Europe',
            'San Marino': 'Europe',
            'Serbia': 'Europe',
            'Slovakia': 'Europe',
            'Slovenia': 'Europe',
            'Spain': 'Europe',
            'Sweden': 'Europe',
            'Switzerland': 'Europe',
            'Ukraine': 'Europe',
            'United Kingdom of Great Britain and Northern Ireland': 'Europe',
            'Afghanistan': 'Asia',
            'Armenia': 'Asia',
            'Azerbaijan': 'Asia',
            'Bahrain': 'Asia',
            'Bangladesh': 'Asia',
            'Bhutan': 'Asia',
            'Brunei Darussalam': 'Asia',
            'Cambodia': 'Asia',
            'China': 'Asia',
            'Georgia': 'Asia',
            'India': 'Asia',
            'Indonesia': 'Asia',
            'Iran': 'Asia',
            'Iraq': 'Asia',
            'Israel': 'Asia',
            'Japan': 'Asia',
            'Jordan': 'Asia',
            'Kazakhstan': 'Asia',
            'Kuwait': 'Asia',
            'Kyrgyzstan': 'Asia',
            "Lao People's Democratic Republic": 'Asia',
            'Lebanon': 'Asia',
            'Malaysia': 'Asia',
            'Maldives': 'Asia',
            'Mongolia': 'Asia',
            'Myanmar': 'Asia',
            'Nepal': 'Asia',
            'North Korea': 'Asia',
            'Oman': 'Asia',
            'Pakistan': 'Asia',
            'Palestine': 'Asia',
            'Philippines': 'Asia',
            'Qatar': 'Asia',
            'Saudi Arabia': 'Asia',
            'Singapore': 'Asia',
            'South Korea': 'Asia',
            'Sri Lanka': 'Asia',
            'Syria': 'Asia',
            'Tajikistan': 'Asia',
            'Thailand': 'Asia',
            'Timor-Leste': 'Asia',
            'Turkey': 'Asia',
            'Turkmenistan': 'Asia',
            'United Arab Emirates': 'Asia',
            'Uzbekistan': 'Asia',
            'Vietnam': 'Asia',
            'Yemen': 'Asia',
            'Antigua and Barbuda': 'Americas',
            'Argentina': 'Americas',
            'Bahamas': 'Americas',
            'Barbados': 'Americas',
            'Belize': 'Americas',
            'Bolivia': 'Americas',
            'Brazil': 'Americas',
            'Canada': 'Americas',
            'Chile': 'Americas',
            'Colombia': 'Americas',
            'Costa Rica': 'Americas',
            'Cuba': 'Americas',
            'Dominica': 'Americas',
            'Dominican Republic': 'Americas',
            'Ecuador': 'Americas',
            'El Salvador': 'Americas',
            'Grenada': 'Americas',
            'Guatemala': 'Americas',
            'Guyana': 'Americas',
            'Haiti': 'Americas',
            'Honduras': 'Americas',
            'Jamaica': 'Americas',
            'Mexico': 'Americas',
            'Nicaragua': 'Americas',
            'Panama': 'Americas',
            'Paraguay': 'Americas',
            'Peru': 'Americas',
            'Saint Kitts and Nevis': 'Americas',
            'Saint Lucia': 'Americas',
            'Saint Vincent and the Grenadines': 'Americas',
            'Suriname': 'Americas',
            'Trinidad and Tobago': 'Americas',
            'United States of America': 'Americas',
            'Uruguay': 'Americas',
            'Venezuela': 'Americas',
            'Australia': 'Oceania',
            'Fiji': 'Oceania',
            'Kiribati': 'Oceania',
            'Marshall Islands': 'Oceania',
            'Micronesia': 'Oceania',
            'Nauru': 'Oceania',
            'New Zealand': 'Oceania',
            'Palau': 'Oceania',
            'Papua New Guinea': 'Oceania',
            'Samoa': 'Oceania',
            'Solomon Islands': 'Oceania',
            'Tonga': 'Oceania',
            'Tuvalu': 'Oceania',
            'Vanuatu': 'Oceania',
            'Algeria': 'Africa',
            'Angola': 'Africa',
            'Benin': 'Africa',
            'Botswana': 'Africa',
            'Burkina Faso': 'Africa',
            'Burundi': 'Africa',
            'Cabo Verde': 'Africa',
            'Cameroon': 'Africa',
            'Central African Republic': 'Africa',
            'Chad': 'Africa',
            'Comoros': 'Africa',
            'Congo, Republic of the...': 'Africa',
            'Democratic Republic of the Congo': 'Africa',
            "Côte d'Ivoire": 'Africa',
            'Djibouti': 'Africa',
            'Egypt': 'Africa',
            'Equatorial Guinea': 'Africa',
            'Eritrea': 'Africa',
            'Eswatini': 'Africa',
            'Ethiopia': 'Africa',
            'Gabon': 'Africa',
            'Gambia': 'Africa',
            'Ghana': 'Africa',
            'Guinea': 'Africa',
            'Guinea-Bissau': 'Africa',
            'Kenya': 'Africa',
            'Lesotho': 'Africa',
            'Liberia': 'Africa',
            'Libya': 'Africa',
            'Madagascar': 'Africa',
            'Malawi': 'Africa',
            'Mali': 'Africa',
            'Mauritania': 'Africa',
            'Mauritius': 'Africa',
            'Morocco': 'Africa',
            'Mozambique': 'Africa',
            'Namibia': 'Africa',
            'Niger': 'Africa',
            'Nigeria': 'Africa',
            'Rwanda': 'Africa',
            'Sao Tome and Principe': 'Africa',
            'Senegal': 'Africa',
            'Seychelles': 'Africa',
            'Sierra Leone': 'Africa',
            'Somalia': 'Africa',
            'South Africa': 'Africa',
            'South Sudan': 'Africa',
            'Sudan': 'Africa',
            'Togo': 'Africa',
            'Tunisia': 'Africa',
            'Uganda': 'Africa',
            'United Republic of Tanzania': 'Africa',
            'Zambia': 'Africa',
            'Zimbabwe': 'Africa'
        }

short_to_fullname = {
    "trump": "Donald Trump",
    "biden": "Joe Biden",
    "lee": "Lee Jae-myung",
    "yoon": "Yoon Suk Yeol",
    "paetongtarn": "Paetongtarn Shinawatra",
    "prayut": "Prayut Chan-o-cha",
    "jacinda": "Jacinda Ardern",
    "luxon": "Christopher Luxon",
    "albanese": "Anthony Albanese",
    "morrison": "Scott Morrison",
    "starmer": "Keir Starmer",
    "sunak": "Rishi Sunak",
    "friedrich": "Friedrich Merz",
    "olaf": "Olaf Scholz",
    "bolsonaro": "Jair Bolsonaro",
    "lula": "Luiz Inácio Lula da Silva",
    "singh": "Manmohan Singh",
    "modi": "Narendra Modi",
    "harper": "Stephen Harper",
    "trudeau": "Justin Trudeau",
    "kenyatta": "Uhuru Kenyatta",
    "ruto": "William Ruto",
    "masisi": "Mokgweetsi Masisi",
    "boko": "Duma Boko"
}

fullname_to_short = {
'Donald Trump': 'Trump',
 'Joe Biden': 'Biden',
 'Lee Jae-myung': 'Lee',
 'Yoon Suk Yeol': 'Yoon',
 'Paetongtarn Shinawatra': 'Paetongtarn',
 'Prayut Chan-o-cha': 'Prayut',
 'Jacinda Ardern': 'Jacinda',
 'Christopher Luxon': 'Luxon',
 'Anthony Albanese': 'Albanese',
 'Scott Morrison': 'Morrison',
 'Keir Starmer': 'Starmer',
 'Rishi Sunak': 'Sunak',
 'Friedrich Merz': 'Friedrich',
 'Olaf Scholz': 'Olaf',
 'Jair Bolsonaro': 'Bolsonaro',
 'Luiz Inácio Lula da Silva': 'Lula',
 'Manmohan Singh': 'Singh',
 'Narendra Modi': 'Modi',
 'Stephen Harper': 'Harper',
 'Justin Trudeau': 'Trudeau',
 'Uhuru Kenyatta': 'Kenyatta',
 'William Ruto': 'Ruto',
 'Mokgweetsi Masisi': 'Masisi',
 'Duma Boko': 'Boko'
}

politicians_db = {
        'trump': {
            'name': 'Donald Trump',
            'country': 'United States',
            'continent': 'Americas',
            'ideology': 'conservative',
            'popularity_score': 9,  # Global recognition
            'approval_rating': 5,   # Current approval based on recent polls
            'incumbent_status': 'current',
            'age_category': 'senior',
            'party_color': 'red',
            'party_name': 'Republican Party'
        },
        
        'biden': {
            'name': 'Joe Biden',
            'country': 'United States',
            'continent': 'Americas',
            'ideology': 'liberal',
            'popularity_score': 8,  # Global recognition
            'approval_rating': 4,   # Lower approval as former president
            'incumbent_status': 'former',
            'age_category': 'senior',
            'party_color': 'blue',
            'party_name': 'Democratic Party'
        },
        
        'lee': {
            'name': 'Lee Jae-myung',
            'country': 'South Korea',
            'continent': 'Asia',
            'ideology': 'liberal',
            'popularity_score': 5,  # Regional recognition
            'approval_rating': 5,   # Opposition leader approval
            'incumbent_status': 'current',
            'age_category': 'middle_aged',
            'party_color': 'blue',
            'party_name': 'Democratic Party of Korea'
        },
        
        'yoon': {
            'name': 'Yoon Suk Yeol',
            'country': 'South Korea',
            'continent': 'Asia',
            'ideology': 'conservative',
            'popularity_score': 6,  # Regional recognition
            'approval_rating': 4,   # Lower approval ratings
            'incumbent_status': 'former',
            'age_category': 'middle_aged',
            'party_color': 'red',
            'party_name': 'People Power Party'
        },
        
        'paetongtarn': {
            'name': 'Paetongtarn Shinawatra',
            'country': 'Thailand',
            'continent': 'Asia',
            'ideology': 'liberal',
            'popularity_score': 4,  # Regional recognition
            'approval_rating': 6,   # Moderate approval
            'incumbent_status': 'current',
            'age_category': 'young',
            'party_color': 'red',
            'party_name': 'Pheu Thai Party'
        },
        
        'prayut': {
            'name': 'Prayut Chan-o-cha',
            'country': 'Thailand',
            'continent': 'Asia',
            'ideology': 'conservative',
            'popularity_score': 4,  # Regional recognition
            'approval_rating': 3,   # Lower approval as former leader
            'incumbent_status': 'former',
            'age_category': 'senior',
            'party_color': 'blue',
            'party_name': 'United Thai Nation Party'
        },
        
        'jacinda': {
            'name': 'Jacinda Ardern',
            'country': 'New Zealand',
            'continent': 'Oceania',
            'ideology': 'liberal',
            'popularity_score': 7,  # High global recognition
            'approval_rating': 7,   # Still popular internationally
            'incumbent_status': 'former',
            'age_category': 'middle_aged',
            'party_color': 'red',
            'party_name': 'New Zealand Labour Party'
        },
        
        'luxon': {
            'name': 'Christopher Luxon',
            'country': 'New Zealand',
            'continent': 'Oceania',
            'ideology': 'conservative',
            'popularity_score': 3,  # Limited global recognition
            'approval_rating': 5,   # Moderate approval
            'incumbent_status': 'current',
            'age_category': 'middle_aged',
            'party_color': 'blue',
            'party_name': 'New Zealand National Party'
        },
        
        'albanese': {
            'name': 'Anthony Albanese',
            'country': 'Australia',
            'continent': 'Oceania',
            'ideology': 'liberal',
            'popularity_score': 5,  # Regional recognition
            'approval_rating': 5,   # Moderate approval
            'incumbent_status': 'current',
            'age_category': 'middle_aged',
            'party_color': 'red',
            'party_name': 'Australian Labor Party'
        },
        
        'morrison': {
            'name': 'Scott Morrison',
            'country': 'Australia',
            'continent': 'Oceania',
            'ideology': 'conservative',
            'popularity_score': 5,  # Regional recognition
            'approval_rating': 3,   # Lower approval as former PM
            'incumbent_status': 'former',
            'age_category': 'middle_aged',
            'party_color': 'blue',
            'party_name': 'Liberal Party of Australia'
        },
        
        'starmer': {
            'name': 'Keir Starmer',
            'country': 'United Kingdom',
            'continent': 'Europe',
            'ideology': 'liberal',
            'popularity_score': 6,  # International recognition
            'approval_rating': 5,   # Moderate approval
            'incumbent_status': 'current',
            'age_category': 'middle_aged',
            'party_color': 'red',
            'party_name': 'Labour Party'
        },
        
        'sunak': {
            'name': 'Rishi Sunak',
            'country': 'United Kingdom',
            'continent': 'Europe',
            'ideology': 'conservative',
            'popularity_score': 6,  # International recognition
            'approval_rating': 3,   # Lower approval as former PM
            'incumbent_status': 'former',
            'age_category': 'middle_aged',
            'party_color': 'blue',
            'party_name': 'Conservative Party'
        },
        
        'friedrich': {
            'name': 'Friedrich Merz',
            'country': 'Germany',
            'continent': 'Europe',
            'ideology': 'conservative',
            'popularity_score': 4,  # Regional recognition
            'approval_rating': 5,   # Moderate as opposition leader
            'incumbent_status': 'opposition',
            'age_category': 'senior',
            'party_color': 'black',
            'party_name': 'Christian Democratic Union'
        },
        
        'olaf': {
            'name': 'Olaf Scholz',
            'country': 'Germany',
            'continent': 'Europe',
            'ideology': 'liberal',
            'popularity_score': 5,  # International recognition
            'approval_rating': 4,   # Lower approval ratings
            'incumbent_status': 'current',
            'age_category': 'middle_aged',
            'party_color': 'red',
            'party_name': 'Social Democratic Party'
        },
        
        'bolsonaro': {
            'name': 'Jair Bolsonaro',
            'country': 'Brazil',
            'continent': 'Americas',
            'ideology': 'conservative',
            'popularity_score': 7,  # High international recognition
            'approval_rating': 4,   # Lower approval as former president
            'incumbent_status': 'former',
            'age_category': 'senior',
            'party_color': 'blue',
            'party_name': 'Liberal Party'
        },
        
        'lula': {
            'name': 'Luiz Inácio Lula da Silva',
            'country': 'Brazil',
            'continent': 'Americas',
            'ideology': 'liberal',
            'popularity_score': 7,  # High international recognition
            'approval_rating': 6,   # Moderate approval
            'incumbent_status': 'current',
            'age_category': 'senior',
            'party_color': 'red',
            'party_name': 'Workers Party'
        },
        
        'singh': {
            'name': 'Manmohan Singh',
            'country': 'India',
            'continent': 'Asia',
            'ideology': 'liberal',
            'popularity_score': 6,  # International recognition as former PM
            'approval_rating': 5,   # Respected elder statesman
            'incumbent_status': 'former',
            'age_category': 'senior',
            'party_color': 'blue',
            'party_name': 'Indian National Congress'
        },
        
        'modi': {
            'name': 'Narendra Modi',
            'country': 'India',
            'continent': 'Asia',
            'ideology': 'conservative',
            'popularity_score': 8,  # High global recognition
            'approval_rating': 8,   # Highest approval among world leaders
            'incumbent_status': 'current',
            'age_category': 'senior',
            'party_color': 'orange',
            'party_name': 'Bharatiya Janata Party'
        },
        
        'harper': {
            'name': 'Stephen Harper',
            'country': 'Canada',
            'continent': 'Americas',
            'ideology': 'conservative',
            'popularity_score': 4,  # Regional recognition
            'approval_rating': 4,   # Moderate as former PM
            'incumbent_status': 'former',
            'age_category': 'middle_aged',
            'party_color': 'blue',
            'party_name': 'Conservative Party of Canada'
        },
        
        'trudeau': {
            'name': 'Justin Trudeau',
            'country': 'Canada',
            'continent': 'Americas',
            'ideology': 'liberal',
            'popularity_score': 7,  # High international recognition
            'approval_rating': 3,   # Low approval before losing election
            'incumbent_status': 'current',
            'age_category': 'middle_aged',
            'party_color': 'red',
            'party_name': 'Liberal Party of Canada'
        },
        
        'kenyatta': {
            'name': 'Uhuru Kenyatta',
            'country': 'Kenya',
            'continent': 'Africa',
            'ideology': 'centrist',
            'popularity_score': 4,  # Regional recognition
            'approval_rating': 5,   # Moderate as former president
            'incumbent_status': 'former',
            'age_category': 'middle_aged',
            'party_color': 'blue',
            'party_name': 'Jubilee Party'
        },
        
        'ruto': {
            'name': 'William Ruto',
            'country': 'Kenya',
            'continent': 'Africa',
            'ideology': 'conservative',
            'popularity_score': 4,  # Regional recognition
            'approval_rating': 4,   # Moderate approval
            'incumbent_status': 'current',
            'age_category': 'middle_aged',
            'party_color': 'yellow',
            'party_name': 'United Democratic Alliance'
        },
        
        'masisi': {
            'name': 'Mokgweetsi Masisi',
            'country': 'Botswana',
            'continent': 'Africa',
            'ideology': 'centrist',
            'popularity_score': 2,  # Limited international recognition
            'approval_rating': 3,   # Lower approval, lost recent election
            'incumbent_status': 'former',
            'age_category': 'middle_aged',
            'party_color': 'blue',
            'party_name': 'Botswana Democratic Party'
        },
        
        'boko': {
            'name': 'Duma Boko',
            'country': 'Botswana',
            'continent': 'Africa',
            'ideology': 'liberal',
            'popularity_score': 2,  # Limited international recognition
            'approval_rating': 6,   # Higher approval as new president
            'incumbent_status': 'current',
            'age_category': 'middle_aged',
            'party_color': 'orange',
            'party_name': 'Umbrella for Democratic Change'
        }
    }