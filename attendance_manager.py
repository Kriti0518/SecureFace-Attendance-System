import csv
import os
from datetime import datetime


def mark_attendance(name):

    file_exists = os.path.isfile("attendance_records.csv")

    with open("attendance_records.csv", "a", newline="") as file:

        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(["Name", "Date", "Time"])

        now = datetime.now()

        writer.writerow([
            name,
            now.strftime("%Y-%m-%d"),
            now.strftime("%H:%M:%S")
        ])

        print("Attendance Marked Successfully")


def view_attendance_log():

    try:

        with open("attendance_records.csv", "r") as file:

            print(file.read())

    except FileNotFoundError:

        print("No attendance records found.")