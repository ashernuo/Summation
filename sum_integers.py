def sum_even_numbers():
    sum=0

    for i in range(1, 10000):
        sum=sum+i
        i=i+1
    print("Sum is ", sum)
sum_even_numbers()