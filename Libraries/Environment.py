
# =====================================================================================
#    Filename   :  Environment.py
#    Description: Common Functions for Setting Up the Environment and Manipulating Global Variables
#    Version    :  1.0
#    Created    :  10/04/2018
#    Compiler   :  python
#    Author     :
#    Company    :
#
#    Revision History:
#
# =====================================================================================

import os.path
import datetime
import time
import sys
sys.path.append('../')
import Testdata_web


#############################################################################
# Func Name : company_override
# Args : None
# Description : Overrides the Company Name being provided in the TestData.txt
#############################################################################
def COMPANY_OVERRIDE():
    ts = time.time()
    timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d%H%M%S')
    Testdata_web.Username='qa'+timestamp
    Testdata_web.Password='qa'+timestamp
    Testdata_web.Login_Confirm_Message=u"Welcome, "+'qa'+timestamp
    return('qa'+timestamp)
