'''
s=str(input("Enter the string"))
s = ''.join(char for char in s if char.isalnum())
n=len(s)
is_palindrome =True
for i in range (n//2):
    if s[i] != s[n - i -1]:
        is_palindrome = False
        break
if is_palindrome:
    print("It's a palindrome!")
else:
    print("It's not a palindrome!")
'''
def is_palindrome(s):
    #onos = s.lower().replace(" ", "")  # Convert to lowercase and remove spaces
    return s == s[::-1]  # Check if it equals its reverse

# Example usage
string = input("Enter a string: ")
if is_palindrome(string):
    print("It's a palindrome!")
else:
    print("It's not a palindrome!")

