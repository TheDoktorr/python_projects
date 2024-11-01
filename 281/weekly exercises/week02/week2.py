def Sequence(n=2, initialSequence=None):
    """
    Create a Fibonacci-style sequence up to the nth entry, based on an initial
    two-value sequeunce, where

    x_n = x_{n-1} + x_{n-2}

    Parameter
    ---------
    n: int
        The entry up to which to generate the sequence (n > 0, i.e., n=1 is the
        first entry, etc). Defaults to 2, the length of the initial sequence.
    initialSequence: list
        A list containing the first two values of the sequence, defaulting to
        [0, 1].

    Returns
    -------
    sequence: list
        A list containing the full sequence.
    """

    if initialSequence is None:
        initialSequence = [0, 1]
        
    if not len(initialSequence) > 1:
        raise ValueError("list needs to be at least two elements long to form a sequence")

    if n < 2:
        raise ValueError("n must be the same or larger than the length of the initial sequence")

    # copy and store the initialSequence
    sequence = list(initialSequence)

    # extend and fill in the sequence...
    # take the last element in the list, and add the second to last element:
    for i in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])
    

    return sequence

n = 20
seq = Sequence(n=n)
print(len(seq))
print(seq[-1])