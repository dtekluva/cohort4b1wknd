sweet = input('Enter the no of sweets of Friend_1,Friend_2,Friend_3:').split(',')
def divide_equally (sweet):
    Total_sweet =(int(sweet[0])+int(sweet[1])+int(sweet[2]))
    no_of_friends = 3
    shared_equally = Total_sweet // no_of_friends
    remainder = Total_sweet % no_of_friends
    print('HELLO GUYS, EACH OF YOU SHOULD GET',  shared_equally, 'SWEETS AND',remainder, 'SHOULD BE DISCARDED')
    
