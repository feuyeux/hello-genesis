import genesis as gs
import os

gs.init(backend=gs.cpu)

scene = gs.Scene()

plane = scene.add_entity(
    gs.morphs.Plane(),
)

# https://github.com/Genesis-Embodied-AI/Genesis/blob/main/genesis/assets/xml/franka_emika_panda/panda.xml
franka = scene.add_entity(
    gs.morphs.MJCF(
        file=os.path.join(os.path.expanduser("~"), "Downloads", "panda.xml"),
    ),
)

scene.build()
for i in range(1000):
    scene.step()
