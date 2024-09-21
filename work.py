input1 = input("Enter a sentence - ")
def is_panagram(input1):
    return set('abcdefghijklmnopqrstuvwxyz').issubset(set(input1.lower()))

if is_panagram(input1):
    print("This sentence is a panagram.")
else:
    print("This sentence is not a pangram")