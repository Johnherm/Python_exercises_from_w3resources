#Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn
a = int(input("Please enter a number\n"))
n1 = int("%i"%a)
n2 = int("%i%i"%(a,a))
n3 = int("%i%i%i"%(a,a,a))
value = n1+n2+n3
print(value)