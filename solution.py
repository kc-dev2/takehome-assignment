from datetime import datetime
import time, json

import pytz
from tzlocal import get_localzone

# load json data first
with open('Netlify-follower-raw.json') as json_file:
     json_data = json.load(json_file)

# separate user data from location
# key = user_id, value = [{user.data},"{user.data.location}"]

def get_locations(user_data):
	# use split to separate {user.data} and {user.data.location}
	data_values = user_data.values()
	# need to do 2 things: (1) get location - "".join(loc[0].split(", ")[1:]) and (2) filter out None values bc
	# they don't provide any usable information on location
	locs = ["".join(loc[0].split(", ")[1:]) for loc in data_values if "".join(loc[0].split(", ")[1:]) != 'None']
	 
	# just used for testing code
	# for x in data_values[0:10]:
	# 	y = x[0]
	# 	print(y)
	# 	print("".join(y.split(",")[1:]))
	# print(len(locs))

	return locs


# fn to convert follower locations into timezones 
# Input: User inputted location data
# Output: Timezone
def loc_to_timezone(loc):
	# Not sure how to implement this without the use of some map API to retrieve coordinates and then converting 
	# coordinates to timezone (could use TimezoneFinder module for conversion) 
	# return timezone
	pass

# fn to convert timezone to local time
# Input: now is current datetime, tz is targeted timezone
# Output: returns 'now' into local time of specified timezone
def tz_to_time(now, tz):
	TIMEZONE = pytz.timezone(tz)
	conv_dt = now.astimezone(TIMEZONE)
	return conv_dt


if __name__ == '__main__':
	dt = datetime.now()
	print("Current datetime: {}".format(dt))

	jpn = tz_to_time(dt, 'Asia/Tokyo')
	print("JST datetime: {}".format(jpn))

	zur = tz_to_time(dt, 'Europe/Zurich')
	print("ZUR datetime: {}".format(zur))

	# diff = jpn - zur
	# print(diff)

	test = get_locations(json_data)
	#print(test)

