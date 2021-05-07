from random import randint
import pytest
from lambdata_witt import helper_functions as hf 
import pandas as pd
import numpy as np

def test_NullCounter():
    """Testing null counter function"""
    test_df_nulls = pd.DataFrame(np.nan, index=[0,1,2,3,4,5], columns=['One','Two'])
    assert hf.NullCount.NullCounter(test_df_nulls) == 12