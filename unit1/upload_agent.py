import gym

from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import DummyVecEnv

from huggingface_sb3 import package_to_hub


def main():
    env_id = "LunarLander-v2"
    model_architecture = "PPO-MLP"
    repo_id = "Akriel/MLP-Lunar-Lander"
    commit_message = "Upload PPO LunarLander-v2 trained agent"
    model_name = "Aky-LunarLander"
    model = PPO.load(model_name)

    # Create the evaluation env
    eval_env = DummyVecEnv([lambda: gym.make(env_id)])

    # PLACE the package_to_hub function you've just filled here
    package_to_hub(
        model=model,  # Our trained model
        model_name=model_name,  # The name of our trained model
        model_architecture=model_architecture,  # The model architecture we used: in our case PPO
        env_id=env_id,  # Name of the environment
        eval_env=eval_env,  # Evaluation Environment
        repo_id=repo_id,  # id of the model repository from the Hugging Face Hub (repo_id = {organization}/{repo_name} for instance ThomasSimonini/ppo-LunarLander-v2
        commit_message=commit_message
    )


if __name__ == "__main__":
    main()