# -*- coding: utf-8 -*-
"""
================================================================================
 world/regions.py
================================================================================
 Region groupings (geographic, cultural, political).

 Data only.
================================================================================
"""

# =============================================================================
# REGION -> COUNTRIES
# =============================================================================
REGION_COUNTRIES = {
    # --- Geographic subregions ---
    "North Africa": [
        "Algeria", "Egypt", "Libya", "Morocco", "Sudan", "Tunisia",
        "Western Sahara",
    ],
    "West Africa": [
        "Benin", "Burkina Faso", "Cape Verde", "Gambia", "Ghana",
        "Guinea", "Guinea-Bissau", "Ivory Coast", "Liberia", "Mali",
        "Mauritania", "Niger", "Nigeria", "Senegal", "Sierra Leone",
        "Togo",
    ],
    "Central Africa": [
        "Cameroon", "Central African Republic", "Chad",
        "Democratic Republic of the Congo", "Equatorial Guinea",
        "Gabon", "Republic of the Congo", "Sao Tome and Principe",
    ],
    "East Africa": [
        "Burundi", "Comoros", "Djibouti", "Eritrea", "Ethiopia",
        "Kenya", "Madagascar", "Malawi", "Mauritius", "Mozambique",
        "Rwanda", "Seychelles", "Somalia", "South Sudan", "Tanzania",
        "Uganda", "Zambia", "Zimbabwe", "Réunion",
    ],
    "Southern Africa": [
        "Botswana", "Eswatini", "Lesotho", "Namibia", "South Africa",
    ],
    "Middle East": [
        "Bahrain", "Cyprus", "Egypt", "Iran", "Iraq", "Israel",
        "Jordan", "Kuwait", "Lebanon", "Oman", "Palestine", "Qatar",
        "Saudi Arabia", "Syria", "Turkey", "United Arab Emirates",
        "Yemen",
    ],
    "Central Asia": [
        "Kazakhstan", "Kyrgyzstan", "Tajikistan", "Turkmenistan",
        "Uzbekistan",
    ],
    "South Asia": [
        "Afghanistan", "Bangladesh", "Bhutan", "India", "Maldives",
        "Nepal", "Pakistan", "Sri Lanka",
    ],
    "Southeast Asia": [
        "Brunei", "Cambodia", "Indonesia", "Laos", "Malaysia",
        "Myanmar", "Philippines", "Singapore", "Thailand",
        "Timor-Leste", "Vietnam",
    ],
    "East Asia": [
        "China", "Japan", "Mongolia", "North Korea", "South Korea",
        "Taiwan", "Hong Kong", "Macau",
    ],
    "Caribbean": [
        "Antigua and Barbuda", "Bahamas", "Barbados", "Cuba",
        "Dominica", "Dominican Republic", "Grenada", "Haiti",
        "Jamaica", "Saint Kitts and Nevis", "Saint Lucia",
        "Saint Vincent and the Grenadines", "Trinidad and Tobago",
        "Puerto Rico", "Aruba", "Curaçao", "Bermuda",
        "Cayman Islands", "Turks and Caicos Islands",
        "British Virgin Islands", "US Virgin Islands",
        "Anguilla", "Montserrat", "Sint Maarten",
    ],
    "Central America": [
        "Belize", "Costa Rica", "El Salvador", "Guatemala",
        "Honduras", "Nicaragua", "Panama",
    ],
    "Melanesia": ["Fiji", "Papua New Guinea", "Solomon Islands", "Vanuatu"],
    "Micronesia": [
        "Guam", "Kiribati", "Marshall Islands", "Micronesia",
        "Nauru", "Northern Mariana Islands", "Palau",
    ],
    "Polynesia": [
        "American Samoa", "Cook Islands", "French Polynesia",
        "Niue", "Samoa", "Tonga", "Tuvalu", "Wallis and Futuna",
    ],
    "Scandinavia": ["Denmark", "Norway", "Sweden"],
    "Nordic countries": [
        "Denmark", "Finland", "Iceland", "Norway", "Sweden",
        "Faroe Islands", "Greenland", "Åland Islands",
    ],
    "Baltic states": ["Estonia", "Latvia", "Lithuania"],
    "Balkans": [
        "Albania", "Bosnia and Herzegovina", "Bulgaria", "Croatia",
        "Greece", "Kosovo", "Montenegro", "North Macedonia",
        "Romania", "Serbia", "Slovenia",
    ],
    "Benelux": ["Belgium", "Netherlands", "Luxembourg"],
    "Iberian Peninsula": ["Spain", "Portugal", "Andorra", "Gibraltar"],
    "British Isles": ["United Kingdom", "Ireland"],
    "Caucasus": ["Armenia", "Azerbaijan", "Georgia"],
    "Levant": ["Cyprus", "Israel", "Jordan", "Lebanon",
               "Palestine", "Syria", "Turkey"],

    # --- Political / economic ---
    "G7": ["Canada", "France", "Germany", "Italy", "Japan",
           "United Kingdom", "United States"],
    "G20": [
        "Argentina", "Australia", "Brazil", "Canada", "China",
        "France", "Germany", "India", "Indonesia", "Italy",
        "Japan", "Mexico", "Russia", "Saudi Arabia", "South Africa",
        "South Korea", "Turkey", "United Kingdom", "United States",
        "European Union",
    ],
    "BRICS": [
        "Brazil", "Russia", "India", "China", "South Africa",
        "Egypt", "Ethiopia", "Iran", "United Arab Emirates",
    ],
    "EU": [
        "Austria", "Belgium", "Bulgaria", "Croatia", "Cyprus",
        "Czech Republic", "Denmark", "Estonia", "Finland", "France",
        "Germany", "Greece", "Hungary", "Ireland", "Italy", "Latvia",
        "Lithuania", "Luxembourg", "Malta", "Netherlands", "Poland",
        "Portugal", "Romania", "Slovakia", "Slovenia", "Spain",
        "Sweden",
    ],
    "NATO": [
        "Albania", "Belgium", "Bulgaria", "Canada", "Croatia",
        "Czech Republic", "Denmark", "Estonia", "Finland", "France",
        "Germany", "Greece", "Hungary", "Iceland", "Italy", "Latvia",
        "Lithuania", "Luxembourg", "Montenegro", "Netherlands",
        "North Macedonia", "Norway", "Poland", "Portugal", "Romania",
        "Slovakia", "Slovenia", "Spain", "Sweden", "Turkey",
        "United Kingdom", "United States",
    ],
    "OPEC": [
        "Algeria", "Angola", "Equatorial Guinea", "Gabon", "Iran",
        "Iraq", "Kuwait", "Libya", "Nigeria", "Republic of the Congo",
        "Saudi Arabia", "United Arab Emirates", "Venezuela",
    ],
    "ASEAN": [
        "Brunei", "Cambodia", "Indonesia", "Laos", "Malaysia",
        "Myanmar", "Philippines", "Singapore", "Thailand", "Vietnam",
    ],
    "Arab League": [
        "Algeria", "Bahrain", "Comoros", "Djibouti", "Egypt", "Iraq",
        "Jordan", "Kuwait", "Lebanon", "Libya", "Mauritania",
        "Morocco", "Oman", "Palestine", "Qatar", "Saudi Arabia",
        "Somalia", "Sudan", "Syria", "Tunisia",
        "United Arab Emirates", "Yemen",
    ],
    "Commonwealth": [
        "Antigua and Barbuda", "Australia", "Bahamas", "Bangladesh",
        "Barbados", "Belize", "Botswana", "Brunei", "Cameroon",
        "Canada", "Cyprus", "Dominica", "Eswatini", "Fiji", "Gabon",
        "Gambia", "Ghana", "Grenada", "Guyana", "India", "Jamaica",
        "Kenya", "Kiribati", "Lesotho", "Malawi", "Malaysia",
        "Maldives", "Malta", "Mauritius", "Mozambique", "Namibia",
        "Nauru", "New Zealand", "Nigeria", "Pakistan", "Papua New Guinea",
        "Rwanda", "Saint Kitts and Nevis", "Saint Lucia",
        "Saint Vincent and the Grenadines", "Samoa", "Seychelles",
        "Sierra Leone", "Singapore", "Solomon Islands",
        "South Africa", "Sri Lanka", "Tanzania", "Togo", "Tonga",
        "Trinidad and Tobago", "Tuvalu", "Uganda",
        "United Kingdom", "Vanuatu", "Zambia",
    ],
    "Non-Aligned Movement": [
        "Afghanistan", "Algeria", "Angola", "Bahamas", "Bahrain",
        "Bangladesh", "Barbados", "Belarus", "Belize", "Benin",
        "Bhutan", "Bolivia", "Botswana", "Brunei", "Burkina Faso",
        "Burundi", "Cambodia", "Cameroon", "Cape Verde",
        "Central African Republic", "Chad", "Colombia", "Comoros",
        "Republic of the Congo", "Cuba", "Djibouti", "Dominica",
        "Dominican Republic", "Ecuador", "Egypt", "Equatorial Guinea",
        "Eritrea", "Eswatini", "Ethiopia", "Fiji", "Gabon", "Gambia",
        "Ghana", "Grenada", "Guatemala", "Guinea", "Guinea-Bissau",
        "Guyana", "Haiti", "Honduras", "India", "Indonesia", "Iran",
        "Iraq", "Ivory Coast", "Jamaica", "Jordan", "Kenya", "Kuwait",
        "Laos", "Lebanon", "Lesotho", "Liberia", "Libya", "Madagascar",
        "Malawi", "Malaysia", "Maldives", "Mali", "Mauritania",
        "Mauritius", "Mongolia", "Morocco", "Mozambique", "Myanmar",
        "Namibia", "Nepal", "Nicaragua", "Niger", "Nigeria", "North Korea",
        "Oman", "Pakistan", "Palestine", "Panama", "Papua New Guinea",
        "Peru", "Philippines", "Qatar", "Rwanda",
        "Saint Kitts and Nevis", "Saint Lucia",
        "Saint Vincent and the Grenadines", "Sao Tome and Principe",
        "Saudi Arabia", "Senegal", "Seychelles", "Sierra Leone",
        "Singapore", "Somalia", "South Africa", "Sri Lanka", "Sudan",
        "Suriname", "Syria", "Tanzania", "Thailand", "Timor-Leste",
        "Togo", "Trinidad and Tobago", "Tunisia", "Turkmenistan",
        "Uganda", "United Arab Emirates", "Uzbekistan", "Vanuatu",
        "Venezuela", "Vietnam", "Yemen", "Zambia", "Zimbabwe",
    ],

    # --- Income groupings (World Bank, approximate) ---
    "High-income countries": [
        "Australia", "Austria", "Bahamas", "Bahrain", "Barbados",
        "Belgium", "Brunei", "Canada", "Chile", "Croatia", "Cyprus",
        "Czech Republic", "Denmark", "Estonia", "Finland", "France",
        "Germany", "Greece", "Hong Kong", "Hungary", "Iceland",
        "Ireland", "Israel", "Italy", "Japan", "Kuwait", "Latvia",
        "Liechtenstein", "Lithuania", "Luxembourg", "Macau", "Malta",
        "Monaco", "Netherlands", "New Zealand", "Norway", "Oman",
        "Panama", "Poland", "Portugal", "Puerto Rico", "Qatar",
        "Romania", "San Marino", "Saudi Arabia", "Seychelles",
        "Singapore", "Slovakia", "Slovenia", "South Korea", "Spain",
        "Sweden", "Switzerland", "Taiwan", "Trinidad and Tobago",
        "United Arab Emirates", "United Kingdom", "United States",
        "Uruguay",
    ],
    "Low-income countries": [
        "Afghanistan", "Burkina Faso", "Burundi",
        "Central African Republic", "Chad",
        "Democratic Republic of the Congo", "Eritrea", "Ethiopia",
        "Gambia", "Guinea", "Guinea-Bissau", "Liberia", "Madagascar",
        "Malawi", "Mali", "Mozambique", "Niger", "Rwanda",
        "Sierra Leone", "Somalia", "South Sudan", "Sudan", "Syria",
        "Togo", "Uganda", "Yemen",
    ],
}

