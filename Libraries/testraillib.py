# =====================================================================================
#    Filename   :  testraillib.py
#    Description:
#    Version    :  1.0
#    Created    :  10/04/2018
#    Compiler   :  python
#    Author     :
#    Company    :
#
#    Revision History:
#
# =====================================================================================
#!/usr/bin/env python
from testrail import *
import json
import os.path
import tempfile
import time
from subprocess import check_output
from optparse import OptionParser
import subprocess
import sys
######################################################################
# Func Name : get_runid
# Args : planid,config (optional)
#
# returns : Run details
######################################################################	
def get_runid(planid, testrail_url, testrail_user, testrail_password,config_value = None):
	client = APIClient(testrail_url)
	client.user = testrail_user
	client.password = testrail_password
	runidurl = 'get_plan/' + str(planid)
	runids = client.send_get(runidurl)
	runs ={}
	entries = runids ['entries']
	entry = entries[0]
	for run in entry ['runs']:
		config = run ['config']
		runs [config] = run ['id']
	return runs [config_value] 
######################################################################
# Func Name : get_planid
# Args : planid,config (optional)
#
# returns : plan id
######################################################################	
def get_planid(planName, projectid, testrail_url, testrail_user, testrail_password):
    client = APIClient(testrail_url)
    client.user = testrail_user
    client.password = testrail_password
    planidurl = 'get_plans/' + str(projectid)	
    planids = client.send_get(planidurl)
    print ("Plans : %s" %planids)
    for plan in planids:
	    if plan ['name'] == planName:
		    planid = plan ['id']
		    break
	    else:
		    planid = 'none'
    print ("Planid : %s" %planid)
    return planid
######################################################################
# Func Name : get_projectid
# Args : planid,config (optional)
#
# returns : Run details
######################################################################	
def get_projectid(projectName, testrail_url, testrail_user, testrail_password):
    client = APIClient(testrail_url)
    client.user = testrail_user
    client.password = testrail_password
    projectid = client.send_get('get_projects')
    print ("Projeccts : %s" %projectid)
    for project in projectid:
	    if project ['name'] == projectName:
		    projectid = project ['id']
		    break
	    else:
		    projectid = 'none'
    return projectid
######################################################################
# Func Name : update_result
# Args : planid,config (optional)
#
# returns : Run details
######################################################################	
def update_result(runid,caseid,status,comments, testrail_url, testrail_user, testrail_password):
	client = APIClient(testrail_url)
	client.user = testrail_user
	client.password = testrail_password
	if status == 'PASS':
		statusid = '1'
	elif status == 'BLOCKED':
		statusid = '2'
	else:
		statusid = '5'
	updateresulturl = 'add_result_for_case/' + str(runid) + '/' + str(caseid)
	tesresult = client.send_post(updateresulturl,
    	{'status_id': statusid, 'comment': comments})
	print ("%s" %tesresult)
######################################################################
# Func Name : get_automationids
# Args : runid,testrail username, testrail password, testrail url. config (optional)#
# returns : Run details
######################################################################
def get_automationids(runid, testrail_url, testrail_user, testrail_password, config = None):
	autoidlist ={}
	client = APIClient(testrail_url)
	client.user = testrail_user
	client.password = testrail_password
	retrivecaseidsuri = 'get_tests/' + str(runid)
	caseids = client.send_get(retrivecaseidsuri)
	for testcases in caseids:
		autoidlist [str(testcases["custom_automation_id"])] = str(testcases["case_id"])
	return autoidlist