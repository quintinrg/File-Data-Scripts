#This script reads any files in the same directory ending in '.out', checks for the pattern phrase, and returns a list of files containing the phrase.

#Creating a list with all outputs files
list_of_files = []
import os
for filename in os.listdir():
  if filename.endswith('.out'):
    list_of_files.append(filename)

#Defining a function to diferenciate lists
def differentiate_lists(list1,list2):
  return list(set(list1) - set(list2))

###Verification of normal termination
secret_files_list = []
pattern = "pinapple"


#Appending each filename into secret_files_list
for each_file in list_of_files:
  with open(each_file) as current_file:
    for line in current_file:
      if pattern in line:
        secret_files_list.append(current_file.name)

#creating a list of fail calculations and saving on a txt file
negative_files = differentiate_lists(list_of_files, secret_files_list)
file = open("negative_files.txt", "w")
file.write('No secrets contained in:\n')
file.write(str(negative_files))
file.close()

###Looking for imaginary modes on the files that terminated normally
imaginary_pattern="***imaginary mode***"
imaginary_list=[]

for each_file in secret_files_list:
  with open(each_file) as current_file:
    for line in current_file:
      if imaginary_pattern in line:
        imaginary_list.append(current_file.name)
                
imaginary_list=list(dict.fromkeys(imaginary_list))   #removing duplicated itens on the list

#Creating negative_files.txt, and writing list of .out files not containing the secret word
# file = open("negative_files.txt", "w")
# file.write('\nThese files do not contain the secret word:\n')
# file.write(str(imaginary_list))
# file.close()

#Creating a list with files that terminated normally and has only real frequencies
real_frequencies_list=differentiate_lists(secret_files_list,imaginary_list)

#Adding the list of files containing the secret word into secret_files.txt
file = open("secret_files.txt", "w")
file.write("These files terminated normally and contain the secret word:\n")
file.write(str(real_frequencies_list))
file.close()
print(secret_files_list)
