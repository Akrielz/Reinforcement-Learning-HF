import gym
from stable_baselines3 import PPO


def main():
    # Load agent
    model = PPO.load("models/unit1/MLPLunarLander")

    # Visualize the agent
    env = gym.make('LunarLander-v2')

    obs = env.reset()
    while True:
        action, _states = model.predict(obs)
        obs, rewards, dones, info = env.step(action)
        env.render()

        if dones:
            obs = env.reset()


if __name__ == "__main__":
    main()