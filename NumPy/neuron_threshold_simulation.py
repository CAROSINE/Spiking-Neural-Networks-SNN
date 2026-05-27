import numpy as np

neurons = np.array([0.5, 0.8, 0.3])

threshold = 0.6 
print("neurons values: ", neurons)
print("Threshold: ", threshold)

fired = neurons > threshold  
print("Fired?: ", fired)  

print("Active neurons: ",neurons[fired])
   
weights = np.array([0.4, 0.7, 0.2])  
signal = neurons * weights   
print("Output Signal: ",signal )  
print("Total signal: ", signal.sum())    
