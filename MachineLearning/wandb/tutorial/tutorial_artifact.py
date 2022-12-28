import wandb
import random
import numpy as np
import pandas as pd

run = wandb.init(name="artifact_tutorial_v2", job_type="dataset")
artifact = wandb.Artifact(name="sample_dataset", type="dataset")

artifact.add_file(local_path="./tutorial.csv", name="hello2")
run.log_artifact(artifact)