# Please write a program to check if a word is a palindrome. ie remains the same even if it is reversed.

# word=input("which word are you testing?: ")
# reverse= word[::-1]       #(start, stop and step)
# print(word)
# print(reverse)
# if word==reverse:
#     print(f"yes, {word} is a Palindrome")
# else:
#     print(f"naa, {word} is not a Palindrome")

# #to reverse high level
# txt= ("level","what","talking","about")
# print(list(reversed(txt)))

word = "boy"
# print(list(reversed(word)))
# reverse = reversed(word)
# answer = "".join((reverse))
# print((answer))

word = "copy my work"
reverse = "".join(reversed(word))      #.join is a string methonds but you still use it in the front
reverse = "-".join(reversed(word))       #so .join is in the front and the delimited in front
reverse = "/".join(reversed(word))
reverse = " ".join(reversed(word))
print(reverse)

ans ="jan-drf-001/FNTC2003"
solution = ans.split("/")      #.split by the already set delimiter. 
print(solution)                #while .split is at the back and the delimiter at the back as well.





