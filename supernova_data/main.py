#After running main.py, new_data.txt will be created. Delete that file when you want to run the program again to avoid appending new data below the previous data.
relevant_data = ""

with open("data.txt") as data_file:
  for line in data_file:
    splitted_line = line.split()
    if "Hel" in line:
     relevant_data = splitted_line[1:3]
    elif "Kin" in line:
      relevant_data = splitted_line[1:4]
    elif "Gal" in line:
      relevant_data = splitted_line[1:4]
    elif "Local Group" in line:
      relevant_data = splitted_line[1:4]
    elif "3K" in line:
      relevant_data = splitted_line[1:4]
    elif "Infall only" in line:
      relevant_data = splitted_line[1:5]
    elif "GA only" in line:
      relevant_data = splitted_line[1:6]
    elif "Shapley" in line:
      relevant_data = splitted_line[1:7]
    #The below line will handle the first line in each set, and remove the spaces.
    else:
      if line == "\n":
        relevant_data = ""
        pass
      else:
        relevant_data = splitted_line[0:1]

    relevant_text = ""

    for each_item in relevant_data:
      relevant_text = relevant_text + " " + each_item
      
#relevant_data into new file
    file = open("new_data.txt", "a")
    file.write(f"{relevant_text} \n")
    file.close()
