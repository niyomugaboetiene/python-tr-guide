# Record the start and end time of program execution and compute duration.
from datetime import datetime
import time

start_time = datetime.now()

# program starts

time.sleep(3) # 3 secs

# program ends

end_time = datetime.now()

duration = end_time - start_time

print("Start time", start_time)
print("End time", end_time)
print("Duration", duration)