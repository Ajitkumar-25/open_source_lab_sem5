# Function to remove words repeated at least twice in all sentences
def remove_repeated_words(sentences):
    # Split sentences into words
    words = ' '.join(sentences).split()
    
    # Create a dictionary to count word occurrences
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    
    # Filter words occurring at least twice
    filtered_words = [word for word in words if word_count[word] < 2]
    
    # Join the filtered words to form updated sentences
    updated_sentences = ' '.join(filtered_words).split('\n')
    
    return updated_sentences

# Read the content of file1.txt
with open('file1.txt', 'r') as file1:
    sentences = file1.readlines()

# Process sentences to remove words repeated at least twice
updated_sentences = remove_repeated_words(sentences)

# Write the updated content to file2.txt with spaces between lines
with open('file2.txt', 'w') as file2:
    file2.write('\n'.join(updated_sentences))
