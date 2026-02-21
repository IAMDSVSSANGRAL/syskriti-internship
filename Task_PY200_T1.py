x = [2,3,4,5,6,7,9,10,4,5,5,7]
y = [2,3,4,5,6,7,5,9,10,4,5,5,7]

# This function calculate the mean for the list
def mean(x):
   sum = 0 
   n = len(x)

   for i in x:
      sum = sum+i
      mean = sum/n
   
   return f'MEAN FOR THE LIST IS {mean}'



#This function calculate the median for the list 
def median(x):
   sort_x = sorted(x)
   n = len(x)
   if n%2==1:
      index = int((n+1)/2)
      return f'MEDIAN FOR LIST = {sort_x[index]}'
   else :
      index_1 = int(n/2)
      median = (sort_x[index_1]+sort_x[index_1+1])/2
      return f'MEDIAN FOR LIST = {median}'
   

#this function calculate the mode for the list
def mode(x):

   freq ={}

   for i in x:
      if i in freq:
         freq[i]+= 1
      else:
         freq[i] = 1

   max_freq = max(freq.values())
   
   x = []

   for item,value in freq.items():
      if value == max_freq:
         x.append(item)
   
   return f'MODE = {x}'


print(mode(x))
print(mean(x))
print(median(x))
print(median(y))





