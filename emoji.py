message=input("Enter your message")
#split method convert into the list of word
words=message.split()
print(words)
emoji={':)':'🙂',':(':'😥'}
output=''
for word in words:
    output+=emoji.get(word, word)+" "
print(output)
