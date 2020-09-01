#This script reads any files in the same directory ending in '.out', checks for the pattern phrase, and returns a list of files containing the phrase.

#Creates a list with all files to check
list_of_files = []
import os
for filename in os.listdir():
  if filename.endswith('.out'):
    list_of_files.append(filename)

#Function to diferenciate lists
def divide_lists(list1,list2):
  return list(set(list1) - set(list2))

secret_files_list = []
pattern = "pinapple"

#Appends each filename into secret_files_list
for each_file in list_of_files:
  with open(each_file) as current_file:
    for line in current_file:
      if pattern in line:
        secret_files_list.append(current_file.name)

#Creates a list of negative files and writes it to negative_files.txt
negative_files = divide_lists(list_of_files, secret_files_list)
file = open("negative_files.txt", "w")
file.write('No secrets contained in:\n')
file.write(str(negative_files))
file.close()

#Removes duplicate list items
final_secret_list = list(dict.fromkeys(secret_files_list))


#Additional filter, files containing the secret phrase and exempt phrase will not be considered secret.

exempt_phrase = "pizza" #Filter phrase
def optional_filter(secondary_phrase):
  exempt_list=[]
  for each_file in secret_files_list:
    with open(each_file) as current_file:
      for line in current_file:
        if exempt_phrase in line:
          exempt_list.append(current_file.name)
        final_secret_list = divide_lists(secret_files_list, exempt_list) 
  return(final_secret_list)

final_secret_list = optional_filter(exempt_phrase) #Assigns return of function to final_secret_list, to override the unfiltered variable

#Writes the list of files containing the secret word into secret_files.txt
file = open("secret_files.txt", "w")
file.write("These file contain the secret phrase:\n")
file.write(str(final_secret_list))
file.close()
