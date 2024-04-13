def calculate(x):
    if len(x)!=9:
        raise ValueError("List must contain nine numbers.")
        
    arr=np.array(x,dtype=int)
    
    newarr = arr.reshape(3,3)
    
    calculations={

        'mean': [list(np.mean(newarr,axis=0)), list(np.mean(newarr,axis=1)), np.mean(newarr.flatten())],
        'variance': [list(np.var(newarr,axis=0)), list(np.var(newarr,axis=1)), np.var(newarr.flatten())],
        'standard deviation': [list(np.std(newarr,axis=0)), list(np.std(newarr,axis=1)), np.std(newarr.flatten())],
        'max': [list(np.max(newarr,axis=0)), list(np.max(newarr,axis=1)), np.max(newarr.flatten())],
        'min': [list(np.min(newarr,axis=0)), list(np.min(newarr,axis=1)), np.min(newarr.flatten())],
        'sum': [list(np.sum(newarr,axis=0)), list(np.sum(newarr,axis=1)), np.sum(newarr.flatten())],
    }
    
    return calculations 
