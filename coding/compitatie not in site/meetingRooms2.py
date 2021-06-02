# https://www.youtube.com/watch?v=kZfHnsrQcP0

# determine no of meeting rooms required (least)

# the meeting which have to be start first determined by the ascending order of the starting time
# either new room needed or older room re occupied will be determined by the ending time of the meeting

import heapq

meeting_schedule = [[0,30],[15,20],[5,10]]

meeting_schedule = [[x[1],x[0]] for x in meeting_schedule] # [e,s]

meeting_schedule.sort(key = lambda x:x[1])

meeting_rooms = []  #[ending, starting]

heapq.heapify(meeting_rooms)

heapq.heappush(meeting_rooms,meeting_schedule[0])

print(meeting_rooms)

for i in range(1,len(meeting_schedule)):
	current = meeting_schedule[i] # [e,s]
	running = meeting_rooms[0] # [e,s]

	if running[0] > current[1]:
		heapq.heappush(meeting_rooms,current)
	else:
		heapq.heappop(meeting_rooms)
		heapq.heappush(meeting_rooms,[current[0],running[1]])


print(len(meeting_rooms))

print(meeting_rooms)

