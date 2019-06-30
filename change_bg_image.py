import itertools
import os
import random
from subprocess import check_output, CalledProcessError

from config import IMAGES_DIR, MONITOR_NUM, WORKSPACE_NUM

image = random.choice(os.listdir(IMAGES_DIR))
path = os.path.join(IMAGES_DIR, image)

monitors = range(MONITOR_NUM)
workspaces = range(WORKSPACE_NUM)
for monitor, workspace in itertools.product(monitors, workspaces):
    command = (
        "xfconf-query "
        "--channel xfce4-desktop "
        "--property /backdrop/screen0/monitor{}/workspace{}/last-image "
        "--set {}".format(monitor, workspace, path)
    )
    try:
        result = check_output(command, shell=True)
    except CalledProcessError as e:
        raise e
