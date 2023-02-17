# RL&Robot Assignment
This is one of the assignment for Frontier Research Practice II (Prof. Dong Hao track，Spring 2023) at Peking University - Practice for reinforcement learning and robot simulator.

### Pre-requisite knowledge
+ Familiar with [Isaac Gym ](https://developer.nvidia.com/isaac-gym) and able to read and understand the code of the official **example**.
+ Familiar with Reinforcement Learning (RL) Algorithm.

If you haven't done it yet, please refer to our [Tencent documentation](https://docs.qq.com/doc/DV2lNQ3BjZkdIaFhI?&u=e23d125f17914e8fbff97bd0f703c79e) to learn the pre-requisite knowledge
### Your Task
+ Task 1: Try to run the code and familiar with the detail:
    (1) How the RL algorithm interacts with the environment;
    (2) How the file structure is organized.
+ Task 2: To try to build your own environment or algorithm, you can start with these entry ways: (**Optional**)
(1) Change the object or agent and retrain RL;
(2) Change the environment parameters (e.g. friction, damping) and retrain RL;
(3) Create an new environment, set up a new RL task in the environment and try to train it. (**Hard**)

+ Task 3: Submit your notes, or some findings, or a video of the training results, etc to TA through [WeChat](https://gengyiran.github.io/images/WeChat.jpeg)

The whole assignment will get full marks if you complete **task 1** carefully. Of course, we encourage you to complete other tasks carefully and you will gain more.

### Build Environment
- The code has been tested on Ubuntu `18.04/20.04` with Python `3.7/3.8`. The minimum recommended NVIDIA driver version for Linux is `470.74` (dictated by support of IsaacGym).

- We use Anaconda to create virtual environments. To install `Anaconda`, follow instructions [here](https://docs.anaconda.com/anaconda/install/linux/).

- Details regarding installation of IsaacGym can be found [here](https://developer.nvidia.com/isaac-gym). We highly recommend you to install the Preview `Release 4 version` of IsaacGym, because other versions may have collision detection issues.
**DO NOT** use `./create_conda_env_rlgpu.sh`, We highly recommend you to create a conda enviroment first and then use `pip install -e .` to install isaacgym only without create a new environment.

- Ensure that Isaac Gym works on your system by running one of the examples from the `python/examples` directory, like `joint_monkey.py`. Please follow troubleshooting steps described in the Isaac Gym `Preview Release 3/4 install instructions` if you have any trouble running the samples.

- To install `mani_skill_learn`, you can clone `ManiSkill-Learn` and then install the package as following commands:
```
git clone https://github.com/haosulab/ManiSkill-Learn.git
cd ManiSkill-Learn/
pip install -e .
```

### Run the code

In the root folder, run:
```
./scripts/open_door.sh
```
