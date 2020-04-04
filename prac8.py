count characters
fname=input("Enter file name:")
char=input("Enter the character to be searched:")
with open (fname,'r') as f:
words=f.read().lower().count(char)
print(f"File {fname} has {words} instances of letter {char}")
