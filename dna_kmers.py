# Function to extract k-mers from a DNA sequence
def extract_kmers(dna_sequence, k):
    kmers = []
    n = len(dna_sequence)
    for i in range(n - k + 1):
        kmer = dna_sequence[i:i + k]
        kmers.append(kmer)
    return kmers

# Function to read the content of a text file
def read_txt_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print("File not found.")
        return None
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return None

# Example usage of the read_txt_file function
file_path = '/content/seq.txt'
sequence = read_txt_file(file_path).replace('\n', '')

# Function to generate k-mers from a DNA sequence
def generate_kmers(sequence, k):
    kmers = []
    n = len(sequence)
    if k <= 0 or k > n:
        raise ValueError("Invalid value of k.")
    for i in range(n - k + 1):
        kmer = sequence[i:i+k]
        kmers.append(kmer)
    return kmers

# Example usage of the generate_kmers function
k = 6
kmers = generate_kmers(sequence, k)

# Function to create pairs of k-mers
def all_pairs(kmers_12):
    pairs_list = []

    for i in range(len(kmers_12) - 1):
        pair = [kmers_12[i], kmers_12[i + 1]]
        pairs_list.append(pair)

    return pairs_list

pairs_list = all_pairs(kmers)

file_name = 'long_dna.txt'

# Writing to a file
with open(file_name, 'w') as file:
    for sublist in pairs_list:
        line = ' '.join(sublist) + '\n'
        file.write(line)

file_name = 'long_dna.txt'

# Initializing the line counter
line_count = 0

# Opening the file in read mode
with open(file_name, 'r') as file:
    for line in file:
        if 'N' in line.split('\n')[0]:
            line_count += 1

print(f"Number of lines with errors in the file '{file_name}': {line_count}")
