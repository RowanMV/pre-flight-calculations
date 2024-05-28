from wthrvrbls import cloud, wthr, digits_to_words, windspeed

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

    # Check if METAR is automatically generated
    if 'AUTO' in data:
        data.remove('AUTO')
        output = 'Automatically generated '
    else:
        output = ''


    # Processing wind data 180V240 12G18KT, VRB05KT, 140V200 08KT, 12008KT, 31015G27KT
    if data[3][3] == 'V':  
        # Only true for if wind direction varies within a range
        dir = f'variable from between {data[3][:3]} and {data[4:]}'
        vel = windspeed(data[4])
        vis = data[5]
        wind = dir + vel
    elif data[3][-2:] == 'KT':  
        # Only true if wind speed information is contained
        if data[3][:3] == 'VRB':
            dir = 'variable'
        else:
            dir = f'from {data[3][:3]}'
        vel = windspeed(data[3][3:])
        vis = data[4]
        wind = vel + dir
    
    
    output += f'METAR observation for aerodrome {ad} taken at the {day} day of the month at {time} UTC. Winds are {wind}. Visibility is {vis}.'

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