COUNTRY_REGION = {}
for _region, _countries in REGION_COUNTRIES.items():
    for _country in _countries:
        COUNTRY_REGION.setdefault(_country, []).append(_region)
del _region, _countries, _country


# =============================================================================
# REGION TYPE
# =============================================================================
REGION_TYPE = {
    "North Africa": "geographic",
    "West Africa": "geographic",
    "Central Africa": "geographic",
    "East Africa": "geographic",
    "Southern Africa": "geographic",
    "Middle East": "geographic",
    "Central Asia": "geographic",
    "South Asia": "geographic",
    "Southeast Asia": "geographic",
    "East Asia": "geographic",
    "Caribbean": "geographic",
    "Central America": "geographic",
    "Melanesia": "geographic",
    "Micronesia": "geographic",
    "Polynesia": "geographic",
    "Scandinavia": "cultural",
    "Nordic countries": "cultural",
    "Baltic states": "cultural",
    "Balkans": "cultural",
    "Benelux": "political",
    "Iberian Peninsula": "geographic",
    "British Isles": "geographic",
    "Caucasus": "geographic",
    "Levant": "geographic",
    "G7": "economic",
    "G20": "economic",
    "BRICS": "economic",
    "EU": "political",
    "NATO": "military",
    "OPEC": "economic",
    "ASEAN": "political",
    "Arab League": "political",
    "Commonwealth": "political",
    "Non-Aligned Movement": "political",
    "High-income countries": "economic",
    "Low-income countries": "economic",
}


__all__ = [name for name in dir() if name.isupper() and not name.startswith("_")]