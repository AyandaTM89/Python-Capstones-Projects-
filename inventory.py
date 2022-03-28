#importing modules
from tabulate import tabulate
print("\t\n CAPSTONE PROJECT IV \n")

# defining the local  variables
inventory = ""
country = ""
code = ""
product = ""
cost = 0
table = []
quantity = 0

#initialising the Shoes class
class Shoes:
    #constructor with the attributes
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
        self.value = cost * quantity

    # get a country product
    def getCountry(self):
        return self.country

    # get a code of the product
    def getCode(self):
        return self.code

    # get the product name
    def getProduct(self):
        return self.product

    # get the quantity of the product
    def getQuantity(self):
        return self.quantity

    # get the cost of the product
    def getCost(self):
        return self.cost

    # get the value of the product
    def getValue(self):
        return self.value

    # setting the vlue of the lowest quantity
    def set_quantity(self,value):
        self.quantity = value

    # get all the attributes of the class
    def getAll(self):
        return f" {self.country} {self.code} {self.product} {self.quantity} "

    # defining the value per item value
def value_per_item(Shoe_list):
    # tabulate 
    table = [["country", "code", "product", "cost", "quantity", "value"]]
    for obj in Shoe_list:
        table.append([obj.getCountry(), obj.getCode(), obj.getProduct(), obj.getCost(), obj.getQuantity(), obj.getValue()])
    print(tabulate(table))
    print("========================================================================\n")

    # defining read data funtion to read data from inventory text file
def read_data():

    #try catch block for error handling
    try:
        with open("inventory.txt", "r") as file:
            content = file.readlines()
            for line in content:
                print(line)

     # except block error handling
    except FileNotFoundError:
            print("Wrong file name or missing file")

 # get a lowest quantity from the product list
def get_lowest(Shoe_list):
    low_velue = Shoe_list[0]
    for low in Shoe_list:
        if low.getQuantity() < low_velue.getQuantity():
            low_value = low
    return low_value

# get a highest value of the product
def get_high(Shoe_list):
    high_value = Shoe_list[0]
    for high in Shoe_list:
        if high.getQuantity() > high.getQuantity():
            high_value = high
    print(high_value.getAll(), "\n Can be Sold")

# adding a quantity of lowest product to the text file
def list_to_file(Shoe_list):
    with open("inventory.txt", "r+") as file:
        for shoe_list_object in Shoe_list:
            file.write(shoe_list_object.getAll())
            file.write("\n")

#shoe object with the list of products in inventory file
Shoe_list =[]
shoe  = Shoes("South Africa", "SKU44386","Air Max 90", 2300, 20) 
Shoe_list.append(shoe)

shoe1 =Shoes("China","SKU90000","Jordan 1",3200,50)     
Shoe_list.append(shoe1)

shoe2  = Shoes("United States","SKU29077","Cortez",970,60) 
Shoe_list.append(shoe2)

shoe3  = Shoes("Russia","SKU89999","Air Force 1",2000,43) 
Shoe_list.append(shoe3)

shoe4  = Shoes("Egypt","SKU19888","Dunk SB",1500,26) 
Shoe_list.append(shoe4)

shoe5  = Shoes("Columbia","SKU87500","Air Huarache",2683,8)
Shoe_list.append(shoe5)

shoe6 = Shoes("Vietnam","SKU63221","Blazer",1700,19) 
Shoe_list.append(shoe6)

while True:
    # menu to select option .on what the user whant to do
    menu = input(" What would you like to do : \n ● read data \n ● search \n ● table \n ● quit \n>>:").lower()

    # if user selects search .they will have to choose between searching code
    # and checking the stock quantity
    if menu == "search":
        objects = input("\n CHOOSE OPTIONS >>\n ● code \n ● quantity \n>>: ").lower()
        if objects == "code":
            print("\t\t________Product Code_______\n")
            search = input("\n\n Please enter Product Code: ")
            for shoes in Shoe_list:
                if shoes.getCode() == search:
                    print(shoes.getAll())
                    print("========================================================================\n")

        # if the user selects the quantity they choese between lowest and highest quantity
        elif objects == "quantity":
            quantity = input("\n Quantity to check >> \n ● Lowest \n ● Highest \n >>: ")
            print("\t\t ___________Quantity Checker_____________\n")
            
            # if lowest quantity options selected
            if quantity == "Lowest":
                print("===========================Lowest Quantity=============================================")
                lowest = get_lowest(Shoe_list)
                print(lowest.getAll())
                print("========================================================================")
                
                # lowest stock...a user can opt to re-order or exit 
                order = input('Wants to order stock(yes/no)? ')

                #if the user selects yes.they will have to order the stock
                if order in 'yes':
                    mini = int(input("Enter new product quantity : "))
                    lowest.set_quantity(mini + lowest.getQuantity())
                    list_to_file(Shoe_list)
                    print("Product ordered \n")
                    print(lowest.getAll())
                    print("========================================================================\n")

                 # if user choese no to re-order stock .program will exit   
                elif order in "no":
                    print("good bye", quit)
                    
                # highest quantity option selected
            elif quantity == "Highest":
                print("===========================Highest Quantity=============================================")
                get_high(Shoe_list)
                print("========================================================================\n")

            else:
                break

    # calling on viewing table function    
    elif menu == "table":
        menu == True
        print(value_per_item(Shoe_list))

        # calling on read data function
    elif menu == "read data":
        menu == True
        print(read_data())   
    
            # quit for exiting on options    
    elif menu == "quit":
        print('Goodbye!!!')
        exit()
    else:
            print("You have made a wrong choice, Please Try again")