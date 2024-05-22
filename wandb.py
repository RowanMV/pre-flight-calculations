# Currently need 2 unit converters, one from pounds to kg and one from inches to metre

def weightconv(pounds: float) -> float:
    '''
    Takes weight in pounds as input and converts it to kilogrammes'''
    return pounds*0.453592

def lengthconv(inches: float) -> float:
    '''
    Takes length in inches as input and converts it to metres'''
    return inches*0.0254

def weightinp(raw: str) -> float:
    '''
    Takes as input the string inputted by the user, detects the units and converts it floato an floateger in kilogrammes'''
    weightdata = raw.split(1)
    weighttypes = {"lbs", "pounds", "lb"}
    if weightdata[1] in weighttypes:
        weightconv(weightdata[0])

def lengthinp(raw: str) -> float:
    '''
    Takes as input the string inputted by the user, detects the units and converts it floato an floateger in metres'''
    lengthdata = raw.split(1)
    lengthtype = {"inch", "inches", "in"}
    if lengthdata[1] in lengthtype:
        lengthconv(lengthdata[0])

def check(raw: str) -> bool:
    '''
    Function checks if any numbers have been added as input'''
    for char in raw:
        if char.isnumeric():
            return True
    return False
