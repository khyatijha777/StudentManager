from django.shortcuts import render

# Create your views here.
def todays_attendance(req):
    return render(req, 'attendance/todays_attendance.html')