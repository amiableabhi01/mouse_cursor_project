# cv2.inRange function is used to filter out a particular color from the frame
# The result then undergoes morphosis i.e. erosion and dilation
# Resultant frame is returned as mask 
def makeMask(hsv_frame, color_Range):
	
	mask = cv2.inRange( hsv_frame, color_Range[0], color_Range[1])
	# Morphosis next ...
	eroded = cv2.erode( mask, kernel, iterations=1)
	dilated = cv2.dilate( eroded, kernel, iterations=1)
	
	return dilated
