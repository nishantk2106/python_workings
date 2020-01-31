from functools import reduce

nums=[1,2,3,4,5,6,7,8,9,10]
evens=list(filter(lambda n: n%2==0,nums))
odds=list(filter(lambda n: n%2!=0,nums))
double_evens=list(map(lambda evens:evens*2,evens))
double_odds=list(map(lambda odds:odds*2,odds))
sum_evens=reduce(lambda a,b : a+b,double_evens)
sum_odds=reduce(lambda b,a:b-a,double_odds)
print(evens)
print(odds)
print(double_evens)
print(double_odds)
print(sum_evens)
print(sum_odds)