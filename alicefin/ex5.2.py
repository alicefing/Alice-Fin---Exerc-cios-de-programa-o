
phrase = input ("type a phrase: ")
words = phrase.split ()
words_with_a = [w for w in words if "a" in w]

repleaced_a_by_o = [w.replace ("a", "o") for w in words_with_a]
print (repleaced_a_by_o)

