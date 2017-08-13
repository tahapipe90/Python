#understanding string

t='taha'  #first string
p='pipewala' #second string

print t[0]  #this will print the first letter of string as string start from 0th index
print t[1] 
print t[2]
print t[3]
print t[-1] #this will print the last letter of the string (-1 is used to print the last letter of the string)

#slicing the string 

print p[2:5] #this will print the letter after 2nd position till 5th position
print p[1:7] 
print p[3:6]

print p[:3] #this will print the starting letter till 3
print p[3:] #this will print the letter after 3rd till end

#string concatination using +
print t+p

print t+' '+p

#string repeating
print t*2

