# Asks for an input from the user as a mark.
# If the mark is greater that 85 print "Distinction"
# If the mark is between 65 and 85 print "Pass"
# Anything else print "Fail"
# Try to do this both with and without elif statements.

m = int(input("Please enter in your mark: "))

if m >= 85:
    print("Distinct")
if m <85 and m >=65:
    print("Pass")
if m <= 65:
    print("Fail")