# Currently need 2 unit converters, one from pounds to kg and one from inches to metre

def weightconv(pounds: int) -> int:
    '''
    Takes weight in pounds as input and converts it to kilogrammes'''
    raise NotImplementedError

def lengthconv(inches: int) -> int:
    '''
    Takes length in inches as input and converts it to metres'''
    raise NotImplementedError

def weightinp(raw: str) -> int:
    '''
    Takes as input the string inputted by the user, detects the units and converts it into an integer in kilogrammes'''
    raise NotImplementedError

def lengthinp(raw: str) -> int:
    '''
    Takes as input the string inputted by the user, detects the units and converts it into an integer in metres'''
    raise NotImplementedError