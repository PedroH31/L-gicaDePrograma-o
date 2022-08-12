"""

#It’s...not really an adventure game...#Ver 1.0
#Your village is being attacked by 'a germanic tribe' and you need to run to the stores and get the right things to save
your village, and probably some good looking girl or boy you want to marry. All prices in gold pieces excl. VAT...
chop chop!! ze germanz are coming!
#The code should allow you to get 1 thing from each store and each item you get should be removed from the store
inventory, then do same for next store...
# one way to buy by typing the key 'newt' in an input box...or something
# at end you should print the 'items' you have taken..in this version you don't have to pay for stuff or add it up
#ver 1.2 add ability to exit a store without buying and go to next by typing 'exit', and to exit if a nonexistant item
is bought(typed)
#Add purse with 1000 gold pieces and payment for the items during or at end of code and show a message about total cost
and how much gold you have left
#ver 1.4 random bug fix, ' browser compatability', refactoring code...
basically being lazy ..stop scrolling TikTok/Facebook! ;-)
#Ver 1.5 print inventory before and after purchases as one department_store of stuff(combine inventories from all stores
 into one...pretend Big Biz bought all the local stores, and want constant reporting for inventory management...)
# as in all games there is a special way to do this that actually makes money and solves the problem...
can you find 'them'? Do you know why? May require knowledge of actual python 'lore'
"""

freelancers = {'name': 'freelancing Shop', 'brian': 70, 'black knight': 20, 'biccus diccus': 100, 'grim reaper': 500,
               'minstrel': -15}
antiques = {'name':'Antique Shop','french castle':400, 'wooden grail':3, 'scythe':150, 'catapult':75, 'german joke':5}
pet_shop = {'name':'Pet Shop','blue parrot':10, 'white rabbit':5, 'newt': 2}
purse = 1000
cart = {}
items_and_values = ''
department_store = {}

for department in (freelancers, antiques, pet_shop) :department_store.update(department)
department_store.pop('name')
print(f'morning stock', sorted(department_store.items()))
print()

for shop in (freelancers, antiques, pet_shop):
    shop.pop('name')
    buy_item = input(f'Welcome to {shop.get("name")}! (type exit to exit store) what do you want to buy: {shop}: ').lower()
    if buy_item == 'exit':
        print('You left the store.')
        continue
    elif buy_item not in shop:
        print('You left the store.')
        continue
    items_and_values = items_and_values + f'{buy_item}:{shop[buy_item]} Gp, '
    cart.update({buy_item: shop.pop(buy_item)})
    items_bought = ", ".join(cart.keys())
total_cost = sum(cart.values())
purse -= total_cost
print(f'You purchased {items_and_values}, the total cost is {total_cost},You have {purse} gold left!.')

print(f'evening stock:', sorted(department_store.items()))






