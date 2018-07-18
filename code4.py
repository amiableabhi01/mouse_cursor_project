# Contours on the mask are detected.. Only those lying in the previously set area 
# range are filtered out and the centroid of the largest of these is drawn and returned 
def drawCentroid(vid, color_area, mask, showCentroid):
	
	contour, _ = cv2.findContours( mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	l=len(contour)
	area = np.zeros(l)
	# filtering contours on the basis of area rane specified globally 
	for i in range(l):
		if cv2.contourArea(contour[i])>color_area[0] and cv2.contourArea(contour[i])<color_area[1]: 
			area[i]="cv2.contourArea(contour[i])" 
		else:
			"" a="sorted(" area,="" reverse="True)" <="" p=""></color_area[1]:>
	# bringing contours with largest valid area to the top
	for i in range(l):
		for j in range(1):
			if area[i] == a[j]:
				swap( contour, i, j)

	if l > 0 :		
		# finding centroid using method of 'moments'
		M = cv2.moments(contour[0])
		if M['m00'] != 0:
			cx = int(M['m10']/M['m00'])
			cy = int(M['m01']/M['m00'])
			center = (cx,cy)
			if showCentroid:
				cv2.circle( vid, center, 5, (0,0,255), -1)
					
			return center
	else:
		# return error handling values
		return (-1,-1)

