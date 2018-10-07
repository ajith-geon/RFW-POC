# =====================================================================================
#    Filename   :  ElementLocators_prism.py
#
#    Description:  This file contains the element locators identified for PRiSM
#
#    Version    :  1.0
#    Created    :  10/04/2018
#    Compiler   :  python
#    Author     :
#    Company    :
#
#    Revision History:
#
# =====================================================================================

######################################################################
# Page Name : PRiSM Login Page
# comment :  PRiSM Login Page
#######################################################################
Username_Xpath='//input[@id="ctl00_LoginContent_LoginView1_LoginControl_UserName"]'
Password_Xpath='//input[@id="ctl00_LoginContent_LoginView1_LoginControl_Password"]'
Login_Button='//input[@id="ctl00_LoginContent_LoginView1_LoginControl_LoginButton"]'
Eula_Accept_Button='//input[@id="AgreeButton"]'

######################################################################
# Page Name : PRiSM Home Page
# comment :  PRiSM Home Page
#######################################################################
Glass_Invitation='//div[@id="ctl00_RightPlaceHolder_TryNewDashboard"]'
Add_Widget_PlaceHolder='//div[@class="widget-add-tile widget-tile-flex text-center"]'

######################################################################
# Page Name : Glass Dashboard Page
# comment :  Glass Dashboard Page
#######################################################################
Add_Widget_Button='//button[@class="mat-raised-button mat-primary"]'
Default_Toggle_Button='//div[@class="mat-slide-toggle-thumb"]'
ReturnToOld_Button='//div[@class="back-panel pull-left"]/i'