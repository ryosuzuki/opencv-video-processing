import cv2

def main():
  cap = cv2.VideoCapture('./video/invader.mp4')
  while not cap.isOpened():
    cap = cv2.VideoCapture('./video/invader.mp4')
    cv2.waitKey(1000)
    print 'Wait for the header'

  pos_frame = cap.get(cv2.cv.CV_CAP_PROP_POS_FRAMES)
  while True:
    flag, frame = cap.read()
    if flag:
      # The frame is ready and already captured
      processFrame(frame)
      pos_frame = cap.get(cv2.cv.CV_CAP_PROP_POS_FRAMES)
      print str(pos_frame)+' frames'
    else:
      # The next frame is not ready, so we try to read it again
      cap.set(cv2.cv.CV_CAP_PROP_POS_FRAMES, pos_frame-1)
      print 'frame is not ready'
      # It is better to wait for a while for the next frame to be ready
      cv2.waitKey(1000)

    if cv2.waitKey(10) == 27:
      break
    if cap.get(cv2.cv.CV_CAP_PROP_POS_FRAMES) == cap.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT):
      # If the number of captured frames is equal to the total number of frames,
      # we stop
      break

def processFrame(img):
  original_size = img.shape[:2][::-1]
  output_size = (26, 26)
  img2 = cv2.resize(img, output_size)
  img3 = cv2.resize(img2, original_size, interpolation=cv2.cv.CV_INTER_NN)
  cv2.imshow('video', img3)

if __name__ == '__main__':
  main()



