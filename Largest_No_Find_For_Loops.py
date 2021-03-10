# Largest Number Finder in a Given List , Using For Loop .
largest_no = 0
no_list = [10,12,24,50,23,32,95,59,84]
for no in no_list:
    if no > largest_no :
        largest_no = no
    print("Current Number :- {} , Largest Number in the given List is :- {} .".format(no,largest_no))
print("Process End !!!!")
