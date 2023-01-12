""" Usecase -> grid search

    RIGHT_GBM_PARAMETER_CONFIG: template for grid search by lgbm

"""

RIGHT_GBM_TRAINING_PARAMETER_CONFIG = {
        'objective': 'multiclass',
        'num_iterations': [40, 50, 70, 100, 150], # default = 100
        'learning_rate': [0.05, 0.1, 0.15, 0.2], # default = 0.1
        'num_leaves': [20, 31, 50, 100, 150], # default = 31
        'max_depth': [-1, 1, 2, 3, 4, 5, 7, 9], # default = -1  --> no limit
        'min_data_in_leaf': [10, 20, 40], # default = 20
        'lambda_l1': [0, 0.01, 0.05, 0.1, 0.2, 0.5, 1.0], #default = 0
        'lambda_l2': [0, 0.01, 0.05, 0.1, 0.2, 0.5, 1.0], #default = 0
        'feature_fraction': [0.5, 0.6, 0.8, 1.0], # default = 1
        'feature_fraction_seed': 2, # default = 2
        'feature_fraction_bynode': [0.5, 0.6, 0.8, 1.0], # default = 1
        'bagging_fraction': [0.1, 0.2, 0.3, 0.5, 1.0], # default = 0
        'bagging_freq': [1, 2, 5, 10, 20], # default = 0
        'bagging_seed': 3, # default = 3
        # objective parameters
        'num_class': 3, # default = 1
        # metric parameters
        'metric': ["multi_logloss"],
}

# Reference
# https://lightgbm.readthedocs.io/en/latest/Parameters.html