MENU = {
    'espresso': {
        'ingredients': {
            'water': 50,
            'coffee': 18,
        },
        'cost': 1.5,
    },
    'latte': {
        'ingredients': {
            'water': 200,
            'milk': 150,
            'coffee': 24,
        }, 
        'cost': 2.5,
    },
    'cappucino': {
        'ingredients': {
            'water': 250,
            'milk': 100,
            'coffee': 24,
        },
        'cost': 3.0,
    }
}

RESOURCES = {
    'water': 300,
    'milk': 200,
    'coffee': 100,
}

def reset_resources(drink):
    if 'milk' not in MENU[drink]['ingredients']:
        RESOURCES['water'] = RESOURCES['water'] - MENU[drink]['ingredients']['water']
        RESOURCES['coffee'] = RESOURCES['coffee'] - MENU[drink]['ingredients']['coffee']
    else: 
        RESOURCES['water'] = RESOURCES['water'] - MENU[drink]['ingredients']['water']
        RESOURCES['coffee'] = RESOURCES['coffee'] - MENU[drink]['ingredients']['coffee']
        RESOURCES['milk'] = RESOURCES['milk'] - MENU[drink]['ingredients']['milk']
    
def check_money(quarter, dime, nickle, pennie, drink):
    global money
    quarters = float(quarter) * 0.25
    dimes = float(dime) * 0.10
    nickles = float(nickle) * 0.05
    pennies = float(pennie) * 0.01
    current_money = quarters + dimes + nickles + pennies
    
    if (current_money < MENU[drink]['cost']):
        print("sorry that's not enough money. Money refunded.")
    else: 
        if (current_money > MENU[drink]['cost']):
            change = current_money - MENU[drink]['cost']
            money += MENU[drink]['cost']
            print(f"Here is ${change:.2f} dollars in change")
            
        print(f"here is you {drink}☕. enjoy!")
        reset_resources(drink)
        
def check_resource(drink):
    if 'milk' not in MENU[drink]['ingredients']:
        if (RESOURCES['coffee'] < MENU[drink]['ingredients']['coffee']):
            print('sorry, there is not enough coffee')
        else: 
            if (RESOURCES['water'] < MENU[drink]['ingredients']['water']):
                print('sorry there is not enough water')
            else:
                quarter = input("Insert your quarter:")
                dime = input("Insert your dime:")
                nickle = input("Insert your nickle:")
                pennie = input("Insert your pennie:")
                check_money(quarter, dime, nickle, pennie, drink)
    else:
        if (RESOURCES['coffee'] < MENU[drink]['ingredients']['coffee']):
            print('sorry, there is not enough coffee')
        else: 
            if (RESOURCES['milk'] < MENU[drink]['ingredients']['milk']):
                print('sorry there is not enough milk')
            else:
                if (RESOURCES['water'] < MENU[drink]['ingredients']['water']):
                    print('sorry there is not enough water')
                else:
                    quarter = input("Insert your quarter: ")
                    dime = input("Insert your dime: ")
                    nickle = input("Insert your nickle: ")
                    pennie = input("Insert your pennie: ")
                    check_money(quarter, dime, nickle, pennie, drink)

money = 0
quarters = 0
dimes = 0
nickles = 0
pennies = 0 

while True:
    user_drink = input('what would you like? (cappucino/espresso/latte)').lower()  
    if (user_drink) == "off":
        print("Okey bye....")
        break
    elif (user_drink == "report"):
        print(f"""
        water   : {RESOURCES["water"]}
        milk    : {RESOURCES['milk']}
        coffee  : {RESOURCES['coffee']}
        money   : {money:.2f}
    """)
    else: 
        check_resource(user_drink)
    