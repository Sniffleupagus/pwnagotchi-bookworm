import os
from threading import Lock

# pwny-hydra - move frame_path to /tmp (truly temporary, not retained in /var/tmp), and put PID
# in filename to support multiple pwnagotchi on one system. Additional images will accumulate in
# /tmp until a reboot. in /var/tmp, they would accumulate until deleted. Potentially "breaking"
# change, since the semi-permanent "/var/tmp/pwnagotchi.png" is no longer available. I am unaware
# of any plugins or other code that accesses the png directly, so I think it is ok.

frame_path = '/tmp/pwnagotchi/pwnagotchi%d.png' % os.getpid()
frame_format = 'PNG'
frame_ctype = 'image/png'
frame_lock = Lock()


def update_frame(img):
    global frame_lock, frame_path, frame_format
    if not os.path.exists(os.path.dirname(frame_path)):
        os.makedirs(os.path.dirname(frame_path))
    with frame_lock:
        img.save(frame_path, format=frame_format)
