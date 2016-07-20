#fully connected layer
import numpy as np
import functions as f
import conv 
#class Full:
    #def __init__(self,vector,nodes,weights):
vector  = np.array([[3,5,7]])
nodes = 2

#def forward():
nothing,vectorLength = vector.shape
nothing = None
weights = np.zeros(shape=(nodes,vectorLength))

def act(input):
    return 1/(1+np.e**-input)

out = act(np.dot(weights,vector.T))
    

print conv.run(np.array([[1,2,3]]),size=1)


        
        
    
        
    
    
        
