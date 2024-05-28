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

def windspeed(inp: str) -> str:
    '''
    Takes as input the windspeed data and converts it into readable english'''
    if len(inp) == 7:
        out = f'and at a speed of {inp[:2]} knots gusting up to {inp[3:5]} knots'
    elif len(inp) == 4:
        out = f'and at a speed of {inp[:2]} knots'
    return out 