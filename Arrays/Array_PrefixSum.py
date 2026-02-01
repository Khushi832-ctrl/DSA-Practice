# sum of all element in an array 
# Write Python code to find sum of all element and printing the running sum after each step
arr = [1,2,3,4,5]
total = 0
for x in arr:
    total += x #update total 
    print(total) #print after every update #inside loop
    #code inside loop runs every iteration # prefix sum
    #code outside loop runs once # total sum
    #this is called prefix sum
