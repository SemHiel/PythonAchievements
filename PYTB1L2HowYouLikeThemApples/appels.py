
import math

#Vervang de 0-en met de juiste berekeningen

trees               = 333             #hoeveel bomen zijn er in totaal?
shadedTrees         = math.ceil((trees/3)*2)  #hoeveel bomen staan er in de schaduw (afgerond naar boven)?
sunnyTrees          = trees/3             #hoeveel in de zon?

shadeOutputModifier = 0.8            #hoeveel procent productie geeft een schaduwboom?

sunnyTreeOutput     = 146            #hoeveel appels geeft 1 zonnige boom?
shadedTreeOutput    = shadeOutputModifier*sunnyTreeOutput             #hoeveel appels geeft 1 schaduw boom?

sunnyOutput         = sunnyTrees*sunnyTreeOutput           #hoeveel appels geven alle zonnige bomen?
shadedOutput        = shadedTreeOutput*shadedTrees             #hoeveel appels geven alle schaduw bomen?
totalOutput         = sunnyOutput+shadedOutput             #hoeveel appels zijn er in totaal?

owners              = 4             #met hoeveel mensen verdelen we de appels?

eatCount            = totalOutput%owners             #hoeveel appels houden we over omdat ze niet eerlijk te verdelen zijn?
sellableOutput      = totalOutput-eatCount             #hoeveel appels zijn er over en dus verkoopbaar?
cut                 = sellableOutput/owners            #hoeveel appels mag ik verkopen?

print(cut)
