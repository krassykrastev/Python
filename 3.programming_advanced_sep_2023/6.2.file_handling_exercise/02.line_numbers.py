# Write a program that reads a text file, inserts line numbers in front of each line, and counts all the letters and
# punctuation marks. The result should be written in another text file.
#
# text2.txt
# -I was quick to judge him, but it wasn't his fault.
# -Is this some kind of joke?! Is it?
# -Quick, hide here. It is safer.
#
# output2.txt:
# Line 1: -I was quick to judge him, but it wasn't his fault. (37)(4)
# Line 2: -Is this some kind of joke?! Is it? (24)(4)
# Line 3: -Quick, hide here. It is safer. (22)(4)

with open("text2.txt", "r") as file:
