import string
import pandas as pd
#from postscrape.postscrape.spiders.NFL import NFL
import pandas as pd

# I found that I forgot to convert years type from string to list which makes its appearance not that good on excel 
# so this is a simple pretty algorithm

data = pd.read_csv("postscrape/postscrape/spiders/Newplayers.csv")
for i,years in enumerate(data):
    try:
        data.iloc[i,1] = years.split(',')
    except:
        data.iloc[i,1] = []

print(data.iloc[:,1])
data.to_csv ('pretty.csv', index = False, header=True)






