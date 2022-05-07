digits = int(input('Enter number of digits: '))

def largest_product(n):
    
    lprod = 1
    num = int(digits * '9')

    for i in range(num, 0, -1):
        for j in range(num, 0, -1):
            prod = i * j
            
            if (str(prod)[:3] == str(prod)[6:2:-1]):
                if prod > lprod:        
                    lprod = prod
                else:
                    continue
            else:
                continue

    return lprod

print(largest_product(digits))
    