# Read agent
import pickle

import gym

with open("models/unit2/taxi_model.pkl", "rb") as f:
    model = pickle.load(f)

# Evaluate our Agent
from unit2.general.q_learn import evaluate_agent

# Get env from gym
env = gym.make(model["env_id"])

# Get parameters from model
max_steps = model["max_steps"]
n_eval_episodes = model["n_eval_episodes"]
Qtable_taxi = model["qtable"]
eval_seed = model["eval_seed"]

mean_reward, std_reward = evaluate_agent(env, max_steps, n_eval_episodes, Qtable_taxi, eval_seed)
print(f"Mean_reward={mean_reward:.2f} +/- {std_reward:.2f}")