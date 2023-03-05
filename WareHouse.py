#Project Done By Saif Battah 1170986
class WareHouse:
    itemCount = 0
    def __init__(self,Code,Name,Exp_Date,WUCost,SUCost,Quantity):
        self.Code = Code
        self.Name = Name
        self.Exp_Date = Exp_Date
        self.WUCost = WUCost
        self.SUCost = SUCost
        self.Quantity = Quantity
        WareHouse.itemCount += 1

    def get_Code(self):
        return self.__Code

    def get_Name(self):
        return self.__Name

    def get_Exp_Date(self):
        return self.__Exp_Date

    def get_WUCost(self):
        return self.__WUCost

    def get_SUCost(self):
        return self.__SUCost

    def get_Quantity(self):
        return self.__Quantity

    def set_Code(self,Code):
        self.__Code = Code

    def set_Name(self,Name):
        self.__Name = Name

    def set_Exp_Date(self,Exp_Date):
        self.__Exp_Date = Exp_Date

    def set_WUCode(self,WUCode):
        self.__WUCode = WUCode

    def set_SUCost(self,SUCost):
        self.__SUCost = SUCost

    def set_Quantity(self,Quantity):
        self.__Quantity = Quantity