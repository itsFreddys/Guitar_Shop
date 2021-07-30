# project module for classes
import datetime

# Globals
today = datetime.datetime.now()
YEAR = 2021

product_list ={1:('Guitar', 199.99),
                   2:('Keyboard',149.99),
                   3:('Drums\t',299.99),
                   4:('Guitar strings',7.99),
                   5:('Guitar picks',4.99),
                   6:('Guitar Lessons',100),
                   7:('Piano Lessons',100),
                   8:('Drums Lessons',80),
                   9:('Maintance',100)
                   }

# function
def shopSpree():
    spree = input(str("\nDo you want to make another purchase? (Y for yes, N for no): "))
   
    if spree.upper() == 'Y':
        return 'Y'
    elif spree.upper() == 'N':
        print("Goodbye")
        return 'N'
    else:
        print("Invalid entry, try again.")
        shopSpree()

# Class
class Store: 
    def __init__(self, cost = 0, choice = 1):
        self.products = []      # this should be an int value
        self.cost = cost              # float value
        self.choice = choice
        self.select_here()
    
    
    def select_here(self):
        for i, j in product_list.items():                # prints our list for the user to see
            print(i,'.', j[0], ': \t\t${:.2f}'.format(j[1]))
        print('0. When you are finished selecting.')
        while self.choice >= 1 or self.choice <= 9:                                     # where it loops for user inputs
            self.choice = int(input('\nChoose the product: '))
            if (self.choice >= 1 and self.choice <= 9):
                self.products.append((product_list[self.choice][0], product_list[self.choice][1]))
                print('Added', product_list[self.choice][0], 'for $', product_list[self.choice][1])
            elif (self.choice == 0):
                break
            else:
                print("Invalid entry try again")
        self.delivery()
        
                
    def delivery(self):
        print("\nToday's date is {}, select a day after today's date.".format(today.strftime("%x")))
        month = int(input("Enter a month (in Numerical form) that is after {}: ".format(today.strftime("%B"))))
        day = int(input("Enter a day that is after {}/{}: ".format(today.strftime("%B"),today.strftime("%d"))))
        print("\nDelivery date has been set for {}/{}/{}.".format(month,day,YEAR))
        self.printReceipt()
  
  
    def printReceipt(self):
        
        print('Your total purchase: ')
        for v in self.products:
            print(v[0],"\t$ {:.2f}".format(v[1]))
            self.cost += v[1]
        print("Total cost of purchase: ${}".format(self.cost))
        
        
        
        
        
        


