import math

max_price = 5000000
listing_tax = 0.025
profit_tax = 0.1
total_tax = listing_tax + profit_tax

# Replace the number with how much you bought an item for
drachma_spent = 1000000

# Return the minimum price you should sell at to make a profit of at least 1 drachma
def min_resell_price(spent):
    rule_text = 'drachma_spent must be an integer greater than 0 and less than or equal to ' + str(max_price)

    if(isinstance(spent, int)):
        if(spent <= max_price and spent > 0):
            return (math.ceil((spent + 1) / (1 - 1 * total_tax)))
        elif(spent > max_price):
            print (rule_text + ', provided value (' + str(spent) + ') exceeds the limit of ' + str(max_price) + '!')
        elif(spent < 1):
            print (rule_text + ', provided value ' + str(spent) + ')  is less than 1!')
    else:
        print (rule_text + ', provided value (' + str(spent) + ')  is not an integer!')

print(min_resell_price(drachma_spent))