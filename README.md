# Reinforcement Learning - Hugging Face Course

This repository contains the code for the Hugging Face course on Reinforcement
Learning.

## Course

The course is available on the Hugging Face website:  
https://huggingface.co/deep-rl-course/unit0/introduction

## Progress:

### Everything is done!
Check my certificate [here](https://github.com/Akrielz/Reinforcement-Learning-HF/blob/main/certificate.pdf)


You can check my progress on the course here:  
https://huggingface.co/spaces/ThomasSimonini/Check-my-progress-Deep-RL-Course

With the username "Akriel".

**Warning: The following table and documentation is not updated with all the models yet**

| passed | unit   | env                         | mean   | std    | Link                                                                  |
|--------|--------|-----------------------------|--------|--------|-----------------------------------------------------------------------|
| ✅      | Unit 1 | LunarLander-v2              | 257.78 | 15.02  | [link](https://huggingface.co/Akriel/MLP-Lunar-Lander )               |
| ✅      | Unit 2 | Taxi-v3                     | 7.56   | 2.71   | [link](https://huggingface.co/Akriel/q-Taxi-v3)                       |
| ✅      | Unit 2 | FrozenLake                  | 1.00   | 0.00   | [link](https://huggingface.co/Akriel/q-FrozenLake-v1-4x4-noSlippery)  |
| ✅      | Unit 3 | SpaceInvadersNoFrameskip-v4 | 528.50 | 161.90 | [link](https://huggingface.co/Akriel/dqn-SpaceInvadersNoFrameskip-v4) |


## Installation

To install the dependencies, run the following command, where <ENV_NAME> is the
name of the environment you want to create:

```bash
conda env create -n <ENV_NAME> python=3.8
conda activate <ENV_NAME>
sudo ./env_setup.sh
```

Or you can install the same conda environment from the `environment.yml` file:

```bash
conda env create -f conda_environment.yml -n <ENV_NAME>
conda activate <ENV_NAME>
```

## Unit 1

Unit 1 is about the basics of Reinforcement Learning, applied on the game
Lunar Lander v2, used as an example in the OpenAI Gym. The game purpose is to
land a spaceship on a platform, without crashing.

Here is a video with the AI playing the game:

https://user-images.githubusercontent.com/34741250/217315000-ea7c8040-5fb5-4c7a-b29a-4413caf071f4.mp4

## Unit 1 Bonus

Unit 1 Bonus is about getting to use the environment from ML-Agents to train
an agent to play the game "Huggy the Dog", which has as goal to collect as many
sticks as possible.

Here is a video with the AI playing the game:

https://user-images.githubusercontent.com/34741250/217324570-1f4d94cf-de0a-4941-b494-b4825698a821.mp4

## Unit 2 

Unit 2 is about learning how Q-Learning works, and how to use it to train an
agent to play the game Taxi-v3, which has as goal to pick up a passenger at
one location and drop them off at another. Similarly, we are using it on the
game Frozen Lake, which has as goal to reach the goal state without falling
into a hole.

Here is a video with the AI playing Taxi-v3:

https://user-images.githubusercontent.com/34741250/218331070-2c3d8b24-68c3-4bf5-980f-ae676792e88c.mp4

Here is a video with the AI playing Frozen Lake:

https://user-images.githubusercontent.com/34741250/218331075-a97305cc-fe3b-4ed3-94b3-343c91f60eff.mp4

## Unit 3

Unit 3 is about applying RL Zoo to train a DQN agent to play the game
Space Invaders, which has as goal to shoot down as many aliens as possible.

Here is a video with the AI playing the game:

https://user-images.githubusercontent.com/34741250/219143123-6f6a6161-2095-4827-9eb8-1b2ce1a05ce4.mp4



