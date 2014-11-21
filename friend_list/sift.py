import cv2, sys, os
import numpy as np

img1 = []
img2 = []
detector = cv2.SIFT()
x = 0
print 'start'
for path in os.listdir(sys.argv[1]):
    path = os.path.join(sys.argv[1], path)
    gray = cv2.imread(path, 0)
    
    h, w = gray.shape
    gray = gray[ : ,w - h :]
    
    p, k = detector.detectAndCompute(gray, None)
    img1.append( (path, k) )
    
    print x,'\r',
    x+=1
print 'img1 finished'
    
x = 0
for path in os.listdir(sys.argv[2]):
    path = os.path.join(sys.argv[2], path)
    gray = cv2.imread(path, 0)
    p, k = detector.detectAndCompute(gray, None)
    img2.append( (path, k) )
    
    print x,'\r',
    x+=1
print 'img2 finished'



with open('rst.txt', 'w') as f:
    for p1, k1 in img1:
        pb, cb = None, 0
        x = 0
        
        matcher = cv2.BFMatcher(cv2.NORM_L2)       
        
        for p2, k2 in img2:
            print x,'\r',
            x+=1
            matches = matcher.knnMatch(k2,k1,k=2)
            cnt = sum([m.distance < 0.7*n.distance for (m, n) in matches])
            
            if cnt > cb:
                cb = cnt
                pb = p2
        print '[%s]'%cb, p1, pb
        print >>f, p1, pb

    
'''
#SIFT
detector = cv2.SIFT()
p1, k1 = detector.detectAndCompute(gray,None)
p2, k2 = detector.detectAndCompute(gray2,None)

FLANN_INDEX_KDTREE = 0
index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
search_params = dict(checks=50)   # or pass empty dictionary

flann = cv2.FlannBasedMatcher(index_params,search_params)
matches = flann.knnMatch(k1,k2,k=2)

count = 0

#matchesMask = [0 for i in xrange(len(matches))]
for i,(m,n) in enumerate(matches):
    if m.distance < 0.7*n.distance:
        count += 1
        #matchesMask[i]=1

print count
'''