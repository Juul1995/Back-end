# Do not modify these lines
__winc_id__ = '62311a1767294e058dc13c953e8690a4'
__human_name__ = 'casting'

# Add your code after this line
# Casting is when you convert a variable value from one type to another.
leek_price = 2
print('Leek is '+ str(leek_price) +' euro per kilo.')

Leek_order = 'leek 4'

order_number = int(Leek_order.find(" "))  

Sum_total = leek_price * order_number 
print(Sum_total)

Kilo_broccoli = 2.34 
order_broccoli = 'broccoli 1.6'
Sum_broccoli = round((float((order_broccoli[order_broccoli.find(" ") +1:]))* Kilo_broccoli),2)

print(str((order_broccoli[order_broccoli.find(" ")+1:]))+'kg broccoli costs '+str(Sum_broccoli)+ 'e')