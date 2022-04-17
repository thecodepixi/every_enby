from os import listdir
from os.path import isfile, join, splitext

pos = ["noun", "adjective", "adverb", "verb"]
dict_file_path = './wordnet_temp/'
files = [f for f in listdir(dict_file_path) if isfile(join(dict_file_path, f))]

for file in files: 
  filename = splitext(file)[1][1:]
  txt_file_name = filename + ".txt"
  txt_file = open(txt_file_name, "w")
  contents = open(dict_file_path + file, "r")

  for line in contents: 
    word = line.split(' ')[0].split("_") 
    if len(word) <= 2:
      txt_file.write(" ".join(word) + ",")

  txt_file.close()
