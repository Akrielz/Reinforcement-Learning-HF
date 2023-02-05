# Imports
import gym
import torch

from stable_baselines3 import PPO


def main():
    # Create environment
    env = gym.make('LunarLander-v2')

    # Check if GPU is available
    if torch.cuda.is_available():
        print("Using GPU")

    # Instantiate the agent
    model = PPO(
        'MlpPolicy',
        env,
        verbose=1,
        n_steps=2048,
        batch_size=64,
        n_epochs=10,
        gamma=0.999,
        gae_lambda=0.98,
        ent_coef=0.01,
        device='cuda',
    )

    # Train the model
    model.learn(total_timesteps=int(1e6))

    # Save the model
    model_name = "MLP-LunarLander"
    model.save(model_name)


if __name__ == "__main__":
    main()