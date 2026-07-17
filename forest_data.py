FOREST_OPTIONS = [
    {"name": "Bandipur National Park", "state": "Karnataka", "latitude": 11.6627, "longitude": 76.6330},
    {"name": "Bandipur Forest", "state": "Karnataka", "latitude": 11.6627, "longitude": 76.6330},
    {"name": "Bandipur Tiger Reserve", "state": "Karnataka", "latitude": 11.6627, "longitude": 76.6330},
    {"name": "Nagarhole National Park", "state": "Karnataka", "latitude": 11.9530, "longitude": 76.1590},
    {"name": "Periyar National Park", "state": "Kerala", "latitude": 9.5300, "longitude": 77.2000},
    {"name": "Mudumalai National Park", "state": "Tamil Nadu", "latitude": 11.5800, "longitude": 76.5330},
    {"name": "Silent Valley National Park", "state": "Kerala", "latitude": 11.0830, "longitude": 76.4330},
    {"name": "Kanha National Park", "state": "Madhya Pradesh", "latitude": 22.3350, "longitude": 80.6110},
    {"name": "Pench National Park", "state": "Madhya Pradesh", "latitude": 21.7610, "longitude": 79.6220},
    {"name": "Gir Forest", "state": "Gujarat", "latitude": 21.1240, "longitude": 70.8240},
    {"name": "Gir National Park", "state": "Gujarat", "latitude": 21.1240, "longitude": 70.8240},
    {"name": "Gir Sanctuary", "state": "Gujarat", "latitude": 21.1240, "longitude": 70.8240},
    {"name": "Kaziranga National Park", "state": "Assam", "latitude": 26.5760, "longitude": 93.1710},
    {"name": "Manas National Park", "state": "Assam", "latitude": 26.7160, "longitude": 91.0000},
    {"name": "Jim Corbett National Park", "state": "Uttarakhand", "latitude": 29.5300, "longitude": 78.7720},
    {"name": "Corbett Tiger Reserve", "state": "Uttarakhand", "latitude": 29.5300, "longitude": 78.7720},
    {"name": "Dudhwa National Park", "state": "Uttar Pradesh", "latitude": 28.4910, "longitude": 80.6050},
    {"name": "Sundarbans National Park", "state": "West Bengal", "latitude": 21.9497, "longitude": 89.1833},
    {"name": "Sundarbans", "state": "West Bengal", "latitude": 21.9497, "longitude": 89.1833},
    {"name": "Sariska Tiger Reserve", "state": "Rajasthan", "latitude": 27.3214, "longitude": 76.4316},
    {"name": "Bhadra Wildlife Sanctuary", "state": "Karnataka", "latitude": 13.7100, "longitude": 75.6460},
    {"name": "Bandhavgarh National Park", "state": "Madhya Pradesh", "latitude": 23.6850, "longitude": 80.9670},
    {"name": "Ranthambore National Park", "state": "Rajasthan", "latitude": 26.0170, "longitude": 76.5020},
    {"name": "Simlipal National Park", "state": "Odisha", "latitude": 21.9380, "longitude": 86.3490},
    {"name": "Tadoba Andhari Tiger Reserve", "state": "Maharashtra", "latitude": 20.3030, "longitude": 79.4490},
    {"name": "Bannerghatta National Park", "state": "Karnataka", "latitude": 12.8000, "longitude": 77.5770},
    {"name": "Anshi National Park", "state": "Karnataka", "latitude": 14.9950, "longitude": 74.3560},
    {"name": "Dandeli Wildlife Sanctuary", "state": "Karnataka", "latitude": 15.2360, "longitude": 74.6170},
    {"name": "Pushpagiri Wildlife Sanctuary", "state": "Karnataka", "latitude": 12.6600, "longitude": 75.6800},
    {"name": "Sharavathi Valley Wildlife Sanctuary", "state": "Karnataka", "latitude": 14.1700, "longitude": 74.8500},
    {"name": "Brahmagiri Wildlife Sanctuary", "state": "Karnataka", "latitude": 12.1800, "longitude": 75.8500}
]


def get_searchable_forests(search_term: str = ""):
    filtered = [forest for forest in FOREST_OPTIONS if search_term.lower() in forest["name"].lower()]
    return filtered or FOREST_OPTIONS
