# open the frozen taxi model
import pickle

import gym

from unit2.general.upload_model import push_to_hub

with open("models/unit2/taxi_model.pkl", "rb") as f:
    model = pickle.load(f)

# Get env from gym
env = gym.make(model["env_id"])

username = "Akriel"  # FILL THIS
repo_name = "q-Taxi-v3"
push_to_hub(
    repo_id=f"{username}/{repo_name}",
    model=model,
    env=env
)
