'''United States of America Python Dictionary to find the tax rates'''

# Dedicated to the public domain.

# All Data was collected from the states official websites


us_state_tax_rate = {
    "Alabama": 4,
    "Alaska": 0,
    "Arizona": 5.6,
    "Arkansas": 6.5,
    "California": 7.25,
    "Colorado": 2.9,
    "Connecticut": 6.35,
    "Delaware": 0,
    "Florida": 6,
    "Georgia": 4,
    "Hawaii": 4,
    "Idaho": 6,
    "Illinois": 6.25,
    "Indiana": 7,
    "Iowa": 6,
    "Kansas": 6.50,
    "Kentucky": 6,
    "Louisiana": 4.45,
    "Maine": 5.50,
    "Maryland": 6,
    "Massachusetts": 6.25,
    "Michigan": 6,
    "Minnesota": 6.5,
    "Mississippi": 7,
    "Missouri": 4.225,
    "Montana": 0,
    "Nebraska": 5.5,
    "Nevada": 6.85,
    "New Hampshire": 0,
    "New Jersey": 6.625,
    "New Mexico": 5,
    "New York": 4.5,
    "North Carolina": 4.75,
    "North Dakota": 5,
    "Ohio": 5.75,
    "Oklahoma": 4.5,
    "Oregon": 0,
    "Pennsylvania": 6,
    "Rhode Island": 7,
    "South Carolina": 6,
    "South Dakota": 4.5,
    "Tennessee": 7,
    "Texas": 6.25,
    "Utah": 4.7,
    "Vermont": 6,
    "Virginia": 5.3,
    "Washington": 6.5,
    "West Virginia": 6,
    "Wisconsin": 5,
    "Wyoming": 4,
    "District of Columbia": 6,
    "American Samoa": 15,
    "Guam": 4,
    "Northern Mariana Islands": 7,
    "Puerto Rico": 10.5,
    "United States Minor Outlying Islands": 7,
    "U.S. Virgin Islands": 0,
}

# inverted / reversed version
inverted_us_state_tax_rate = (dict(map(reversed, us_state_tax_rate.items())))