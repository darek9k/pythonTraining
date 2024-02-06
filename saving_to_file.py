# if w its overwrite
file = open("new_file.txt", "a")
file.write("pice of text")
file.close()

file = open("new_file.txt", "a")
file.write("new text")
file.close()
