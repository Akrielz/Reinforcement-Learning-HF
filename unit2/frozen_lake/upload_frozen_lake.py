# open the frozen lake model
import pickle

import gym

from unit2.general.upload_model import push_to_hub

with open("models/unit2/frozenlake_model.pkl", "rb") as f:
    model = pickle.load(f)

# Get env from gym
env = gym.make(model["env_id"], map_name="4x4", is_slippery=False)

# Upload the model to the Hub
username = "Akriel" # FILL THIS
repo_name = "q-FrozenLake-v1-4x4-noSlippery"
push_to_hub(
    repo_id=f"{username}/{repo_name}",
    model=model,
    env=env
)