'''
Created on Jun 24, 2016

@author: Waqas Ali
'''

import pymysql, json, sys 
from django.http import HttpResponse 
from rest_framework.decorators import api_view
from pythondbhelper.dbhelper import dbhelper
from CB_Core.dbConnection import *

@api_view(['GET'])
def GetAllStudents(request):    
    try:       
        helper = dbhelper(host, port, user, passwd, db)    
        dt = helper.fetchAll("Select s.Id, s.FirstName, s.LastName, s.Age, s.Gender, c.ClassName From Student as s INNER JOIN class as c ON s.classid = c.id")
        res=json.dumps(dt)           
    except:
        res = str(sys.exc_info()[1])
    
    print(res)
    return HttpResponse(res) 


def AddNewStudent(newStudent):    
    try:        
        helper = dbhelper(host, port, user, passwd, db)
        qry_insert = "INSERT INTO Student(FirstName, LastName, Age, Gender, ClassId) VALUES ('{0}', '{1}', {2}, '{3}', {4})".format(newStudent._FirstName, newStudent._LastName, newStudent._Age, newStudent._Gender, newStudent._ClassId)
        helper.insertRecord(qry_insert)                                
        res = 'Student Added successfully!'            
    except:
        res = str(sys.exc_info()[1])    
        
    return HttpResponse(res)
