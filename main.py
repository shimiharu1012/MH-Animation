import sys
sys.dont_write_bytecode = True

from mealpy import bio_based
from mealpy import evolutionary_based
from mealpy import human_based
from mealpy import math_based
from mealpy import music_based
from mealpy import physics_based
from mealpy import swarm_based
from mealpy import system_based

import opfunu

from Anime_2D import generate_2D_animation
from Anime_3D import generate_3D_animation


func_num=int(input('select function [1.Ackley,2.Alpine,3.EggCrate,4.EggHolder,]:'))

if func_num==1:
    func=opfunu.name_based.Bird()
elif func_num==2:
    func=opfunu.name_based.Alpine02()
elif func_num==3:
    func=opfunu.name_based.EggCrate()
elif func_num==4:
    func=opfunu.name_based.EggHolder()
else:
    print("your input is unacceptable!!")
    sys.exit()


model_num=int(input('select model [1.DE,2.PSO,3.ABC,4.FFA]:'))

if model_num==1:
    model=evolutionary_based.DE.BaseDE(epoch=50,pop_size=50)
elif model_num==2:
    model=swarm_based.PSO.OriginalPSO(epoch=50,pop_size=50)
elif model_num==3:
    model=swarm_based.ABC.OriginalABC(epoch=50,pop_size=50)
elif model_num==4:
    model=swarm_based.FFA.OriginalFFA(epoch=50,pop_size=50)
else:
    print("your input is unacceptable!!")
    sys.exit()

Animetion_dim=int(input('input animation dimention [2 or 3]:'))

if Animetion_dim==2:
    generate_2D_animation(func,model)
elif Animetion_dim==3:
    generate_3D_animation(func,model)
else:
    print("your input is unacceptable!!")
    sys.exit()
    
    

