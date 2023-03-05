#Project Done By Saif Battah 1170986
from WareHouse import *
import datetime
from SuperMarket import *
from datetime import date
import weakref
import gc
#=======================================================================================================================
ItemsDict = {}
SuperMarketDict = {}
#Items_In_SuperMarket = {}
#=======================================================================================================================
print("1. Add product items to the warehouse\n"
      "2. Add a new supermarket to the management system\n"
      "3. List of items in the warehouse based on expiry date\n"
      "4. Clear an item from the warehouse\n"
      "5. Distribute products from the warehouse to a supermarket\n"
      "6. Generate a report about the sales status of the warehouse\n"
      "7. Exit")
choice = input("---------------------\nPlease Select Choice: ")
#=======================================================================================================================
def add_product(itc,itn,ited,itwyc,itsuc,itq): #add new product to warehouse class as an object
    if itc in ItemsDict:
        print("Item Already Exists!")
        sel = input("Want to Update Quantity?(Y/any botton to close): ")
        if (sel == 'Y'): # if the item code already exists in the warehouse
            if(ItemsDict[itc].Name == itn and ItemsDict[itc].Exp_Date == ited and ItemsDict[itc].WUCost == itwyc and
                    ItemsDict[itc].SUCost == itsuc): #if matching all properties between old and new then
                # only update quantity
                print("Update Quantity.....")
                old_q = int(ItemsDict[itc].Quantity) #old quantity
                new_q = int(itq) #new quantity
                updated_q = old_q + new_q # total quantity
                ItemsDict[itc].Quantity = updated_q # assign new quantity to the object
                #re-write into the file with all updates
                f = open("warehouse_items.txt", "w")
                f.write("")
                f.close()
                f = open("warehouse_items.txt", "a")
                for i in ItemsDict:
                    f.write(str(ItemsDict[i].Code) + ";" + str(ItemsDict[i].Name) + ";" + str(ItemsDict[i].Exp_Date) +
                            ";" + str(ItemsDict[i].WUCost) + ";" + str(ItemsDict[i].SUCost) +
                            ";" + str(ItemsDict[i].Quantity) + '\n')
                f.close()

            else:
                #if the information between the 2 quantites of the same code are not the same, then error occurs
                print("Unmatched Information between the Items\n"
                      "Please re-Enter product Information with different Code Number")
        else:
            #if you don't want to update!
            print("ok...")
    else:
        #new product added!
        wareh = WareHouse(itc,itn,ited,itwyc,itsuc,itq)
        ItemsDict[itc] = wareh
        f = open("warehouse_items.txt", "a")
        f.write(str(itc)+";"+itn+";"+ited+";"+str(itwyc)+";"+str(itsuc)+
                ";"+str(itq)+'\n') #write on file
        f.close()
#-----------------------------------------------------------------------------------------------------------------------
def add_supermarket(sn,sc,sa,sd):#add new supermarket to supermarket class as an object
    if sn in SuperMarketDict:
        print("Super Market Already Exists!")
    else:
        sm = SuperMarket(sn,sc,sa,sd)
        SuperMarketDict[sn] = sm
#-----------------------------------------------------------------------------------------------------------------------
def search_in_wh(code,quantity):#
    exists = 0
    for i in ItemsDict:
        if(int(code) == int(ItemsDict[i].Code)):
            exists = 1
            if (int(ItemsDict[i].Quantity) == 0): # out of stock
                print("no remaining items of this product, code:",code, "of quantity: ",quantity,"in the ware house!")
            elif(int(quantity) <= int(ItemsDict[i].Quantity)): # if offered is less than exist
                print(quantity," Offered Successfully!")
                remaining = int(ItemsDict[i].Quantity) - int(quantity)
                ItemsDict[i].Quantity = remaining
                print(ItemsDict[i].Name,"'s Remaining in WareHouse = ",ItemsDict[i].Quantity)
            elif(int(quantity) > int(ItemsDict[i].Quantity)):# if offered is more than exist
                print("Only offered ",ItemsDict[i].Quantity, "From ",quantity)
                ItemsDict[i].Quantity = 0
                print(ItemsDict[i].Name,"'s Remaining in WareHouse = ", ItemsDict[i].Quantity)

    if(exists == 0):
        print("item:",code,"with requested amount of:",quantity," not in the ware house!")
