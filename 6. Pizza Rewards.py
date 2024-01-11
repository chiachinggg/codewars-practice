'''
In an attempt to boost sales, the manager of the pizzeria you work at has devised a pizza rewards system: if you already made at least 5 orders of at least 20 dollars, you get a free 12 inch pizza with 3 toppings of your choice.

However, the rewards system may change in the future. Your manager wants you to implement a function that, given a dictionary of customers, a minimum number of orders and a minimum order value, returns a set of the customers who are eligible for a reward.

Customers in the dictionary are represented as:

{ 'customerName' : [list_of_order_values_as_integers] }
See example test case for more details.
'''                     
        
#after modularization

def pizza_rewards(customers, min_orders, min_price):
    yahoo = set()
    counter = 0
    def price_check(order):
        counter+=1
        return order >= min_price
        
    def order_check(counter):
        return counter >= min_orders
        
    for customer in customers:
        for order in customers[customer]:
            if price_check(order):
        if order_check(counter):
            yahoo.add(customer)
    return yahoo
    #customer.items()


#initial solution
def pizza_rewards(customers, min_orders, min_price):
    yahoo = set()
    for index, customer in enumerate(customers):
        counter = 0
        for order in customers[customer]:
            if order >= min_price:
                counter +=1
        if counter>=min_orders:
            yahoo.add(customer)
    return yahoo
