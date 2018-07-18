'''
This function takes as input the center of yellow region (yc) and 
the previous cursor position (pyp). The new cursor position is calculated 
in such a way that the mean deviation for desired steady state is reduced.
'''
def setCursorPos( yc, pyp):
	
	yp = np.zeros(2)
	
	if abs(yc[0]-pyp[0])<5 and abs(yc[1]-pyp[1])<5:
		yp[0] = yc[0] + .7*(pyp[0]-yc[0]) 
		yp[1] = yc[1] + .7*(pyp[1]-yc[1])
	else:
		yp[0] = yc[0] + .1*(pyp[0]-yc[0])
		yp[1] = yc[1] + .1*(pyp[1]-yc[1])
	
	return yp
