def steps(number):
    i=0 
    while number!= 1: 
        if (number%2) == 0:
            number=(number/2)
        else: 
           number=(3*number+1)/2 
        i=i+1
    return(i)
