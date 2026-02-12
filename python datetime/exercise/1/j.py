# Generate timestamps for file names or logs.
from datetime import datetime
now = datetime.now()

timestamp = now.strftime("%Y%m%d_%H%M%S")

filename = f"log_{timestamp}.txt"

print("Timestamp: ", timestamp)
print("File name: ", filename)