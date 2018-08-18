#!/usr/bin/env python

"""
Unit tests for tune module
===========================
"""

import pytest
import pandas as pd
from implicitmf.tune import  gridsearchCV, smbo
from implicit.als import AlternatingLeastSquares
from _mock_data import sparse_array


def test_gridsearchCV_output():
    """
    Check that output of gridsearchCV()
    is a pandas dataframe.
    """
    als = AlternatingLeastSquares()
    hyperparams = {
        'regularization': [0.2,0.3]
    }
    output = gridsearchCV(base_model=als, X=sparse_array(), n_folds=2, hyperparams=hyperparams)
    assert isinstance(output, pd.DataFrame)

def test_smbo_hyperparam_error():
    """
    Check that objective() raises a ValueError
    is model parameter is not the correct format.
    """
    def obj(hyperparams):
        pass
    msg = "`model` must be either 'ltr' or 'als'"
    with pytest.raises(ValueError, match=msg):
        hyperparams = {'regularization':(10**-4, 10**-1, 'log-uniform')}
        smbo(X=sparse_array(), obj=obj, model='test',
        hyperparams=hyperparams, n_threads=10, n_calls=100, n_jobs=1)