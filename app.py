#import the libraries
import json
#for getting the close matches use get_close _matches library
from difflib import get_close_matches

#load the json file
data=json.load(open("data.json"))

#function that calculates the definition for a word
def translate(word):
    word=word.lower() #convert the word into lower case
    if word in data:
        return data[word]
    elif word.title() in data:   #this is used for proper noun
        return data[word.title()]
    elif word.upper() in data: #this is used for USA or NATO
        return data[word.upper()]
    elif len(get_close_matches(word,data.keys()))>0: #for getting the close matches
        yn=input("Did you mean %s instead? Enter Y if yes,or N if no: " % get_close_matches(word,data.keys())[0])
        if yn=="Y":
            return data[get_close_matches(word,data.keys())[0]]
        elif yn=="N":
            return "The word doesn't exist.Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist.Please double check it"
def main():
    while True:
        ch = input("\n1. Search a Word\n2. Exit\n Enter Your Choice: ")
        if ch == '1':
            words =input("Enter word:") #input the word from user
            output = translate(words)
            if type(output)==list:   #check for output list
                for item in output:
                    print(item)
            else:
                print(output)
        elif ch == '2':
            print("Good Bye!!!")
            break
        else:
            print("Invalid Input!!!\nPlease Try Again.")


if __name__ == '__main__':
    main()