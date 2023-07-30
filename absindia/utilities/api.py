# Copyright (c) 2023, Baaridun Nasr and contributors
# For license information, please see license.txt

import datetime

import frappe
from frappe.utils import getdate, today, add_to_date

@frappe.whitelist()
def getCurrentEmployeeNo():
    '''
    get current employee no from the current session user
    '''
    return frappe.db.get_value('Employee', {'user_id': frappe.session.user}, 'name')

@frappe.whitelist()
def getCurrentYear():
    '''
    get the current year from today
    '''
    return getdate(today()).isocalendar()[0]

@frappe.whitelist()
def getCurrentWeekNo():
    '''
    get the current week number from today
    '''
    return getdate(today()).isocalendar()[1]

@frappe.whitelist()
def getWeekNo(curTime):
    '''
    get the week number of the specified datetime
    '''
    return getdate(curTime).isocalendar()[1]

@frappe.whitelist()
def getTimeDiffInHrs(time2, time1):
    '''
    get the time difference between two input datetimes in hours
    '''
    if len(time1)>19:
        time1=time1[:-7]
    if len(time2)>19:
        time2=time2[:-7]
    fromTime = datetime.datetime.strptime(time1, '%Y-%m-%d %H:%M:%S')
    toTime = datetime.datetime.strptime(time2, '%Y-%m-%d %H:%M:%S')
    return (((toTime - fromTime).seconds)/3600)


@frappe.whitelist()
def getTimeDiffInDays(time2, time1):
    '''
    get the time difference between two input datetimes in days
    '''
    fromDate = getdate(time1)
    toDate = getdate(time2)
    return (toDate - fromDate).days

def getWeekStartDate(time1):
    '''
    get week start date of the given datetime
    '''
    weekDay = datetime.datetime.strptime(time1, '%Y-%m-%d').weekday()
    return(add_to_date(time1, days=(-1*(weekDay)), as_string=True))
    pass

def getWeekEndDate(time1):
    '''
    get week end date of the given datetime
    '''
    weekDay = datetime.datetime.strptime(time1, '%Y-%m-%d').weekday()
    return(add_to_date(time1, days=(6-(weekDay)), as_string=True))
    pass

@frappe.whitelist()
def inCurrentWeek(time1):
    '''
    check if the given datetime is in the current week
    '''
    return (getCurrentWeekNo() == getWeekNo(str(time1)))