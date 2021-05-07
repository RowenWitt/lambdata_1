import pandas as pd
import numpy as np
import random
import pytest

test_list = [1,2,3,4,float('NAN')]
data = {'col1':['a','b','c','d','e','f',float('nan')], 'col2':['Bird','Cow',float('nan'),'Platypus','Giraffe','Zebra','Monkey'],'col3':[1,2,3,4,5,6,7]}
test_df = pd.DataFrame(data=data)



class NullCount:
    """Simple null counter class on input df or list"""
    def __init__(self):
        return

    def NullCounter(df):
        """Null counter function"""
        count = pd.isna(df).sum().sum()
        return count

    def test_NullCounter():
    """Testing null counter function"""
    test_df_nulls = pd.DataFrame(np.nan, index=[0,1,2,3,4,5], columns=['One','Two'])
    assert hf.NullCount.NullCounter(test_df_nulls) == 12


class TrainTest:
    """A simple train-test splitter using sample"""
    def __init__(self):
        return 

    def TrainTestSplit(df, frac):
        """Train-test split function"""
        a = df
        b = float(frac)
        print(b)
        train = a.sample(frac=b)
        test = df.drop(train.index[0:])

        return [print(train), print(test)]
        

class Randomize:
    """Input dataframe randomizer, need to 2-d randomize on 1-dtype dfs"""
    def __init__(self):
        return 'Instantiation, successful'

    def Randomizer(df, seed):
        """Because of different dtypes columns don't 2-d randomize"""
        cols = test_df.columns
        a = df
        b = int(seed)
        c = []
        for i in df.columns:
            z = (df[i].sample(frac=1,random_state=b,axis=0))
            c.append(list(z))
        nc = {i: c[i] for i in range(0, len(c))}
        d = pd.DataFrame(nc)
        return d