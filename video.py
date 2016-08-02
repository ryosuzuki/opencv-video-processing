import cv2
import sys, getopt

pixel_count = 52
file = './video/invader.mp4'

def main(argv):
  if (argv and argv[0]):
    global file
    file = argv[0]
  if (argv and argv[1]):
    global pixel_count
    pixel_count = int(argv[1])
  stream()

def stream():
  cap = cv2.VideoCapture(file)
  while not cap.isOpened():
    cap = cv2.VideoCapture(file)
    cv2.waitKey(1000)
    print 'Wait for the header'

  pos_frame = cap.get(cv2.cv.CV_CAP_PROP_POS_FRAMES)
  while True:
    flag, frame = cap.read()
    if flag:
      # The frame is ready and already captured
      process(frame)
      pos_frame = cap.get(cv2.cv.CV_CAP_PROP_POS_FRAMES)
      print str(pos_frame) + ' frames'
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

def process(img):
  original_size = img.shape[:2][::-1]
  output_size = (pixel_count, pixel_count)
  img_small = cv2.resize(img, output_size)
  # Grayscale
  img_gray = cv2.cvtColor(img_small, cv2.COLOR_RGB2GRAY)
  # Black and white
  (thresh, img_bw) = cv2.threshold(img_gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
  img_bw = cv2.threshold(img_gray, thresh, 255, cv2.THRESH_BINARY)[1]
  # Output with original size
  img_out = cv2.resize(img_bw, original_size, interpolation=cv2.cv.CV_INTER_NN)
  cv2.imshow('video', img_out)

if __name__ == '__main__':
  main(sys.argv[1:])














