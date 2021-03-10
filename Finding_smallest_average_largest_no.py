# Finding Smallest Number , Largest Number ,Average of it in Python .
small_no = None
lar =0
count = 0
summ = 0
nos = (101,40,60,80,194,30,10,20,44,132)
for numb in nos:
    count = count +1 
    summ = summ + numb
    if numb > lar:
        lar = numb 
    print("The current Number is {} , The largest number till now :- {} .".format(numb,lar))
    print("Loop executed total {} times for Largest Number .".format(count)) # Number of times loop executed .
    print("total sum :- {}.".format(summ)) # Sum (Total)
    print("Average found is :- {}".format(summ/count)) # Average 
    print("-------------------------------------------------------------------------------------\n\n")
for var in nos:
    if small_no == None:
        small_no = var
    elif var < small_no:
        small_no = var
    print("\n\n Current Number :- {} and smallest number :- {}".format(var,small_no))


    






