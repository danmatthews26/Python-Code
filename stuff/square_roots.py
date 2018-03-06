#calculate the square root of a perfect square
def square_root(perfect_square):
    ans = 0     #variable to increment  
    while (ans * ans <= perfect_square and ans * ans != perfect_square): #while the sqaure of ans is < and != equal to perfect_square
        ans = ans + 1   #increment ans so it continues to test values
    if (ans * ans == perfect_square):   #if a perfect square has been found
        print("square root is {}".format(ans))  #prints what the answer is 
    else:
        print("Not a perfect square")    

square_root(int(input("Give a number: ")))  #gets user input as an int with a prompt "Give a number: "