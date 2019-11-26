#!/usr/bin/env python

from main import *
import sys
n = int(sys.argv[1])

with open('hospital.sql', 'a+') as f:
    for i in range(n):
        camera_number = fake.random_int(min=1, max=50)
        date = fake.date_this_month(before_today=True, after_today=False)
        print("INSERT INTO Video_Record(Date, Path, Camera_number) VALUES(" + wrap(date) + " , '/dev/hospital/video_records/" + str(date) + "/" + fake.file_name(extension="avi") + "' , " + str(camera_number) + " );", file=f)

with open('hospital_mysql.sql', 'a+') as f:
    for i in range(n):
        camera_number = fake.random_int(min=1, max=50)
        date = fake.date_this_month(before_today=True, after_today=False)
        print("INSERT INTO Video_Record(Date, Path, Camera_number) VALUES(" + wrap(date) + " , '/dev/hospital/video_records/" + str(date) + "/" + fake.file_name(extension="avi") + "' , " + str(camera_number) + " );", file=f)