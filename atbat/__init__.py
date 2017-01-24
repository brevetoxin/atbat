import math

def validateProbabilities(b, p, l):
    if b < 0.0 or b > 1.0:
        raise ValueError('Batter probability must be between 0.0 and 1.0')
    if p < 0.0 or p > 1.0:
        raise ValueError('Pitcher probability must be between 0.0 and 1.0')
    if l <= 0.0 or l > 1.0:
        raise ValueError('League probability must be greater than 0 and less than or equal to 1.0')

def log5(b, p, l):
    validateProbabilities(b, p, l)
    return ((b*p)/l)/(((b*p)/l)+(((1-b)*(1-p))/(1-l)))

def moreyZ(b, p, l):
    validateProbabilities(b, p, l)
    return ((((b-l)/math.sqrt(l*(1-l)))+((p-l)/math.sqrt(l*(1-l))))/math.sqrt(2))*(math.sqrt(l*(1-l)))+l
