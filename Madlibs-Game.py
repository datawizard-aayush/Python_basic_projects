#MADLIBS Game
# Word game where you can create story by filling blanks with random words
print("\033[1;4m ***---Welcome to the Mad libs game---***\033[0m")
# 👆 printing in bold (1m) and underlined (4m) in python
print("\033[94m Here we fill in the blanks of a story with words to create a funny story.\033[0m") #blue color text(94m)
# Function to determine if "a" or "an" is appropriate
def a_or_an(word):
    if word[0].lower() in "aeiou":
        return "an"
    else:
        return "a"
adjective1=input("enter an adjective[1] (description) ")
noun1=input("enter a noun (person,place,thing) ")
adjective2=input("enter an adjective[2] (description) ")
verb1=input("enter a verb ending (with ing) ")
adjective3=input("enter an adjective[3] (description) ")
print("\n") #for leaving the necessary lines
print(f"Today I went to a  {a_or_an(adjective1)} {adjective1} zoo.")
print(f"In an exhibit, I saw a {a_or_an(noun1)} {noun1}.")
print(f"{noun1} was {adjective2} and {verb1}.")
print(f"I was {adjective3 } !")