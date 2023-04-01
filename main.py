import pandas
#read data from csv file
data = pandas.read_csv("./nato_phonetic_alphabet.csv")

#convert dataframe to dictionary
nato_alphabet = {row.letter: row.code for (index, row) in data.iterrows()}


print(".:::Welcome To Nato Alphabet Helper:::.")

should_continue = True

while should_continue:
    try:
        name = input("Enter a word: ").upper()
        result = [nato_alphabet[letter] for letter in name]
        should_continue = False 
    except KeyError:
        print("Sorry, You can only enter letters. Try Again!")
        
#print the result
print(result)