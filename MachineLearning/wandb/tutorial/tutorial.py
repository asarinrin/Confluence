import pandas as pd
import numpy as np
import wandb
import random
from sweep_configuratioin.sample_sweep_configuration import SWEEP_CONFIGURATION

SWEEP_CONFIGURATION = {
    'method': 'grid',
    'name': 'sweep',
    'metric': {
        'goal': 'minimize', 
        'name': 'validation_loss'
		},
    'parameters': {
        'batch_size': {'values': [16, 32, 64]},
        'epochs': {'values': [5, 10, 15]},
        # 'lr': {'max': 0.1, 'min': 0.0001}
    },
    # 'early_terminate': {
    #     'type': 'hyperband',
    #     's': 2,
    #     'eta': 3,
    #     'max_iter': 27
    # }
}

# 🐝 Step 1: Define training function that takes in hyperparameter 
# values from `wandb.config` and uses them to train a model and return metric
def train_one_epoch(epoch, lr, bs): 
    acc = 0.25 + ((epoch/30) +  (random.random()/10))
    loss = 0.2 + (1 - ((epoch-1)/10 +  random.random()/5))
    return acc, loss

def evaluate_one_epoch(epoch): 
    acc = 0.1 + ((epoch/20) +  (random.random()/10))
    loss = 0.25 + (1 - ((epoch-1)/10 +  random.random()/6))
    return acc, loss

def main():
    # Use the wandb.init() API to generate a background process 
    # to sync and log data as a Weights and Biases run.
    # Optionally provide the name of the project. 
    run = wandb.init(project='my-first-sweep')

    # note that we define values from `wandb.config` instead of 
    # defining hard values
    # lr  =  wandb.config.lr
    lr  =  0.01
    bs = wandb.config.batch_size
    epochs = wandb.config.epochs

    for epoch in np.arange(1, epochs):
        train_acc, train_loss = train_one_epoch(epoch, lr, bs)
        val_acc, val_loss = evaluate_one_epoch(epoch)

        run.log({
            'epoch': epoch, 
            'train_acc': train_acc,
            'train_loss': train_loss, 
            'val_acc': val_acc, 
            'val_loss': val_loss
        })

# 🐝 Step 2: Define sweep config
sweep_configuration = SWEEP_CONFIGURATION

# 🐝 Step 3: Initialize sweep by passing in config
sweep_id = wandb.sweep(sweep=sweep_configuration, project='my-first-sweep')

# 🐝 Step 4: Call to `wandb.agent` to start a sweep
wandb.agent(sweep_id, function=main)
