def prime(num):
    prime_list = [2,3,5,7,11,13,17,19]

    for i in range(20, 20+num):
        if any(i%n == 0 for n in prime_list):
            continue
        else:
            prime_list.append(i)
    
    print(prime_list[10000])

prime(120000)