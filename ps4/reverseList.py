# Example of a function to reverse list recursively

# No variables, no change to list
# This came to me originally as a Scheme exercise and I was trying to remember it here.
# 
# The bit that hung me up was brackets.
# The base case, list of length 1, is still a list and DOES NOT need brackets.
# The recursive case, however, as it takes the head of each sublist, 
# DOES need brackets around item 0 in order add two lists.  
# This was counterintuitive to me at first.
# I think now I see that this because rev() is list -> list

a = [i for i in range(10)]

def rev(a):
    if len(a) == 1:
        return a
    else:
        last = len(a)
        return rev(a[1:]) + [a[0]]

print(a)
print(rev(a))
print(a)
