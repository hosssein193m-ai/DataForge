# -*- coding: utf-8 -*-
"""
================================================================================
 world/continents.py
================================================================================
 Country → continent mapping, plus continent → countries reverse index.

 Data only.
================================================================================
"""

# =============================================================================
# COUNTRY -> CONTINENT
# =============================================================================
COUNTRY_CONTINENT = {
    # --- Asia ---
    "Afghanistan": "Asia", "Armenia": "Asia", "Azerbaijan": "Asia",
    "Bahrain": "Asia", "Bangladesh": "Asia", "Bhutan": "Asia",
    "Brunei": "Asia", "Cambodia": "Asia", "China": "Asia",
    "Cyprus": "Asia", "Georgia": "Asia", "India": "Asia",
    "Indonesia": "Asia", "Iran": "Asia", "Iraq": "Asia",
    "Israel": "Asia", "Japan": "Asia", "Jordan": "Asia",
    "Kazakhstan": "Asia", "Kuwait": "Asia", "Kyrgyzstan": "Asia",
    "Laos": "Asia", "Lebanon": "Asia", "Malaysia": "Asia",
    "Maldives": "Asia", "Mongolia": "Asia", "Myanmar": "Asia",
    "Nepal": "Asia", "North Korea": "Asia", "Oman": "Asia",
    "Pakistan": "Asia", "Palestine": "Asia", "Philippines": "Asia",
    "Qatar": "Asia", "Russia": "Asia", "Saudi Arabia": "Asia",
    "Singapore": "Asia", "South Korea": "Asia", "Sri Lanka": "Asia",
    "Syria": "Asia", "Taiwan": "Asia", "Tajikistan": "Asia",
    "Thailand": "Asia", "Timor-Leste": "Asia", "Turkey": "Asia",
    "Turkmenistan": "Asia", "United Arab Emirates": "Asia",
    "Uzbekistan": "Asia", "Vietnam": "Asia", "Yemen": "Asia",
    "Hong Kong": "Asia", "Macau": "Asia",

    # --- Europe ---
    "Albania": "Europe", "Andorra": "Europe", "Austria": "Europe",
    "Belarus": "Europe", "Belgium": "Europe",
    "Bosnia and Herzegovina": "Europe", "Bulgaria": "Europe",
    "Croatia": "Europe", "Czech Republic": "Europe",
    "Denmark": "Europe", "Estonia": "Europe", "Finland": "Europe",
    "France": "Europe", "Germany": "Europe", "Greece": "Europe",
    "Hungary": "Europe", "Iceland": "Europe", "Ireland": "Europe",
    "Italy": "Europe", "Kosovo": "Europe", "Latvia": "Europe",
    "Liechtenstein": "Europe", "Lithuania": "Europe",
    "Luxembourg": "Europe", "Malta": "Europe", "Moldova": "Europe",
    "Monaco": "Europe", "Montenegro": "Europe",
    "Netherlands": "Europe", "North Macedonia": "Europe",
    "Norway": "Europe", "Poland": "Europe", "Portugal": "Europe",
    "Romania": "Europe", "San Marino": "Europe", "Serbia": "Europe",
    "Slovakia": "Europe", "Slovenia": "Europe", "Spain": "Europe",
    "Sweden": "Europe", "Switzerland": "Europe", "Ukraine": "Europe",
    "United Kingdom": "Europe", "Vatican City": "Europe",

    # --- North America ---
    "Antigua and Barbuda": "North America",
    "Bahamas": "North America", "Barbados": "North America",
    "Belize": "North America", "Canada": "North America",
    "Costa Rica": "North America", "Cuba": "North America",
    "Dominica": "North America",
    "Dominican Republic": "North America",
    "El Salvador": "North America", "Grenada": "North America",
    "Guatemala": "North America", "Haiti": "North America",
    "Honduras": "North America", "Jamaica": "North America",
    "Mexico": "North America", "Nicaragua": "North America",
    "Panama": "North America",
    "Saint Kitts and Nevis": "North America",
    "Saint Lucia": "North America",
    "Saint Vincent and the Grenadines": "North America",
    "Trinidad and Tobago": "North America",
    "United States": "North America",

    # --- South America ---
    "Argentina": "South America", "Bolivia": "South America",
    "Brazil": "South America", "Chile": "South America",
    "Colombia": "South America", "Ecuador": "South America",
    "Guyana": "South America", "Paraguay": "South America",
    "Peru": "South America", "Suriname": "South America",
    "Uruguay": "South America", "Venezuela": "South America",

    # --- Africa ---
    "Algeria": "Africa", "Angola": "Africa", "Benin": "Africa",
    "Botswana": "Africa", "Burkina Faso": "Africa",
    "Burundi": "Africa", "Cameroon": "Africa",
    "Cape Verde": "Africa", "Central African Republic": "Africa",
    "Chad": "Africa", "Comoros": "Africa",
    "Democratic Republic of the Congo": "Africa",
    "Republic of the Congo": "Africa", "Djibouti": "Africa",
    "Egypt": "Africa", "Equatorial Guinea": "Africa",
    "Eritrea": "Africa", "Eswatini": "Africa",
    "Ethiopia": "Africa", "Gabon": "Africa", "Gambia": "Africa",
    "Ghana": "Africa", "Guinea": "Africa",
    "Guinea-Bissau": "Africa", "Ivory Coast": "Africa",
    "Kenya": "Africa", "Lesotho": "Africa", "Liberia": "Africa",
    "Libya": "Africa", "Madagascar": "Africa", "Malawi": "Africa",
    "Mali": "Africa", "Mauritania": "Africa", "Mauritius": "Africa",
    "Morocco": "Africa", "Mozambique": "Africa",
    "Namibia": "Africa", "Niger": "Africa", "Nigeria": "Africa",
    "Rwanda": "Africa", "Sao Tome and Principe": "Africa",
    "Senegal": "Africa", "Seychelles": "Africa",
    "Sierra Leone": "Africa", "Somalia": "Africa",
    "South Africa": "Africa", "South Sudan": "Africa",
    "Sudan": "Africa", "Tanzania": "Africa", "Togo": "Africa",
    "Tunisia": "Africa", "Uganda": "Africa", "Zambia": "Africa",
    "Zimbabwe": "Africa", "Réunion": "Africa",
    "Saint Helena": "Africa",

    # --- Oceania ---
    "Australia": "Oceania", "Fiji": "Oceania",
    "Kiribati": "Oceania", "Marshall Islands": "Oceania",
    "Micronesia": "Oceania", "Nauru": "Oceania",
    "New Zealand": "Oceania", "Palau": "Oceania",
    "Papua New Guinea": "Oceania", "Samoa": "Oceania",
    "Solomon Islands": "Oceania", "Tonga": "Oceania",
    "Tuvalu": "Oceania", "Vanuatu": "Oceania",

    # --- Territories ---
    "American Samoa": "Oceania", "Anguilla": "North America",
    "Aruba": "North America", "Bermuda": "North America",
    "British Virgin Islands": "North America",
    "Cayman Islands": "North America", "Cook Islands": "Oceania",
    "Curaçao": "North America",
    "Falkland Islands": "South America", "Faroe Islands": "Europe",
    "French Guiana": "South America",
    "French Polynesia": "Oceania", "Gibraltar": "Europe",
    "Greenland": "North America", "Guadeloupe": "North America",
    "Guam": "Oceania", "Martinique": "North America",
    "Montserrat": "North America", "New Caledonia": "Oceania",
    "Niue": "Oceania", "Northern Mariana Islands": "Oceania",
    "Puerto Rico": "North America", "Sint Maarten": "North America",
    "Turks and Caicos Islands": "North America",
    "US Virgin Islands": "North America",
    "Wallis and Futuna": "Oceania",
}


# =============================================================================
# CONTINENT -> COUNTRIES
# =============================================================================
CONTINENT_COUNTRIES = {}
for _country, _continent in COUNTRY_CONTINENT.items():
    CONTINENT_COUNTRIES.setdefault(_continent, []).append(_country)
del _country, _continent


# =============================================================================
# CONTINENT METADATA
# =============================================================================
CONTINENTS = [
    "Africa", "Asia", "Europe",
    "North America", "Oceania", "South America",
]

CONTINENT_AREA_KM2 = {
    "Africa":        30_370_000,
    "Asia":          44_579_000,
    "Europe":        10_180_000,
    "North America": 24_709_000,
    "Oceania":        8_526_000,
    "South America": 17_840_000,
}

CONTINENT_POPULATION = {
    "Africa":        1_340_000_000,
    "Asia":          4_680_000_000,
    "Europe":          748_000_000,
    "North America":   592_000_000,
    "Oceania":          43_000_000,
    "South America":   430_000_000,
}


__all__ = [name for name in dir() if name.isupper() and not name.startswith("_")]