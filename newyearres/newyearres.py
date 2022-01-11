class items:
    itemCount = 0
    def __init__(self, name, type):
        self.name = name
        self.type = type
        items.itemCount+=1
    
    def toy(self):
        return "{} is a toy. Added to item list".format(self.name)

    def furniture(self):
        return "{} is a furniture. Added to item list".format(self.name)

    def iCount(self):
        print("Total item count: {}".format(self.itemCount))

bl = items("ball", 'toy')
tb = items("table", 'furniture')

print(bl.toy())
print(tb.furniture())
print(bl.furniture())
print(items.iCount())