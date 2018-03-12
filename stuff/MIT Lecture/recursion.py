#Tests to see if a word is a palindrom (word spelt same backward as forward).
#This example uses recursion

def isPalindrome(s):
    """Returns true if Palindrome, false otherwise"""
    if len(s) <= 1:
        return True
    else:
        #return weather 1st char is same as last, and loops threw the string checking each 
        return s[0] == s[-1] and isPalindrome(s[1:-1])  

  
x = isPalindrome("abaAAcAAaba")        
print(x)
