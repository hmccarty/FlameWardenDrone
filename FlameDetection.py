import cv2 
import numpy as np
import threading
import random

class FlameDetector:
	def __init__(self, video_src, fb):
                self.video = cv2.VideoCapture(video_src)
                self.fb = fb
	
	def start_processing(self):
                t = threading.Thread(target=self.processing_thread, args=())
	        t.start()	
                
        def processing_thread(self):
		while True:
			(grabbed, frame) = self.video.read()
			frame = cv2.resize(frame, (352, 240))

			if not grabbed:
                                print "Failed to grab frame, ending thread."
				break;

			blur = cv2.GaussianBlur(frame, (21, 21), 0)
			hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)
			lower = [15, 0, 160]
			upper = [25, 230, 255]
			lower = np.array(lower, dtype="uint8")
			upper = np.array(upper, dtype="uint8")
			mask = cv2.inRange(hsv, lower, upper)
			output = cv2.bitwise_and(frame, hsv, mask=mask)

			params = cv2.SimpleBlobDetector_Params()
			params.minThreshold = 0
			params.maxThreshold = 255
			params.filterByArea = True
			params.minArea = 5 	
			params.filterByConvexity = True
			detector = cv2.SimpleBlobDetector(params)
			keypoints = detector.detect(output)
			im_keys = cv2.drawKeypoints(output, keypoints, np.array([]), (0,255,0), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
                        
                        cv2.imshow("vision", im_keys)
			#cv2.imshow("normal", frame)
                        self.fb.add_fire(

			if cv2.waitKey(1) and 0xFF == ord('q'):
				break

		cv2.destroyAllWindows()
		video.release()
