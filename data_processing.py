
one = input("Please enter a sentence: ")
print(one.upper())

two = input("Please enter a paragraph: ")
print(f"The paragraph has {len(two.split())} words")

three = input("Please enter a string: ")
print(three.isdigit())

four = input("Please enter another string: ")
print(four.replace("a","o"))

five = input("Please enter your full name: ")
five_formatted = five.split(" ",2)
first = five_formatted[0].title()[0]
second = five_formatted[1].title()[0]
print(f"Your initials are: {first}{second}")

six = input("Please enter one more string: ")
print(f"The length of your string is: {len(six)}")
      

      


