from random import randrange

class myColors :
            
	ResetAll = "\033[0m"
        
	LightRed     = "\033[91m"
	LightGreen   = "\033[92m"
	LightYellow  = "\033[93m"
	LightBlue    = "\033[94m"
	LightMagenta = "\033[95m"
	LightCyan    = "\033[96m"

nameList = ["Liam","Olivia","Noah","Emma","liver","Charlott","Amelia","James","Ava","Jack","Luna","Ilyada",
"William","Sophia","Benjamin","Isabella","Lucas","Mia","Henry","Evelyn","Theodore","Harper","Tanner","Levi",
"Camila","Alexander","Gianna","Jackson","Elizabeth","Mateo","Eleanor","Daniel","Ella","Michael","Abigail","Mason",
"Sofia","Sebastian","Avery","Ethan","Scarlett","Logan","Emily","Owen","Aria","Samuel","Penelope","Jacob","Chloe",
"Luke","Asher","Layla","Aiden","Mila","John","Nora","Joseph","Hazel","Madison","David","Ellie","Leo","Lily","Nova",
"Julian","Isla","Hudson","Grace","Grayson","Violet","Matthew","Aurora","Ezra","Riley","Gabriel","Zoey","Carter",
"Isaac","Emilia","Jayden","Stella","Lucaz","Zoe","Anthony","Victoria","Dylan","Hannah","Lincoln","Addison",
"Thomas","Leah","Maverick","Lucy","Elias","Eliana","Charles","Everly","Christopher","Elena","Natalie","Ciri"]

surnameList = ["Brown","Jones","Miller","Davis","Garcia","Rodriguez","Wilson","Martinez","Anderson","Taylor","Thomas",
"Hernandez","Moore","Martin","Jackson","Thompson","White","Lopez","Gonzalez","Harris","Clark","Lewis","Robinson",
"Walker","Perez","Hall","Young","Allen","Sanchez","Wright","King","Scott","Green","Baker","Adams","Nelson","Hill",
"Campbell","Mitchell","Roberts","Carter","Phillips","Evans","Turner","Torres","Parker","Collins","Edwards","Stewart",
"Morris","Murphy","Rivera","Cook","Rogers","Morgan","Peterson","Cooper","Reed","Bailey","Bell","Gomez","Kelly","Lee",
"Howard","Ward","Cox","Diaz","Wood","Watson","Brooks","Bennett","Gray","James","Reyes","Cruz","Hughes","Flores",
"Myers","Long","Foster","Sanders","Ross","Morales","Powell","Sullivan","Russell","Jenkins","Gutierrez","Perry",
"Barnes","Fisher","Henderson","Coleman","Patterson","Jordan","Reynolds","Hamilton","Graham","Kim","Butler","Price"]

foodList = ["Bacon, Sausage, with Egg Wrap","Bacon, Egg, with Gouda Sandwich","Impossible breakfast sandwich","Avocado spread",
"Double-smoked bacon, egg, with cheddar sandwich","Egg with Sausage cheddar sandwich","Spinach, Egg white, with Feta wrap",
"Turkey Bacon Cheddar with Egg white sandwich","Ham with Swiss Croissant Bun","Egg white with Roasted Red Pepper egg bites",
"Bacon with Gruyere egg bites","Chicken with Bacon","Chicken wrap protein box","Turkey Provolone with Pesto on Ciabatta",
"Tomato with Mozzarella","Grilled Cheese","Eggs with cheese","Cheddar with Uncured Salami","Plain Bagel","Hippeas White cheddar",
"Chickpea Bites with Avocado","Everything & Cheddar Bagel","Cinnamon Raisin bagel","Pumpkin with Pepita loaf",
"Sprouted grain vegan bagel","Chocolate cake pop","Birthday cake pop","Cinnamon coffee cake","Banana, walnut, with pecan loaf",
"Iced lemon loaf","Ham & Swiss Croissant","Chocolate croissant","Almond croissant","Blueberry Muffin","Unicorn cake pop",
"Double Chocolate brownie","Marshmallow dream bar","Chocolate chip cookie","Butter croissant","Blueberry Scone",
"Petite Vanilla Bean Scone","Berry Trip Parfait","Rolled with Steel-cut oatmeal","Peter Rabbit organics apple with grape",
"Peter Rabbit Organics strawberry banana","Glazed doughnut","Cheese Danish","Salt with Vinegar kettle potato chips",
"Squirrel brand classic almonds","Sweet Potato Kettle potato chips","Simply salted kettle potato chips",]

