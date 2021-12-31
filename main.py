import string
import pandas as pd
#from postscrape.postscrape.spiders.NFL import NFL

import pandas as pd

data = pd.read_csv("postscrape/postscrape/spiders/Newplayers.csv")
d = data.Year

x = data
for i,l in enumerate(d):
    try:
        x.iloc[i,1] = l.split(',')
    except:
        x.iloc[i,1] = " "

print(x.iloc[:,1])
x.to_csv ('pretty.csv', index = False, header=True)






