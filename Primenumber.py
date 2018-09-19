num = int(input("Enter number to determine if prime number: "))
def prime(num):
    if num < 2:
        return(False) 
    if num == 2:
        return(False)
    else:
        for div in range(2,num):
            if num % div == 0:
                return(False)  
        return(True) 

def is_prime():
    if prime(num) == False:
        print("False")
    else:
        print("True")



prime(num)
is_prime()
