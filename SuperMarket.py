#Project Done By Saif Battah 1170986
class SuperMarket:
    def __init__(self,Name,Code,Address,Added_Date):
        self.Name = Name
        self.Code = Code
        self.Address = Address
        self.Added_Date = Added_Date

    def get_Name(self):
        return self.__Name

    def get_Code(self):
        return self.__Code

    def get_Address(self):
        return self.__Address

    def get_Added_Date(self):
        return self.__Added_Date

    def set_Name(self,Name):
        self.__Name = Name

    def set_Code(self,Code):
        self.__Code = Code

    def set_Address(self,Address):
        self.__Address = Address

    def set_Added_Date(self,Added_Date):
        self.__Added_Date = Added_Date