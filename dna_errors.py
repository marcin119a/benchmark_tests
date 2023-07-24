import random
from dna_kmers import all_pairs_with_error

def all_pairs_with_error(kmers_12):
    pairs_list = []

    for i in range(len(kmers_12) - 1):
        if 'N' not in kmers_12[i + 1]:
            result = kmers_12[i]
            insert_position = random.randint(0, len(result))
            result = list(result)
            # Convert the list back to a string
            result[insert_position-1] = 'N'
            pair = [''.join(result), kmers_12[i]]
            pairs_list.append(pair)

    return pairs_list

pairs_list_errors = all_pairs_with_error(kmers)

pairs_list_errors

file_name = 'long_dna_errors.txt'

# Writing to a file
with open(file_name, 'w') as file:
    for sublist in pairs_list_errors:
        line = ' '.join(sublist) + '\n'
        file.write(line)
