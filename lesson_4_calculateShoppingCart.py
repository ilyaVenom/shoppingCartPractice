# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 23:13:19 2023
@author: segal
"""
#practicing python again from Bro Code
# at 5 pm to 10 pm daily starting  
# clip 4 out of 106
# 3rd shopping cart
item = input("What item would you like to buy?: ")
price = float(input("What is the price?: "))
quantity = int(input("How many would you like?: "))

total = price * quantity

print(f"You have bought {quantity} x {item}/s")
print(f"Your total is: ${round(total, 2)}")