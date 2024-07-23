course_room_number = {'CSC101': '3004','CSC102':'4501','CSC103':'6755','NET110':'1244','COM241':'1411'}
course_instructor = {'CSC101': 'Haynes','CSC102':'Alvarado','CSC103':'Rich','NET110':'Burke','COM241':'Lee'}
course_meeting_time = {'CSC101': '8:00 a.m.','CSC102':'9:00 a.m.','CSC103':'10:00 a.m.','NET110':'11:00 a.m.','COM241':'1:00 p.m.'}
course_number = input('Enter the course number:')
if course_number in course_room_number:
    print(f'Course number: {course_number}; Course room number: {course_room_number[course_number]}; Course instructor: {course_instructor[course_number]}; Course meeting time: {course_meeting_time[course_number]}')
else:
    print('Course number not found')