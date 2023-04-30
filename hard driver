import os
import time

#enter your directory for hard drive where you want the file to be written too
directory_path = "  "
filename = "harddrived.txt"
count = 0
string_to_write = "minute: "

# loop forever
while True:
    with open(os.path.join(directory_path, filename), "w") as file:
        file.write(string_to_write + str(count))
    count+=1
    time.sleep(120)
