# Genesis

<https://genesis-world.readthedocs.io/en/latest/user_guide/index.html>

<https://genesis-world.readthedocs.io/zh-cn/latest/user_guide/overview/what_is_genesis.html>

Genesis is a physics platform designed for general purpose *Robotics/Embodied AI/Physical AI* applications. It is simultaneously multiple things:

1. A **universal physics engine** re-built from the ground up, capable of simulating a wide range of materials and physical phenomena.
2. A **lightweight**, **ultra-fast**, **pythonic**, and **user-friendly** robotics simulation platform.
3. A powerful and fast **photo-realistic rendering system**.
4. A **generative data engine** that transforms user-prompted natural language description into various modalities of data.

Genesis 是一个用于机器人、嵌入式 AI 和物理 AI 应用的综合物理平台。它包含以下核心功能：

1. **通用物理引擎**：从零开始构建，可模拟多种材料和物理现象
2. **机器人仿真平台**：轻量、高速、Python友好、易于使用
3. **照片级渲染系统**：高性能、真实感强
4. **数据生成引擎**：把自然语言描述转换成各类数据

<https://github.com/Genesis-Embodied-AI/Genesis>

<https://pypi.org/project/genesis-world>

## install

```sh
conda create -n genesis_env -y
conda activate genesis_env
pip install --upgrade pip
```

```sh
pip install torch torchvision torchaudio -i https://pypi.org/simple
pip install genesis-world
git clone https://github.com/Genesis-Embodied-AI/Genesis.git
cd Genesis
pip install -e . -i https://pypi.org/simple
```

## play

[hello_genesis.py](https://github.com/Genesis-Embodied-AI/Genesis/blob/main/examples/tutorials/hello_genesis.py)

```python
import genesis as gs

gs.init(backend=gs.cpu)

scene = gs.Scene()

plane = scene.add_entity(
    gs.morphs.Plane(),
)
# https://github.com/Genesis-Embodied-AI/Genesis/blob/main/genesis/assets/xml/franka_emika_panda/panda.xml
franka = scene.add_entity(
    # gs.morphs.URDF(
    #     file='urdf/panda_bullet/panda.urdf',
    #     fixed=True,
    # ),
    gs.morphs.MJCF(file="xml/franka_emika_panda/panda.xml"),
)

scene.build()
for i in range(1000):
    scene.step()
```

```sh
conda activate genesis_env

$ cd /Users/hanl5/Downloads/Genesis
cp /Users/hanl5/coding/feuyeux/hello-genesis/hello_genesis.py .
python hello_genesis.py
```

## demo

https://www.youtube.com/watch?v=jM_rYOrgJ7E
