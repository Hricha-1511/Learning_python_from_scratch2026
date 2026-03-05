# printing sum of first n natural numbers

def print_sum_n_num(n):
    sum=0
    for i in range(1,n+1):
        print (i)
        sum=sum+i
    print(sum)    

print_sum_n_num(5)
