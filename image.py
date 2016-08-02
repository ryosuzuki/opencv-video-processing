import cv2

img = cv2.imread('./image/img.jpg')
original_size = img.shape[:2][::-1]
output_size = (26, 26)
# img2 = cv2.resize(img, (original_size[0]/20, original_size[1]/20))
img2 = cv2.resize(img, output_size)

cv2.imwrite('./image/img_mosaic.jpg', img2)
print(img2)
# => 26x26

# Read as gray scale
img_gray = cv2.imread('./image/img_mosaic.jpg', cv2.CV_LOAD_IMAGE_GRAYSCALE)

# Set threshold for binary image
(thresh, img_bw) = cv2.threshold(img_gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
print(thresh)
# => 93.0

img_bw = cv2.threshold(img_gray, thresh, 255, cv2.THRESH_BINARY)[1]
cv2.imwrite('./image/img_bw.jpg', img_bw)

print(img_bw)

img_bw_large = cv2.resize(img_bw, original_size, interpolation=cv2.cv.CV_INTER_NN)
cv2.imwrite('./image/img_bw_large.jpg', img_bw_large)