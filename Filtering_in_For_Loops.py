
# Filtering in a Loop 
count = 0
summ = 0
num = (19,10,20,40,29,30,93,26,46,183)
for no in num:
    if no > 25:
        print("The number above 25 is :- {}.".format(no))
        count = count + 1 #Only counting values that are above 25 .
        summ = summ + no
        
print("\n\nThe loop executed {} times and there sum is {} .".format(count,summ))