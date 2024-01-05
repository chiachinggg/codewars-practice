'''
In an attempt to boost sales, the manager of the pizzeria you work at has devised a pizza rewards system: if you already made at least 5 orders of at least 20 dollars, you get a free 12 inch pizza with 3 toppings of your choice.

However, the rewards system may change in the future. Your manager wants you to implement a function that, given a dictionary of customers, a minimum number of orders and a minimum order value, returns a set of the customers who are eligible for a reward.

Customers in the dictionary are represented as:

{ 'customerName' : [list_of_order_values_as_integers] }
See example test case for more details.
'''                     

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
