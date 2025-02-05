import string

def clean_word(word):
    return word.lower().strip(string.punctuation)

def is_palindrome(word):
    word = clean_word(word)
    return word == word[::-1]

def get_words(sentence):
    return sentence.split()

def count_palindromes_in_list(words):
    count = 0
    for word in words:
        if is_palindrome(word):
            count += 1
    return count

def count_palindromes_in_sentence(sentence):
    words = get_words(sentence)
    return count_palindromes_in_list(words)

def main():
    sentence = input("Enter a sentence: ")
    palindrome_count = count_palindromes_in_sentence(sentence)
    print(f"The number of palindromes in the sentence:{palindrome_count}")
    
main()