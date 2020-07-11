try:
    def digitsum(n): #function to find the power of cards
        sum = 0
        while (n != 0):
            sum = sum + int(n % 10)
            n = int(n/10)
        return sum
    
    t = int(input()) #number of testcases
    
    if t<=1000 and t>=1: #checking constraints of t
        for i in range(t):
            n = int(input())
            if n<=100 and n>=1: #checking constraints of n
                chef = 0
                morty = 0
                #scores of chef and morty
                for j in range(n):
    
                    A, B = map(int, input().split())
    
                    if (A and B >=1) and (A and B <= 10**9):
    
                        if digitsum(A)>digitsum(B):
                            chef = chef+1
                        elif digitsum(A)==digitsum(B):
                            chef = chef+1
                            morty = morty+1
                        else:
                            morty = morty+1
                        cancel = 1
                        #cancel variable is used to allow the printing of scores if condition is true
                    else:
    
                        print("invalid card number")
                        cancel = 0
                if cancel == 1:
    
                    if chef > morty : print("0",chef)
                    elif chef == morty : print("2",chef)
                    else : print("1",morty)
    
            else: print("number of cards cannot be more than 100")
    
    else: print("test cases cannot be more than 1000")

except:
    pass
