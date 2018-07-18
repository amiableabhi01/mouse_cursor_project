# Depending upon the relative positions of the three centroids, this function chooses whether 
# the user desires free movement of cursor, left click, right click or dragging
def chooseAction(yp, rc, bc):
	out = np.array(['move', 'false'])
	if rc[0]!=-1 and bc[0]!=-1:
		
		if distance(yp,rc)<50 and distance(yp,bc)<50 and distance(rc,bc)<50 :
			out[0] = 'drag'
			out[1] = 'true'
			return out
		elif distance(rc,bc)<40: 
			out[0] = 'right'
			return out
		elif distance(yp,rc)<40:	
			out[0] = 'left'
			return out
		elif distance(yp,rc)>40 and rc[1]-bc[1]>120:
			out[0] = 'down'
			return out	
		elif bc[1]-rc[1]>110:
			out[0] = 'up'
			return out
		else:
			return out

	else:
		out[0] = -1
		return out
