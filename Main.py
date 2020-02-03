import FlameDetection as fd
import Firebase as fb
import GPS

#Inits fire base and sets drone id to 0
fbase = fb.Firebase(0)

#Inits GPS locator
l = GPS.Locator()
last_lon = None
last_lat = None

#Inits fire locator and sets camera port to 0
#Flame detector can also receive video files like "video_1.mp4"
fdetector = fd.FlameDetector(0, fbase)
fdetector.start_processing()

while True:
    curr_lon, curr_lat = locator.stream_data()
    if curr_lon != None and curr_lat != None:
        last_lon = curr_lon
        last_lat = curr_lat
        fbase.update_loc(curr_lon, curr_lat)


#f.add_fire(50, 50, 1)
