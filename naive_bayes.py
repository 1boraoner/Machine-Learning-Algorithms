import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import seaborn as sns
from math import pi
def gaussian_prob(mean,var,x):
    
    z = (x- mean)**2 / var
    probs = (1/(np.sqrt(2*pi*var))) * np.exp(-0.5 *z)
    prob = 1
    for i in range(len(probs)):
        prob*=probs[i]    
    return prob
    

def naive_prediction(p_ck,means,vas,new_data):
    prob_vec = []
    for i in range(len(p_ck)):
        t = gaussian_prob(means[i],vas[i],new_data) 
        prob_vec.append(p_ck[i] * t)   
    
    max_prob_class = np.argmax(prob_vec)
    return prob_vec,max_prob_class

from sklearn.datasets import make_blobs

class_number = 4
sample_size = 10000
feat_num = 2

X,y = make_blobs(n_samples=sample_size,n_features=feat_num,centers=class_number)
new_data = np.random.rand(2)

df = pd.DataFrame(X,columns=['x1','x2'])
df['y'] = y

means = []
vas = []
p_ck = np.array(df.groupby('y')['x1'].count() / sample_size)

for ck in range(class_number):
    means.append(np.mean(df[df['y']==ck],axis=0)[:-1])
    vas.append(np.var(df[df['y']==ck],axis=0)[:-1])

result = naive_prediction(p_ck,means,vas,new_data)

#y = 0 purple
#y = 1 blue
#y = 2 green
#y = 3 yellow
colors_list = ["purple", "blue",'green','yellow']

print(f'Predicted data: {new_data}, probability matrix: {result[0]}, Class prediction: {result[1]} ({colors_list[result[1]]})')

plt.scatter(X[:,0],X[:,1],c=y,cmap=mcolors.ListedColormap(colors_list))
plt.scatter(new_data[0],new_data[1],marker='x',s=100,c='red')
            #c=colors_list[result[1]])
plt.show()