import FlameDetection as fd
import Firebase as fb

f = fb.Firebase(0)

f.update_loc(50, 50)
f.add_fire(50, 50, 1)

#f = fd.FlameDetector(0)
#f.start_processing()
