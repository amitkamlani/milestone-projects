#Assumptions of the mortgage calculator:
#The calculator assumes that all mortagages are fixed rate mortages, since there is no access to data regarding future dates, especially if they are indexed.

def string_to_float(string): #A FUNCTION TO CONVERT A PERCENTAGE INPUT TO A DECIMAL
    '''
    A FUNCTION TO CONVERT A PERCENTAGE INPUT TO A DECIMAL
    
    '''
    if '%' not in string:
        return "ERROR: Please enter a valid %.  Make sure to use the % symbol"
    
    else:
        float_100 = float(string.strip('%')) #STRIPS THE '%'FROM THE STRING AND CHANGES DATA TYPE TO FLOAT
        float_ = float_100 / 100 #DIVIDES BY 100 TO GET THE FLOAT
    
        output = round(float_,5) #RETURNS FLOAT TO 5 DECIMAL PLACES
        return output
    
class mortgage_loan(): 
    def __init__(self): #Instances of a mortgage_loan contain these characteristics
        
        while True:
        
            try: 
                self.property_value = int(input("What was the property value?"))
                #returns value of property
                 
            except:
                
                print("Please enter a valid input for property value") #If input is not an integer
                
                continue
            else:
                break
            
        while True: 
            
            try:
                x = input("What was your downpayment?  Enter in full or as a %") #downpayment - can be entered in full or as a %
                
                if "%" in x: 
                    
                    #if input is entered as a %
                    
                    float_value = string_to_float(x) #the string_to_float function changes it to a float
                    
                    self.down_payment = float_value * self.property_value
                    
                else: 
                    
                    #If it is not entered as a %, it looks to convert the string input to a float.
                    
                    self.down_payment = float(x)
            
            except:
                
                #If % is not inputted nor can it convert the string to a float (i.e if input is letters, or other structures)
                
                print("Please enter a valid input, enter the full amount or as a % of face value")
                
                #ERROR IS CAUGHT
                
                continue
            else:
                
                break
            
        self.mortgage = self.property_value - self.down_payment #Actual mortgage is value - loan
        
        
        while True:
            
            try:
                n = input("What is the interest rate? Enter as a decimal or percentage")
                
                if '%' in n:
                    
                    #FOLLOWS SAME PROCESS AS DOWN_PAYMENT
                    
                    float_rate = string_to_float(n)
                    
                    self.rate = float_rate
                
                else:
                    
                    float_rate = float(n)
                    
                    self.rate = float_rate/100
        
            except:
                
                print("please enter a valid input")
                
                continue 
                
            else:
                
                break
                
        while True:
            
            try:
                
                self.years = int(input("Please enter the number of years")) 
                
            except:
                
                print("Please enter a valid input")
                
                continue
            
            else:
                
                break
           
    
    
    def payment(self):
        
        n = input("How frequently will you make payments? Enter monthly, annual or semi-annual")
        
        if n[0].lower() == "m": #If payments are monthly
            periods = self.years*12 #number of periods is number of months of payment (years x 12)
            rate = self.rate/12 # monthly rate is annual rate divided by 12
            
        elif n[0].lower()  == "a": #If payments are yearly, everything stays the same
            periods = self.years
            rate = self.rate
            
        elif n[0].lower() == 's': #If payments are semi-annually, periods is twice years
            periods = self.years * 2
            rate = self.rate / 2 #rate is half of annual rate
        
        else: 
            print("Please enter a valid input")
            
        annuity_factor = (((1/rate)) - (1/(rate*((1+rate)**periods)))) #Calculates annuity factor 
        
        payment = self.mortgage / annuity_factor 
        
        return "Your {} mortgage payment will be {}".format(n,payment)
    
while True:
    
    
    print("Welcome to mortgage calculator.  Please enter the following information.\nYour Mortgage will then be calculated")
    
    mortgage = mortgage_loan() 
    
    print(mortgage.payment())
    
    recalculate = input("Would you like to calculate another payment? Yes or No")
    
    
    if recalculate[0].lower() == 'y':
        continue 
    else:
        break