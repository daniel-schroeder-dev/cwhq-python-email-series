file_handle = open("users.txt", mode="rt")  # Opens `users.txt` in read text (rt) mode.
file_text = file_handle.read()

print(file_text)

file_handle.close()
