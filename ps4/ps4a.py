# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    if len(sequence) == 1:
        singleton = sequence
        return [singleton]
    else:
        perms = []
        for i in range(len(sequence)):
            the_rest = get_permutations(sequence[:i] + sequence[i+1:])
            for j in range(len(the_rest)):
                perm = sequence[i] + the_rest[j]
                perms.append(perm) 

            #perms.append(sequence[i] + get_permutations(sequence[:i] + sequence[i+1:]))
        return perms
#    pass #delete this line and replace with your code here

if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)
    example_input = 'abcd'
    print('Input:', example_input)   
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))
    example_input = 'bcd'
    print('Input:', example_input)   
    print('Expected Output:', ['bcd', 'bdc', 'cbd', 'cdb', 'dbc', 'dcb'])
    print('Actual Output:', get_permutations(example_input))
    example_input = 'ric'
    print('Input:', example_input)   
    print('Expected Output:', ['ric', 'rci', 'irc', 'icr', 'cri', 'cir'])
    print('Actual Output:', get_permutations(example_input))
    #pass #delete this line and replace with your code here

