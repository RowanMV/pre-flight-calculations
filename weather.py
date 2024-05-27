raw = input('Input the weather forecast: ')

# Decoding
cloud = {
    'FEW': 'few',
    'SCT': 'scattered',
    'BKN': 'broken',
    'OVC': 'overcast'
}


if 'TAF' in raw:
    # Start processing a standard TAF message
    pass
elif 'METAR' in raw:
    # Start processing a standar METAR message
    data = raw.split()
    ad = data[1]
    day = data[2][:2]
    time = data[2][2:]
    wind = data[3]
    vis = data[4]
    pass
