
def remove_words_occuring_once(sentences):
    word_count = {}
    updated_sentences = []

    for sentence in sentences:
        words = sentence.split()
        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

    for sentence in sentences:
        words = sentence.split()
        updated_words = [word for word in words if word_count[word] > 1]
        updated_sentence = ' '.join(updated_words)
        updated_sentences.append(updated_sentence)

    return updated_sentences


with open('file1.txt', 'r') as file1:
    sentences = file1.readlines()

updated_sentences = remove_words_occuring_once(sentences)

with open('file2.txt', 'w') as file2:
    file2.write('\n'.join(updated_sentences))
