import timeit
import random
# Lets get this Heap sort going

class getHeapy:
    def __init__(self):
        self.myListy = [0]
        self.HowbigAmI = 0 
        
        
    #lets make the finction to move the current value to the correct spot up the list
    
    def getMovingUp(self, x):
        
        while x // 2 > 0:     # // indicates the floor 
            if self.myListy[x] < self.myListy[x//2]:        # we can check if the parameter x is less than its parent
                forNow = self.myListy[x//2]                 # this is where we swap the spots in the list depending on size 
                self.myListy[x//2] = self.myListy[x]
                self.myListy[x] = forNow
                
            x = x // 2
            
    def getInThere(self, value):
        self.myListy.append(value)
        #make sure to add 1 to the size of the list or else our algorithm to find parent / child will be corrupt
        self.HowbigAmI = self.HowbigAmI + 1
        self.getMovingUp(self.HowbigAmI)
        
        
    # Now we need to delete min but first we have to write the code that willm ove the value down the tree (List)
    
    def getDown(self, value):
        while (value * 2) <= self.HowbigAmI:
            babyValue = self.smallestChild(value)
            
            if self.myListy[value] > self.myListy[babyValue]:
                temp = self.myListy[value]
                self.myListy[value] = self.myListy[babyValue]
                self.myListy[babyValue] = temp
                
            value = babyValue
            
            # this is where we check the left and the right children using the valu * 2 + 1 
    def smallestChild(self, val):
        if val * 2 +1 > self.HowbigAmI:
            return val * 2 
            
        else:
            if self.myListy[val*2] < self.myListy[val*2+1]:
                return val * 2
            else:
                return val * 2 + 1
            
            
        # Delete Min will take the top node which should currently be the smallest pop it off then move the bottom most child to the root
        # and then the new root will be checked by the getDown() function to recreate a binary heap 
        
    def delMin(self):
        #taking the top node or spot in the list
        deleted = self.myListy[1]
        # this is the swap or setting the value of the first index to the last index's value
        self.myListy[1] = self.myListy[self.HowbigAmI]
        self.HowbigAmI = self.HowbigAmI - 1
        self.myListy.pop()
        self.getDown(1)
        return deleted
           
           
def main():
          
    myHeap = getHeapy() 
    
    start_time = timeit.default_timer()
   
    myHeap.getInThere(3)
    
    mil = 1000000
    # here I am just using the random library and doing numbers from 1 to a million a million times. 
    # the time i got was like 7 seconds. 
    while (mil > 0) :
    
        r = random.randrange(0,1000000)
        myHeap.getInThere(r)
        mil-=1
    executionTime = timeit.default_timer() - start_time
   
    print executionTime
    
   
  
          
if __name__=="__main__":main() 
          
            