import time


class FPS:
    def __init__(self):
        self.last_frame = time.time()
        self.fps = 0
        self.fps_log = [0]
        self.time_passed = 0

    def frame_begin(self):
        self.last_frame = time.time()

    def frame_end(self):
        self.time_passed = time.time() - self.last_frame
        if self.time_passed == 0:
            self.time_passed = 0.0001
        self.fps = int(1 / self.time_passed)
        self.fps_log.append(self.fps)
        if len(self.fps_log) > 60:
            self.fps_log.pop(0)