drinkList = ["Caffè Mocha","Pumpkin Cream Cold Brew","Pumpkin Spice Latte","Peppermint Mocha","Iced Brown Sugar Oatmilk Shaken Espresso",
"Irish Cream Cold Brew","Caffè Latte","Hot Chocolate","Chai Tea Latte","Iced Green Tea Lemonade","Apple Crisp Oatmilk Macchiato",
"Cinnamon Dolce Latte","Matcha Tea Latte","Toasted White Chocolate Mocha","Dragon Drink Starbucks Refreshers Beverage","Paradise Drink",
"Iced Chocolate Almondmilk Shaken Espresso","Flat White","Nitro Cold Brew","Vanilla Sweet Cream Nitro Cold Brew","Blonde Roast","The Max"
"Vanilla Sweet Cream Cold Brew","Honey Almondmilk Flat White","Chestnut Praline Latte","Medium Roast—Pike Place Roast","Dark Roast Coffee",
"Caffè Americano","White Chocolate Mocha","Caramel Brulée Latte","Cappuccino","Royal English Breakfast Tea","Cold Brew","Caramel Macchiato",
"Caramel Ribbon Crunch Frappuccino","Mocha Cookie Crumble Frappuccino","Chocolate Cream Cold Brew","Vanilla Bean Crème Frappuccino",
"Iced Starbucks Blonde Vanilla Latte","Strawberry Crème Frappuccino","Iced Sugar Cookie Almondmilk Latte","Java Chip Frappuccino",
"Caramel Brulée Frappuccino","Biscotti Frappuccino","Pink Drink","Apple Pie Frappuccino","Caramel Snickerdoodle Macchiato",
"Twix Frappuccino","Very Berry Lemonade","Dragonfruit Shortcake Frappuccino","White Chocolate Strawberry Iced Latte","Apple-Kiwi Refresher"]

customerList = []

class Human:
  def __init__(p, name, food, drink, second, price, table):
    p.name = name
    p.food = food
    p.drink = drink
    p.second = second
    p.price = price
    p.table = table
  
  def __str__(p):
    return f"{myColors.LightMagenta}Name ={myColors.ResetAll} {p.name} \n {myColors.LightMagenta}Food ={myColors.ResetAll} {p.food} And {p.drink} \n {myColors.LightMagenta}Time Spend ={myColors.ResetAll} {p.second}min \n {myColors.LightMagenta}Amount Paid ={myColors.ResetAll} {p.price}$ \n {myColors.LightMagenta}Table Number ={myColors.ResetAll} {p.table}"  

earnMoney = 0
costMoney = 0
totalMoney = 0

print("\n{:{align}{width}}\n".format(f'{myColors.LightBlue}MyCakeStore{myColors.ResetAll}', align='^', width='120'))

try:
    customer = input(f"{myColors.LightGreen}Daily Customer Count: {myColors.ResetAll}")
    customer = int(customer)
    
    if customer > 4000:
       print(f"{myColors.LightRed}We can't fit that many people in the shop Max Value.{myColors.ResetAll} This shop can accommodate a {myColors.LightYellow}maximum of 4000 people per day{myColors.ResetAll}")
       customer = 4000
except ValueError:
    print(f"{myColors.LightRed}This is not a number!{myColors.ResetAll} but don't worry, our daily average {myColors.LightMagenta}number of customers is 160, {myColors.LightGreen}I accept this value.{myColors.ResetAll}")
    customer = 160

for nb in range(customer):
  nub = globals()['num%s' % nb] = randrange(100)
  earnMoney += round(nub/1.8, 2) 
  costMoney += round(nub/4.7, 2) 
  cstm = globals()['p%s' % nb] = Human(nameList[nub] + " " + surnameList[nub], foodList[round(nub/2)], drinkList[round(nub/2)], 
  nub, round(nub/1.8, 2), round(nub/5))
  customerList.append(cstm)

spcust = randrange(customer)

totalMoney += earnMoney - costMoney 
totalMoney -= 1241.33 * customer/100
totalMoney = round(totalMoney, 2)

print(f"{myColors.LightYellow}Today's Special Customer is:\n{myColors.ResetAll}",customerList[spcust])

print(f"{myColors.LightCyan}Total Money:{myColors.ResetAll}", totalMoney, f"{myColors.LightGreen}${myColors.ResetAll}")
