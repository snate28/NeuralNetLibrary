#This class is the first half of the convolutional layer, it takes an input and outputs values that have to be multiplied by weights
#In other words this class  takes a matrix  as an input and returns the "regions" of a given matrix which will later be multiplied by weights and summed to be a parameter of a filter
class Conv:
    def __init__(self, matrix, size=3, stride=1, padding=None, checkIfWrong=False): #Size argument here is the size of a region
        self.matrix = matrix
        self.size = size
        self.stride = stride
        self.padding = padding
        self.checkIfWrong = checkIfWrong
        
    def run(self):
        output=[]
        
        print "Getting the regions"
        columnSize,rawSize = self.matrix.shape #Get the shape of a matrix
        columnSize = int(columnSize)
        rawSize = int(rawSize)
    
        if self.checkIfWrong == True:
            if((rawSize-self.size) % self.stride) or ((columnSize-self.size) % self.stride) != 0:
                print  "Your connections are wrong. Please change the stride or the size of the region so (rawSize - size)/stride and(columnSize - size)/stride give no remainder."
        #Count how many times to stride right and down
        stridesRight = ((rawSize-self.size)/self.stride)+1 
        stridesDown =  ((columnSize-self.size)/self.stride)+1
        
        #Get the values for strides
        strideRightRange = []
        indx = 0-self.stride
        for i in range(stridesRight):
            indx+=self.stride
            strideRightRange.append(indx)
        
        strideDownRange = []
        indx = 0-self.stride
        for i in range(stridesDown):
            indx+=self.stride
            strideDownRange.append(indx)   
    
    
        for p in range(stridesDown):
            for i in strideRightRange:
                output.append(self.matrix[0+p:self.size+p,0+i:self.size+i])
        return output
        
