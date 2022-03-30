# Contenda Takehome
Task: Find optimal times to post content to reach as many of my followers as possible

## Steps:
The first thing I did was to spend 15-20 minutes to understand the prompt and jot down any initial thoughts. This includes what modules I might use, what it means to be 'optimal', steps to take, etc. I also looked through the JSON data to get a better understanding of how it's formatted so it would be easier to figure out how to extract the data that I want/need. Initial thoughts are outlined in the **prompt.txt** file.

*note: I don't believe the JSON is formatted 100% correctly as explained in README. For example, it looks to be formatted as {"{user_id}":["<{user.data},{user.data.location}"]}. Notice that the data is all under the same string and not 1 array w/ 2 values. It also has open bracket (<) but not a closed one (>). This made it a little difficult when parsing the data in my code.*

Afterwards, I spent another 15-20 minutes trying to come up with a solution to the prompt. Throughout the coding process, I also continued to ask myself if the solution I came up with is actually addressing the prompt.

I spent around 2 hours writing the code, with little breaks here and there to make sure that I was actually solving the problem that was being asked.

So realistic breakdown of time spent is probably 10% understanding problem, 40% (trying to) think of solution, 50% writing code

## Setup
The only additional setup that is necessary is to install the pytz and tzlocal libraries, which I used in my location-timezone conversions. The **requirements.txt** file has the libraries that I installed during the coding process, but I ended up only using pytz and tzlocal.

## Run
To run the solution, ensure that necessary libaries are installed and simply run 
```
    python solution.py
```
from the **takehome-assignment** folder

## Solution
I wasn't able to implement a working solution in the allotted time, mainly because I was unsure of what it meant for a posting time to be 'optimal'. The one that I thought to go for was to return a list of datetime objects in order of 'optimization'. To me, optimization meant reaching the most followers. So the most optimal time is the one where I catered to the location(s) where most of my followers are located. For example, if most of my users are in the EST timezone, then I would post when those users are most active, sometime between 8 AM - 8 PM of that timezone. 

To make the outreach a little more optimal, the solution would 'average' the top 2 locations and then post at a time that average is sometime between 8 AM - 8 PM for that new 'timezone'. 
Example:
 - My current timezone is EST and I post at 10 AM. 
 - Most of my followers are located in Tokyo, which is +13 hours ahead of me (11 PM)
 - My second most followed location is Zurich, which is +6 hours ahead of me (4 PM)
 - I average those 2 times to get a new 'timezone'. In this case, the average is (13+6)/2 = +7.5 hours, which is 5:30 PM EST. Since this new time is between 8 AM - 8 PM, posting right now would be considered optimal.
 - A not optimal posting time would be 3 PM EST, which translates to 4 AM Tokyo time and 9 PM Zurich time. Then, the averaged time would be 10:30 PM, which is outside of the range where I consider users to be most active. In this case, I will add +12 hours to the current time and post then. Here, the new post/optimal time will be the next day 3 AM EST. 

## Code
Since I took a long time trying to figure out the solution, I didn't have time to implement as much as I would've liked. 

Since my solution revolves around finding the timezones that my followers are located in, I needed a way to translate the inputted user location into the timezones. That means first that I needed to extract the locations from the user data. That is the purpose of the **get_locations** function. It takes in the user data (which is manually loaded from the provided JSON file for this assignment), parses the location using **"".join(loc[0].split(", ")[1:])**, and then uses list comprehension + filtering to return a list of locations that are not None, since I can't get any timezones for a None value.

The **tz_to_time** is pretty simple. All it does is input a current datetime.datetime object along with a specified timezone and outputs the datetime.datetime object adjusted for the specified timezone.

## Incomplete Stuff
The biggest time waster for me on this assignment was trying to figure out how to implement **loc_to_timezone**, which would convert the user inputted locations into timezones that could be inputted into the **tz_to_time** function. I only way I could of think to implement this was to utilize an API where I can search for a location, receive (longitude, latitude) coordinates as an output, and then use those again as an input somewhere else to convert them into timezones. I think I wasted a lot of time trying to look for libraries that could help me, but I felt restricted because I didn't want to pay for any APIs. 

Since I couldn't find a way to bridge the gap between location -> timezone, I ended up with not enough time to implement an 'averaging' timezones function that the last paragraph in the Solutions section details.

One other feature that I thought would be cool was to redefine 'optimal' so that instead of posting content when most of my followers are awake, I post when my most active users are awake. For example, if most of my followers are in Tokyo, but my posts get the most interactions from users in Zurich, then maybe it makes more sense to post content to cater towards the Zurich followers instead of the Tokyo ones. This would take too much time though so I did not consider to try to implement it for the assignment.
