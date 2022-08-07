#Student ID: 10982739.
# Student Name: Asher

def sum_prime():
    print("A program to calculate the sum of prime numbers less than a given number")
    
    

    the_number=int(input("Enter the number"))
    total=0
    #Loop starts from 2 because 2 is the first prime number
    for number in range(2, the_number+1):
        i=2
        for i in range (2, number):
            if(number % i==0):
                i=number
                break;
            
        if i is not number:
         total = total + number
    print(f"The sum of prime numbers less than {the_number} is {total}")
sum_prime()