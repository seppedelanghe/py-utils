import cv2

'''
    Generator class for videos that returns a video frame by frame
'''
class VideoFrameGenerator:
    def __init__(self, path: str):
        self.cap = cv2.VideoCapture(path)
        self.done = False

        if not self.cap.isOpened():
            raise Exception("Failed to open video.")

    @property
    def fps(self):
        return self.cap.get(cv2.CAP_PROP_FPS)

    @property
    def resolution(self):
        return (int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

    def skip(self, to: int):
        self.cap.set(1, to)

    def __next__(self):
        if self.done == False:
            ret, frame = self.cap.read()
            if not ret:
                self.cap.release()
                self.done == True
                raise StopIteration

            return frame
            
    def __iter__(self):
        return self

    def __len__(self):
        return int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))

