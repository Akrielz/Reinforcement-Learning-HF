# Training parameters
import pickle

import gym

from unit2.general.q_learn import initialize_q_table, train

n_training_episodes = 10000  # Total training episodes
learning_rate = 0.7          # Learning rate

# Evaluation parameters
n_eval_episodes = 100        # Total number of test episodes

# Environment parameters
env_id = "FrozenLake-v1"     # Name of the environment
max_steps = 99               # Max steps per episode
gamma = 0.95                 # Discounting rate
eval_seed = []               # The evaluation seed of the environment

# Exploration parameters
max_epsilon = 1.0             # Exploration probability at start
min_epsilon = 0.05            # Minimum exploration probability
decay_rate = 0.0005            # Exponential decay rate for exploration prob

# Create the environment
env = gym.make(env_id, map_name="4x4", is_slippery=False)

# Init Qtable
Qtable_frozen_lake = initialize_q_table(env.observation_space.n, env.action_space.n)

# Train the agent
Qtable_frozen_lake = train(
    n_training_episodes, min_epsilon, max_epsilon, decay_rate, env, max_steps, Qtable_frozen_lake, learning_rate, gamma
)

# Create the "model"
model = {
    "env_id": env_id,
    "max_steps": max_steps,
    "n_training_episodes": n_training_episodes,
    "n_eval_episodes": n_eval_episodes,
    "eval_seed": eval_seed,

    "learning_rate": learning_rate,
    "gamma": gamma,

    "max_epsilon": max_epsilon,
    "min_epsilon": min_epsilon,
    "decay_rate": decay_rate,

    "qtable": Qtable_frozen_lake
}

# Save the model using pickle
with open("models/unit2/frozen_lake_model.pkl", "wb") as f:
    pickle.dump(model, f)