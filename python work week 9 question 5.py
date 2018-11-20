# Counts the number of spaces

def count_space(userInput):
        spaces=0
        for char in userInput:
            if char ==" ":
                spaces=spaces+1
        return spaces
    
            
def main():
    userInput=input("Write something: ")
    print(count_space(userInput))
main()
