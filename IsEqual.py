print("first number")
first = input()
print("second number")
second = input()
print("third number")
third = input()
allOfTheNumbersAreEqual = first == second and second == third and third == first
print("All are equal:", allOfTheNumbersAreEqual)
anyOfTheNumbersAreEqual = first == second or second == third or third == first
print("Any of three are equal:", anyOfTheNumbersAreEqual)