import math

# Marketplace constraints
max_price = 5000000
min_price = 1
listing_tax = 0.025
sales_tax = 0.1

# Replace the number with the drachma spent on purchasing items
drachma_spent = 100000
# Replace the number with the amount of items to resell
resell_quantity = 24

def min_resell_price(spent, quantity):
    if(isinstance(quantity, int)):
        if(isinstance(spent, int)):
            if(spent < min_price):
                print('drachma_spent must be an integer greater than ' + str(min_price) + ' and less than ' + str(max_price) + '!')
            elif(spent > max_price):
                print('drachma_spent must be an integer greater than ' + str(min_price) + ' and less than ' + str(max_price) + '!')
            else:
                return(math.ceil((drachma_spent + 1) / (quantity - listing_tax - (quantity * sales_tax))))
    else:
        print('resell_quantity must be an integer greater than 0!')

result = min_resell_price(drachma_spent, resell_quantity)

if result:
    print('You have spent ' + str(f"{drachma_spent:,}") + ' drachma and would like to resell ' + str(f"{resell_quantity:,}") + ' items; your minimum profitable resale listing price is ' + str(f"{result:,}") + ' drachma.')
