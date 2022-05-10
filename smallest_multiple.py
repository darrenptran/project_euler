def smallest(k):        
    n = 1
    
    for i in range(1,k+1):
        if n % i == 0:
            continue
        elif i%2 == 0:
            n *= 2
        elif i%3 == 0:
            n *= 3
        else:
            n *= i 
    
    return n