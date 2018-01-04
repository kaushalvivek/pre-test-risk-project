class User () :
    '''
    Contains details about the user and game settings.
    
    Modes:

    1. Random Positive Negative
    2. All Positive
    3. All Negative
    4. First Five Positive, then Negative
    5. First Five Negative, then Positive
    6. Alternative Positive Negative
    7. Couple Positive, Couple Negative
    8. 1 Negative after 3 Positives.
    9. 1 Positive after 3 Negatives

    Scenarios:

    1. Without Company
    2. -- Contact Ma'am for specifications. --
    
    '''
    mode = -1
    scenario = -1
    name = ""
    email = ""
    age = ""
    branch = ""

    def log () :
        pass