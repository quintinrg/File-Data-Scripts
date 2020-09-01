#This script reads any files in the same directory ending with the given suffix, checks for the pattern phrase, and returns a list of files containing the phrase.

file_type = ".out" #Change to .txt, etc
pattern = "pineapple"
exempt_phrase = "pizza" #Files containing both this exempt phrase and the main phrase, will be not be considered secret files

#Creates a list and appends files to check
list_of_files = []
import os
for filename in os.listdir():
  if filename.endswith(file_type):
    list_of_files.append(filename)

#Function to diferenciate lists
def divide_lists(list1,list2):
  return list(set(list1) - set(list2))

secret_files_list = []

#Appends each filename into secret_files_list
for each_file in list_of_files:
  with open(each_file) as current_file:
    for line in current_file:
      if pattern in line:
        secret_files_list.append(current_file.name)

#Creates a list of negative files and writes it to negative_files.txt
# negative_files = divide_lists(list_of_files, secret_files_list) Redundant? Testing needed
#Removes duplicate list items
# final_secret_list = list(dict.fromkeys(secret_files_list)) #Redundant? Testing needed

#Exempting filter
def optional_filter(secondary_phrase):
  exempt_list= []
  final_secret_list = []
  for each_file in secret_files_list:
    with open(each_file) as current_file:
      for line in current_file:
        if exempt_phrase in line:
          exempt_list.append(current_file.name)
        final_secret_list = divide_lists(secret_files_list, exempt_list) 
  return(final_secret_list)

final_secret_list = optional_filter(exempt_phrase) #Assigns return of function to final_secret_list, to override the unfiltered variable

reject_files = []
for file in list_of_files:
  if file not in final_secret_list:
    reject_files.append(file)
print(reject_files)

#Writes rejected list to file
file = open("reject_files.txt", "w")
file.write('No secrets contained in:\n')
file.write(str(reject_files))
file.close()

#Writes the list of files containing the secret word into secret_files.txt
file = open("secret_files.txt", "w")
file.write("These file contain the secret phrase:\n")
file.write(str(final_secret_list))
file.close()
