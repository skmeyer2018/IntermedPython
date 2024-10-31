#Stephen Kleimeyer
#List Comprehension Exercise 1
print("THIS PROGRAM COVERTS A LIST OF ONES AND ZEROES TO ONS AND OFFS RESPECTIVELY.")
print("THE LIST OF BITS:")
binary = [1,1,0,1,0,0,1,1,0,1,0,1,0,1]
print(binary)
on_off=["on" if b == 1 else "off" for b in binary]
print("BECOMES:")
print(on_off)
