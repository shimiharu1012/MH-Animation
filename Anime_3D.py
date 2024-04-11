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
func=opfunu.name_based.HolderTable(ndim=2)
model=swarm_based.FFA.OriginalFFA(epoch=80,pop_size=50)

#define a problem
problem_dict1={
    "fit_func": func.evaluate,
    "lb": func.lb,  #lower bounds
    "ub":func.ub,   #upper bounds
    "minmax":"min",
    "verbose":True,
    "save_population":True,
}

#optimize
best_position,best_fitness=model.solve(problem_dict1)
POPlist=model.history.list_population       #get histroy to visualize


###---Visualization---###

fig=plt.figure()
#zorder is order for draw objects
ax=fig.add_subplot(projection="3d",computed_zorder=False)   
ims=[] 


###---draw function's surface---###

N=100
X = np.linspace(func.lb[0],func.ub[0], N)
Y = np.linspace(func.lb[1],func.ub[1],N)

X_mesh,Y_mesh=np.meshgrid(X,Y)

Z=np.zeros((len(Y),len(Y))) #initialize Z matrix

#assign function value to Z
for i in range(len(X)):
    for j in range(len(Y)):
        XY=np.array([X[i],Y[j]])
        Z[j][i]=func.evaluate(XY)


#draw function's surface (normal or wireframe)
ax.plot_surface(X_mesh,Y_mesh,Z,color=(0,0.2,1,0.5),zorder=1)
#ax.plot_wireframe(x_mesh,y_mesh,z,rstride=5,cstride=5,color=(0,0,0,0.3),zorder=1)

ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")


###---make animation---###
for gen in range(len(POPlist)):

    x=[]
    y=[]
    z=[]

    for c_s in POPlist[gen]:
        #現在の世代genの全ての解候補の座標(x,y,z)をリスト化
        x.append(c_s[0][0])
        y.append(c_s[0][1])
        xy=np.array([c_s[0][0],c_s[0][1]])
        z_value=func.evaluate(xy)
        z.append(z_value)
    #世代genの解候補を散布図に書き出し、フレームリストに追加        

    #ax_=fig.add_subplot(projection="3d")    
    #opfunu.plot_3d(func,n_space=100,ax=ax_)
    im=ax.scatter(func.x_global[0],func.x_global[1],func.evaluate(func.x_global),color="black"\
                  ,edgecolor="black",linewidth=0.3,zorder=4)
    im=ax.scatter(x,y,z,color="tomato",edgecolor="red",linewidth=0.3,zorder=4)
    ims.append([im])
    
ani=animation.ArtistAnimation(fig,ims,interval=100)


 
#--  to show
plt.show()  


#-- to save
#fn_name=input()
#ani.save(f"Animation/{fn}.gif")   

