import re
pattern = r'^(?!.*\.\.)(?!.*[.-]$)(?!.*[.-]{2})([a-zA-Z0-9][a-zA-Z0-9_.+-]{0,62})@([a-zA-Z0-9-]+\.[a-zA-Z]{2,})(?<!-)$'
n=input("Enter an email address to validate:") 
if re.match(pattern,n):
        print("Valid email address.")
else:
        print("Invalid email address.")
