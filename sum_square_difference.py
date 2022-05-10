def difference(num):
    squared_num = sum([x**2 for x in range(1,num+1)])
    num_squared = (sum([x for x in range(1,num+1)]))**2

    print(num_squared - squared_num)

difference(100)