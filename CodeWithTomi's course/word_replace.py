def replace_word():
    sent = "hi there, how are you."
    print(sent)

    to_be_rep = input("Enter word to be replaced\n")
    replacement = input("Enter new word\n")
    sent = sent.replace(to_be_rep, replacement)
    
    print(sent)

replace_word()