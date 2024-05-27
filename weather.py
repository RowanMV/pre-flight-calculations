raw = input('Input the weather forecast: ')

# Decoding dictionaries
cloud = {
    'FEW': 'Few clouds',
    'SCT': 'Scattered layer',
    'BKN': 'Broken layer',
    'OVC': 'Overcast layer',
    'NSC': 'No significant cloud'
}
wthr = {
    'BC': 'patches',
    'BL': 'blowing',
    'BR': 'mist',
    'DR': 'drifting',
    'BC': 'duststorm',
    'DU': 'dust',
    'DZ': 'drizzle',
    'FC': 'funnel cloud',
    'FG': 'fog',
    'FU': 'smoke',
    'FZ': 'freezing',
    'GR': 'hail',
    'GS': 'small hail',
    'HZ': 'haze',
    'IC': 'ice crystals',
    'MI': 'shallow',
    'PL': 'ice pellets',
    'PO': 'dust devils',
    'PR': 'banks',
    'RA': 'rain',
    'SA': 'sand',
    'SH': 'showers',
    'SG': 'snow grain',
    'SN': 'snow',
    'SQ': 'squalls',
    'SS': 'sandstorm',
    'TS': 'thunderstorm',
    'VA': 'volcanic ash',
    'VC': 'in vicinity',
    'UP': 'unidentified precipitation'
}


if 'TAF' in raw:
    # Start processing a standard TAF message
    raise NotImplementedError

elif 'METAR' in raw:
    # Start processing a standar METAR message
    data = raw.split()
    ad = data[1]
    day = data[2][:2]
    time = data[2][2:]
    wind = data[3]
    vis = data[4]
    output = f'METAR observation for aerodrome {ad} taken at the {day} day of the month at {time} UTC. Winds are {wind} and visibility is {vis}.'

    # Iterate through each statement in the dataset and check if there is any information about cloud layer
    for statement in data:
        for key in cloud.keys():
            if key in statement:
                level = int(data[-3:])
                height = str(int * 100)
                cldtype = cloud[data[:4]]
                if 'TCU' in statement:
                    # Additional processing for towering cumulus
                    output += f' {cldtype} towering cumulus at {height} feet.'
                
                elif 'CB' in statement:
                    # Additional processing for cumulonimbus
                    output += f' {cldtype} cumulonimbus at {height} feet.'
                
                else:
                    output += f' {cldtype} at {height} feet.'
                
                
                
                

    print(output)
    raise NotImplementedError