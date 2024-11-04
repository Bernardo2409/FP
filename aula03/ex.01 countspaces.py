def main() :
   def countSpaces(text):
        spaces = 0
        for char in text :
            if char == " " :
                spaces +=  1
        return spaces
   userInput = input("Enter a string: ")
   spaces = countSpaces(userInput)
   print(spaces)

main()