# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)


# delete everything and add a new row
# with open("my_file.txt", mode="w") as file:
#     file.write("New text.")


# add to the file without delete
with open("my_file.txt", mode="a") as file:
    file.write("\nNew text3.")


# create a new file
with open("new_file.txt", mode="w") as file:
    file.write("\nNew text.")
