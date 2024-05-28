from wthrvrbls import cloud, wthr, digits_to_words

raw = input('Input the weather forecast: ')

if 'TAF' in raw:
    # Start processing a standard TAF message
    raise NotImplementedError

elif 'METAR' in raw:
    # Start processing a standar METAR message
    data = raw.split()
    ad = data[1]
    day = data[2][:2]
    time = data[2][2:]
    # Processing wind data
    if len(data[3]) == 7:
        dir = data[3][:3]
        vel = data[3:-2]
        wind = f'{dir} at {vel} knots'
    else:
        dir = data[3][:3]
        vel = data[3:5]
        gust = data [6:-2]
        wind = f'{dir} at {vel} knots gusting to {gust} knots.'
    #  !TODO deal with variable winds
    
    vis = data[4]
    output = f'METAR observation for aerodrome {ad} taken at the {day} day of the month at {time} UTC. Winds are {wind} and visibility is {vis}.'

    # Iterate through each statement in the dataset and check if there is any information about cloud layer
    for statement in data:
        for key in cloud.keys():
            if key in statement:
                level = int(statement[-3:])
                height = str(level * 100)
                cldtype = cloud[statement[:3]]
                if 'TCU' in statement:
                    # Additional processing for towering cumulus
                    output += f' {cldtype} towering cumulus at {height} feet.'
                
                elif 'CB' in statement:
                    # Additional processing for cumulonimbus
                    output += f' {cldtype} cumulonimbus at {height} feet.'
                
                else:
                    output += f' {cldtype} at {height} feet.'
                    
        # Check if input begins with Q and has 4 digits following
        if statement.startswith('Q') and len(statement) == 5 and statement[1:].isdigit():
            # Keep the numbers portion
            qnh_numbers = statement[1:]
            output += f'Local pressure setting is {qnh_numbers} hPa. '
    print(output)    
