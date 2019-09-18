def score(x, y):
    if x**2 + y**2 > 10**2:
        point=0 
    if x**2 + y**2 <= 10**2 and x**2 + y**2 > 5**2: 
        point=1
    if x**2 + y**2 <= 5**2 and x**2 + y**2 > 1**2: 
        point=5   
    if x**2 + y**2 <= 1**2: 
        point=10
    
    return point