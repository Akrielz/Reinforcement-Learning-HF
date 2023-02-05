import gym
from stable_baselines3 import PPO
from stable_baselines3.common.evaluation import evaluate_policy


def main():
    # Load model "Aky-Lander"
    model = PPO.load("models/unit1/MLPLunarLander")

    # Create a new environment for evaluation
    eval_env = gym.make("LunarLander-v2")

    # Evaluate the model with 10 evaluation episodes and deterministic=True
    mean_reward, std_reward = evaluate_policy(model, eval_env, n_eval_episodes=10, deterministic=True)

    # Print the mean reward
    print(f"Mean reward: {mean_reward:.2f} +/- {std_reward:.2f}")


if __name__ == "__main__":
    main()