i = 100

while i < 1000:
    sum_i = i + i + i
    i_str = str(i) # convert from integer to string so that wer can subscript or index
    last_char = i_str[2]
    last_char_multiple = last_char * 3
  
    if sum_i == int(last_char_multiple):

        print(i, sum_i, last_char, last_char_multiple)
        break

    i+=1