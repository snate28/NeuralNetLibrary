import numpy as np
def weights_init(inSize,outSize): #initialize the weights
    return 2*np.random.random((inSize,outSize))-1
    
def Sigmoid(input, weights): #create a sigmoid layer and return a layer along with its derivative
    out = 1/(1+np.exp(-np.dot(input,weights)))
    derivative = out*(1-out)
    return out,derivative
    
def square_loss(target,output):
    return target-output
    
def backProp(layers, weights, deriv, size, rate = 1): 
    derivative = deriv.pop()#get the cost function derivative
    #reverse all the lists because we need to go backwards
    deriv = deriv[::-1] 
    layers = layers[::-1]
    weights = weights[::-1]
    new_weights=[]
    #backpopagate
    new_weights.append(weights[0]+(layers[1].T.dot(derivative*rate))) #this one does not fit  the algorithm well inside the for loop, so it's outside of it
    for i in range(len(size)-2):
        derivative = derivative.dot(weights[i].T)*deriv[i]
        new_weights.append(weights[i+1]+(layers[i+2].T.dot(derivative*rate)))
    return new_weights[::-1]

def train(input,size,loss="square_loss",rate=1,epochs=1,examples=None,labels=None): #train the network
    layers=[]
    weights=[]
    derivs=[] 
    import ANN
    loss = getattr(ANN,loss) #get the loss function's name
    for i in xrange(len(size)-1): #weights initialization
        weights.append(weights_init(size[i],size[i+1]))

    for i in xrange(epochs): #the training process
        for example, target in input:  #online learning
            layers.append(example) 
            for i in xrange(len(size)-1):
                layer, derivative = Sigmoid(layers[i],weights[i])#calculate the layer and itd derivative
                layers.append(layer)
                derivs.append(derivative)
            
            loss_deriv = loss(target,layers[-1]) #loss function
            
            derivs[-1] = loss_deriv*derivs[-1] #multiply the loss function by the final layer's derivative
            weights = backProp(layers,weights,derivs,size) #update the weights
            layers=[]
            derivs = []
    return weights 
    

   
    
    

def run(input,weights): #run a trained neural network
    layers=[input]
    for i in xrange(len(weights)):
        layer,derivative = Sigmoid(layers[i],weights[i])
        layers.append(layer)
    return layers
     
           
                
#an example:
#dataset:    
#X = [(np.array([[0,0,1]]),np.array([[0,1]])),( np.array([[0,1,1]]),np.array([[1,0]])), (np.array([[1,0,1]]),np.array([[1,0]])), (np.array([[1,1,1]]),np.array([[0,1]]))]
#:train:
#weights = train(X,[3,4,2],epochs=1000)
        
