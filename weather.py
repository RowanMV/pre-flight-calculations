raw = input('Input the weather forecast: ')

# Decoding dictionaries
cloud = {
    'FEW': 'Few clouds',
    'SCT': 'Scattered layer',
    'BKN': 'Broken layer',
    'OVC': 'Overcast layer'
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
    output = f'METAR observation for aerodrome {ad} taken at the {day} day of the month at {time} UTC. Winds are {wind} and visibility is {vis}. '

    # Iterate through each statement in the dataset and check if there is any information about cloud layer
    for statement in data:
        for key in cloud.keys():
            if key in statement:
                level = int(statement[-3:])
                height = str(level * 100)
                cldtype = cloud[statement[:3]]
                output += f'{cldtype} at {height} feet. '
                if 'TCU' in statement:
                    # Additional processing for towering cumulus
                    raise NotImplementedError
                
                elif 'CB' in statement:
                    # Additional processing for cumulonimbus
                    raise NotImplementedError

    def decode_metar_qnh(metar_qnh):

        #Dic mapping digits to words
        digits_to_words = {
            '0': 'zero',
            '1': 'one',
            '2': 'two',
            '3': 'three',
            '4': 'four',
            '5': 'five',
            '6': 'six',
            '7': 'seven',
            '8': 'eight',
            '9': 'nine'
        }

    
            
            
        # Check if input begins with Q and has 4 digits following
        if metar_qnh.startswith('Q') and len(metar_qnh) == 5 and metar_qnh[1:].isdigit():
            # Keep the numbers portion
            qnh_numbers = metar_qnh[1:]

        
            
            return qnh_numbers
        else:
            return None

    for statement in data:
        qnh_output = decode_metar_qnh(statement)
        if qnh_output:
            output += f'Local pressure setting is {qnh_output} hPa. '

    
        
    

            
            
                
        


    
    
    
    
    
    
    
    
    
    
    
    
print(output)
    