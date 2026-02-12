# Display the current time in a different timezone.

from zoneinfo import ZoneInfo
from datetime import datetime

now_utc = datetime.now(ZoneInfo("UTC"))

nairobi_time = now_utc.astimezone(ZoneInfo("Africa/Nairobi"))
kigali_time = now_utc.astimezone(ZoneInfo("Africa/Kigali"))

print("UTC time", now_utc.strftime("%Y-%m-%d %H:%M:%S"))
print("Nairobi time", nairobi_time.strftime("%Y-%m-%d %H:%M:%S"))
print("Kigali time", kigali_time.strftime("%Y-%m-%d %H:%M:%S"))