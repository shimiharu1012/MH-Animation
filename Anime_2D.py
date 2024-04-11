import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from mealpy import bio_based
from mealpy import evolutionary_based
from mealpy import human_based
from mealpy import math_based
from mealpy import music_based
from mealpy import physics_based
from mealpy import swarm_based
from mealpy import system_based

import opfunu


#function and model to optimize
#model has some propeties 
#tune propeties parameters
func=opfunu.name_based.Bird(ndim=2)
model=swarm_based.PSO.OriginalPSO(epoch=50,pop_size=50)
# model=swarm_based.PSO.OriginalPSO(epoch=50,pop_size=50)

def my_func(solution):
    return np.sum(solution**2)


#define a problem
problem_dict1={
    "fit_func": func.evaluate,
    "lb": func.lb,  #lower bounds
    "ub": func.ub,   #upper bounds
    "minmax":"min",
    "verbose":True,
    "save_population":True,
}

#optimize
best_position,best_fitness=model.solve(problem_dict1)
POPlist=model.history.list_population       #get histroy to visualize


fig,ax=plt.subplots()
ims=[] 

###---make animation---###
for gen in range(len(POPlist)):

    x=[]
    y=[]

    for c_s in POPlist[gen]:
        #現在の世代genの全ての解候補の座標(x,y,z)をリスト化
        x.append(c_s[0][0])
        y.append(c_s[0][1])
        
    #世代genの解候補を散布図に書き出し、フレームリストに追加        

    #ax_=fig.add_subplot(projection="3d")    
    #opfunu.plot_3d(func,n_space=100,ax=ax_)
    im=ax.scatter(func.x_global[0],func.x_global[1],color="darkred",edgecolor="black",linewidths=0.3)
    im=ax.scatter(x,y,color="lightcoral",edgecolor="black",linewidth=0.3)
    ims.append([im])

    
    
ani=animation.ArtistAnimation(fig,ims,interval=100)


#--  to show
plt.show()  

#-- to save
#fn_name=input()
#ani.save(f"Animation/{fn}.gif")   