#=======================================================================================================================
while ( choice != '7' ):
    valid_ic = False
    valid_ied = False
    valid_iw = False
    valid_is = False
    valid_iq = False
    valid_sc = False
    valid_sa = False
    valid_sd = False
    valid_sortdate = False
#=======================================================================================================================
    if choice == '1':
        print("Adding Product Item to the Ware House\n---------------------------------------")
        #these while,try catch commands are used to handle user input error
        while not valid_ic:
            try:
                item_code = int(input("Item Code: "))
                valid_ic = True
            except ValueError:
                print("Please Enter Correct item Code")

        item_name = input("Item Name: ")

        print("Expiry Date")
        while not valid_ied:
            try:
                year = int(input('Enter Exp year: '))
                month = int(input('Enter Exp month: '))
                day = int(input('Enter Exp day: '))
                try:
                    a_date = datetime.date(year, month, day) # convert to date data type
                    item_Expiry_Date = str(day)+"/"+str(month)+"/"+str(year)
                    valid_ied = True
                except ValueError as e:
                    print("Wrong Date Input, Please Enter a Correct Date Again")
            except ValueError as e:
                print("Wrong Date Input, Please Enter a Correct Date Again")

        while not valid_iw:
            try:
                item_WUCost = input("Wholesale Unit Cost: ")
                valid_iw = True
            except ValueError:
                print("Please Enter Correct Cost")

        while not valid_is:
            try:
                item_SUCost = input("Sales Unit Cost: ")
                valid_is = True
            except ValueError:
                print("Please Enter Correct Cost")

        while not valid_iq:
            try:
                item_Quantity = input("Quantity: ")
                valid_iq = True
            except ValueError:
                print("Please Enter Correct Quantity")

        add_product(item_code,item_name,item_Expiry_Date,item_WUCost,item_SUCost,item_Quantity)
#=======================================================================================================================
    elif choice == '2':
        print("Adding New Super Market\n------------------------")

        sm_Name = input("Super Market Name: ")

        while not valid_sc:
            try:
                sm_Code = int(input("Super Market Code: "))
                valid_sc = True
            except ValueError:
                print("Please Enter Correct Code")

        sm_Address = input("Super Market Address: ")

        today = date.today()
        sm_Added_Date = today.strftime("%d/%m/%Y")
        print("Date Added Automatically")

        add_supermarket(sm_Name, sm_Code, sm_Address, sm_Added_Date)


#        f = open("sm.txt", "a")
#        f.write(str(sm_Name) + ";" + str(sm_Code) + ";" + str(sm_Address) + ";" + str(sm_Added_Date) + '\n')
#        f.close()
#=======================================================================================================================
    elif choice == '3':
        #initialize variables
        wholesalecost = int(0)
        salescost = int(0)
        print("Enter Expiry Date")
        while not valid_sortdate:
            try:
                year_3 = int(input('Enter Exp year: '))
                month_3 = int(input('Enter Exp month: '))
                day_3 = int(input('Enter Exp day: '))
                try:
                    b_date = date(year_3, month_3, day_3) # convert to date data type
                    sort_Expiry_Date = str(day_3) + "/" + str(month_3) + "/" + str(year_3)
                    valid_sortdate = True
                except ValueError as e:
                    print("Wrong Date Input, Please Enter a Correct Date Again")
            except ValueError as e:
                print("Wrong Date Input, Please Enter a Correct Date Again")
        print(sort_Expiry_Date)
        for i in ItemsDict:
            cur_d = ItemsDict[i].Exp_Date # fetvh date
            #split date by / to re arrange them in date data type again
            d_split = cur_d.split("/")
            day_d = int(d_split[0])
            month_d = int(d_split[1])
            year_d = int(d_split[2])
            try:
                c_date = date(year_d, month_d, day_d) #c_date is the fetched date from object
                # and b_date is the user input date
                if(c_date < b_date):
                    print("Code:", ItemsDict[i].Code,"| Name:", ItemsDict[i].Name,"| Expiry Date:",
                          ItemsDict[i].Exp_Date,"| Wholesale Unit Cost:", ItemsDict[i].WUCost,"| Sales Unit Cost:",
                          ItemsDict[i].SUCost, "| Quantity:", ItemsDict[i].Quantity)
                    wholesalecost+= int(ItemsDict[i].WUCost)
                    salescost+= int(ItemsDict[i].SUCost)
            except ValueError as e:
                print("Wrong Date Input, Please Enter a Correct Date Again")
        if (wholesalecost != 0):
            print("Total WholeSale Cost: ",wholesalecost,"\nTotal Sales Cost: ",salescost)

