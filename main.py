import pandas
#read data from csv file
data = pandas.read_csv("./nato_phonetic_alphabet.csv")

#convert dataframe to dictionary
nato_alphabet = {row.letter: row.code for (index, row) in data.iterrows()}

#ask for input
print(".:::Welcome To Nato Alphabet Helper:::.")
name = input("Enter a word: ").upper()

#print the result
result = [nato_alphabet[letter] for letter in name]
print(result)