class NumberPower:
    def __init__(self,maxi_num):
        self.maxi_num = maxi_num

#createing the interator object
    def __iter__(self):
        self.n = 0
        return self
    
# Iterate over the created object and generate one value each time    
    def __next__(self):
        if(self.n <= self.maxi_num):
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration

#iterating using a for loop
     
for i in NumberPower(10):
    print(i)