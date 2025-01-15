from multiprocessing.managers import Value


class Store:
    def __init__(self):
        self.numberList = None

    def insert(self, value):
        if self.numberList is None:
            self.numberList = []
            self.numberList.append(value)
            print(f"{value} inserted successfully")
        else:
            for i in self.numberList:
                if i == value:
                    print(f"duplicate value so will not insert {value} Current list is {self.numberList}")
                if i != value:
                    self.numberList.append(value)
                    print(f"{value} inserted successfully")

    def remove(self, value):
        self.numberList.remove(value)

    def printList(self):
        print(self.numberList)

c1 = Store()
c1.insert(2)
c1.insert(5)
c1.insert(5)
c1.insert(5)
c1.insert(5)
c1.insert(5)
c1.insert(5)

c1.printList()
# c1.remove(5)
# c1.printList()