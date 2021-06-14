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
    if len(sequence)<2:
        return sequence
    else:
        shift=sequence[0]
        remainder=get_permutations(sequence[1:])
        permutations=[]
        for word in remainder:
            for letter in range(len(word)+1):
                permutations.append(word[:letter]+shift+word[letter:])
        return permutations

if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)
    input="bad"
    print("Input",input)
    print("Expected Output:",["bad","abd","adb","dab","dba","bda"])
    print("Actual Output:",get_permutations(input))
    input="ham"
    print("Input",input)
    print("Expected Output:",["ham","ahm","amh","mah","mha","hma"])
    print("Actual Output:",get_permutations(input))
    input="bot"
    print("Input",input)
    print("Expected Output:",['bot', 'obt', 'otb', 'bto', 'tbo', 'tob'])
    print("Actual Output:",get_permutations(input))

