def sequence_match(seq_a, seq_b):
    subset = True
    for a in seq_a:
        if a not in seq_b:
            subset = False
    return subset

print(sequence_match([1, 2], [1, 2, 3]))
print(sequence_match([1, 2, 3], [1, 2]))