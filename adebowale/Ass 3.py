suggestion = input('Write a word\n:')
reversed_suggestion = (list(reversed(suggestion)))
join_word = ''.join(reversed_suggestion)
print(join_word)
if suggestion == join_word:
    print(f'{suggestion} is a palindrome')
else:
    print(f'{suggestion} is not a palindrome')

