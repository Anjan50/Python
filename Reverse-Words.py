def rev_sentence(sentence):
    words = sentence.split(' ')
    reverse_sentence = ' '.join(reversed(words))
    return reverse_sentence


x = input("Enter a line :")
print(rev_sentence(x))