#=======================================================================================================================
    elif choice == '4':
        #Clear an item from the warehouse
        checker = 0
        i_Code = input("Input The Code of an item: ")
        for i in ItemsDict:
            if(int(i_Code) == int(ItemsDict[i].Code)):
                checker = 1
                #before delete
                print("Code:", ItemsDict[i].Code, "| Name:", ItemsDict[i].Name, "| Expiry Date:",
                      ItemsDict[i].Exp_Date, "| Wholesale Unit Cost:", ItemsDict[i].WUCost, "| Sales Unit Cost:",
                      ItemsDict[i].SUCost, "| Quantity:", ItemsDict[i].Quantity)
                q_tbc = input("Enter The Quantity That Needs to be Cleared: ")
                #check if the quantity is available to be removed or not
                if(int(q_tbc) <= int(ItemsDict[i].Quantity)):
                    result = int(ItemsDict[i].Quantity) - int(q_tbc)
                    ItemsDict[i].Quantity = result
                    #after delete
                    print("Code:", ItemsDict[i].Code, "| Name:", ItemsDict[i].Name, "| Expiry Date:",
                          ItemsDict[i].Exp_Date, "| Wholesale Unit Cost:", ItemsDict[i].WUCost, "| Sales Unit Cost:",
                          ItemsDict[i].SUCost, "| Quantity:", ItemsDict[i].Quantity)

                else:
                    print("Out of Quantity Range!")
        if(checker == 0):
            print("Item Not In The Ware House!")

#=======================================================================================================================
    elif choice == '5':
        checker_1 = 0 #to check if super market exists or not, set 1 if found,else: keep on zero
        ism_Code = input("Enter The Code Of The SuperMarket: ")
        for i in SuperMarketDict:
            if(int(ism_Code) == int(SuperMarketDict[i].Code)): #matching codes
                checker_1 = 1
                f_name = "DistributeItems_" + ism_Code +".txt" # set the name of file to open
                fsm = open(f_name, "r")
                fsm_Lines =fsm.readlines()
                for fsm_line in fsm_Lines:
                    current_fsm_line = fsm_line.strip()
                    fsm_line_split = current_fsm_line.split(";")
                    search_in_wh(fsm_line_split[0],fsm_line_split[1]) #function that search and detuct from warehouse
                fsm.close()
        if(checker_1 == 0):
            print("SuperMarket Not in the list!")
#=======================================================================================================================
    elif choice == '6':
        #initialize variables
        total_items = 0
        individual_profit = 0
        total_wholesale_cost = 0
        total_sales_cost = 0
        total_profit = 0
        #everything is described by its name
        for j in ItemsDict:
            total_items = int(total_items) + int(ItemsDict[j].Quantity)
            total_wholesale_cost = int(total_wholesale_cost) + (int(ItemsDict[j].WUCost) * int(ItemsDict[j].Quantity))
            total_sales_cost = int(total_sales_cost) + (int(ItemsDict[j].SUCost) * int(ItemsDict[j].Quantity))
            individual_profit = int(ItemsDict[j].SUCost) - int(ItemsDict[j].WUCost)
            total_profit = int(total_profit) + ( int(individual_profit) * int(ItemsDict[j].Quantity) )
        print("Number of items in the warehouse:",int(total_items))
        print("Total wholesale cost of all items in the warehouse:",int(total_wholesale_cost))
        print("Total sales cost of all items in the warehouse:",int(total_sales_cost))
        print("Expected profit after selling all items in the warehouse:",int(total_profit))
#=======================================================================================================================
    else:
        print("Please choose correct answer")
#=======================================================================================================================
    print(
        "---------------------\n1. Add product items to the warehouse\n"
        "2. Add a new supermarket to the management system\n"
        "3. List of items in the warehouse based on expiry date\n"
        "4. Clear an item from the warehouse\n"
        "5. Distribute products from the warehouse to a supermarket\n"
        "6. Generate a report about the sales status of the warehouse\n"
        "7. Exit")
    choice = input("---------------------\nPlease Select Choice: ")
#=======================================================================================================================
if (choice == '7'):
    print("Bye Bye")
    exit()
#=======================================================================================================================