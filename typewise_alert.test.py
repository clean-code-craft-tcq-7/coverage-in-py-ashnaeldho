import unittest
from typewise_alert import *
from breach_classifier import *
from breach_detecter import *
from stub_sender import StubSender
class TypewiseTest(unittest.TestCase):
  def test_check_and_alert(self):
    batteryChar = {}

    stubSender = StubSender()
    batteryChar['coolingType'] = 'PASSIVE_COOLING'
    alertTarget = 'TO_CONTROLLER'
    temperatureInC = -50
    # self.assertTrue(check_and_alert(alertTarget,batteryChar,temperatureInC) == True) 
    check_and_alert(alertTarget,batteryChar,temperatureInC,controllerFunctionPointer = stubSender.stub_send_to_controller)
    #Controller TOO_LOW


    batteryChar['coolingType'] = 'PASSIVE_COOLING'
    alertTarget = 'TO_EMAIL'
    temperatureInC = -50
    # self.assertTrue(check_and_alert(alertTarget,batteryChar,temperatureInC) == True) 
    check_and_alert(alertTarget,batteryChar,temperatureInC,emailFunctionPointer = stubSender.stub_send_to_email)
    #Email TOO_LOW


    batteryChar['coolingType'] = 'PASSIVE_COOLING'
    alertTarget = 'TO_CONTROLLER'
    temperatureInC = 50
    # self.assertTrue(check_and_alert(alertTarget,batteryChar,temperatureInC) == True) 
    check_and_alert(alertTarget,batteryChar,temperatureInC,controllerFunctionPointer = stubSender.stub_send_to_controller)
    #Controller TOO_HIGH

    batteryChar['coolingType'] = 'PASSIVE_COOLING'
    alertTarget = 'TO_EMAIL'
    temperatureInC = 50
    # self.assertTrue(check_and_alert(alertTarget,batteryChar,temperatureInC) == True) 
    check_and_alert(alertTarget,batteryChar,temperatureInC,emailFunctionPointer = stubSender.stub_send_to_email)
    #Email TOO_HIGH



    batteryChar['coolingType'] = 'PASSIVE_COOLING'
    alertTarget = 'TO_EMAIL'
    temperatureInC = 25
    # self.assertTrue(check_and_alert(alertTarget,batteryChar,temperatureInC) == False) 
    check_and_alert(alertTarget,batteryChar,temperatureInC,emailFunctionPointer = stubSender.stub_send_to_email)
    #Email Normal



    batteryChar['coolingType'] = 'HI_ACTIVE_COOLING'
    alertTarget = 'TO_CONTROLLER'
    temperatureInC = 0
    # self.assertTrue(check_and_alert(alertTarget,batteryChar,temperatureInC) == True) 
    check_and_alert(alertTarget,batteryChar,temperatureInC,controllerFunctionPointer = stubSender.stub_send_to_controller)
    #Controller Normal



    batteryChar['coolingType'] = 'HI_ACTIVE_COOLING'
    alertTarget = 'TO_EMAIL'
    temperatureInC = 45
    # self.assertTrue(check_and_alert(alertTarget,batteryChar,temperatureInC) == False) 
    check_and_alert(alertTarget,batteryChar,temperatureInC,emailFunctionPointer = stubSender.stub_send_to_email)
    #Email Normal


    batteryChar['coolingType'] = 'HI_ACTIVE_COOLING'
    alertTarget = 'TO_EMAIL'
    temperatureInC = 50
    # self.assertTrue(check_and_alert(alertTarget,batteryChar,temperatureInC) == True) 
    check_and_alert(alertTarget,batteryChar,temperatureInC,emailFunctionPointer = stubSender.stub_send_to_email)
    #Email TOO_HIGH


    batteryChar['coolingType'] = 'MED_ACTIVE_COOLING'
    alertTarget = 'TO_CONTROLLER'
    temperatureInC = 0
    # self.assertTrue(check_and_alert(alertTarget,batteryChar,temperatureInC) == True) 
    check_and_alert(alertTarget,batteryChar,temperatureInC,controllerFunctionPointer = stubSender.stub_send_to_controller)
    #Controller Normal


    batteryChar['coolingType'] = 'MED_ACTIVE_COOLING'
    alertTarget = 'TO_EMAIL'
    temperatureInC = 45
    # self.assertTrue(check_and_alert(alertTarget,batteryChar,temperatureInC) == True) 
    check_and_alert(alertTarget,batteryChar,temperatureInC,emailFunctionPointer = stubSender.stub_send_to_email)
    #Email TOO_HIGH


    batteryChar['coolingType'] = 'MED_ACTIVE_COOLING'
    alertTarget = 'TO_EMAIL'
    temperatureInC = 20
    # self.assertTrue(check_and_alert(alertTarget,batteryChar,temperatureInC) == False) 
    check_and_alert(alertTarget,batteryChar,temperatureInC,emailFunctionPointer = stubSender.stub_send_to_email)
    #Email Normal

    batteryChar['coolingType'] = 'HI_ACTIVE_COOLING'
    alertTarget = 'TO_SMS'
    temperatureInC = 50
    self.assertTrue(check_and_alert(alertTarget,batteryChar,temperatureInC) == None) 

    self.assertTrue(stubSender.controllerCounter['TOO_LOW']==1) 
    self.assertTrue(stubSender.controllerCounter['TOO_HIGH']==1) 
    self.assertTrue(stubSender.controllerCounter['NORMAL']==2) 
    self.assertTrue(stubSender.emailCounter['TOO_LOW']==1) 
    self.assertTrue(stubSender.emailCounter['TOO_HIGH']==3) 
    # self.assertTrue(stubSender.emailCounter['NORMAL']==3) 
    self.assertTrue(stubSender.emailCounter['NORMAL']==0) 
  def test_infers_and_limits_as_per_cooling_type(self):
    self.assertTrue(classify_temperature_breach('PASSIVE_COOLING',100) == 'TOO_HIGH')
    self.assertTrue(classify_temperature_breach('PASSIVE_COOLING',36) == 'TOO_HIGH')
    self.assertTrue(classify_temperature_breach('PASSIVE_COOLING',35.1) == 'TOO_HIGH')
    self.assertTrue(classify_temperature_breach('PASSIVE_COOLING',35) == 'NORMAL') 
    self.assertTrue(classify_temperature_breach('PASSIVE_COOLING',25) == 'NORMAL') 
    self.assertTrue(classify_temperature_breach('PASSIVE_COOLING',0) == 'NORMAL') 
    self.assertTrue(classify_temperature_breach('PASSIVE_COOLING',-0.01) == 'TOO_LOW') 
    self.assertTrue(classify_temperature_breach('PASSIVE_COOLING',-1) == 'TOO_LOW') 
    self.assertTrue(classify_temperature_breach('PASSIVE_COOLING',-25) == 'TOO_LOW') 

    self.assertTrue(classify_temperature_breach('HI_ACTIVE_COOLING',100) == 'TOO_HIGH')
    self.assertTrue(classify_temperature_breach('HI_ACTIVE_COOLING',46) == 'TOO_HIGH')
    self.assertTrue(classify_temperature_breach('HI_ACTIVE_COOLING',45.1) == 'TOO_HIGH')
    self.assertTrue(classify_temperature_breach('HI_ACTIVE_COOLING',45) == 'NORMAL') 
    self.assertTrue(classify_temperature_breach('HI_ACTIVE_COOLING',25) == 'NORMAL') 
    self.assertTrue(classify_temperature_breach('HI_ACTIVE_COOLING',0) == 'NORMAL') 
    self.assertTrue(classify_temperature_breach('HI_ACTIVE_COOLING',-0.01) == 'TOO_LOW') 
    self.assertTrue(classify_temperature_breach('HI_ACTIVE_COOLING',-1) == 'TOO_LOW') 
    self.assertTrue(classify_temperature_breach('HI_ACTIVE_COOLING',-25) == 'TOO_LOW') 

    self.assertTrue(classify_temperature_breach('MED_ACTIVE_COOLING',100) == 'TOO_HIGH')
    self.assertTrue(classify_temperature_breach('MED_ACTIVE_COOLING',46) == 'TOO_HIGH')
    self.assertTrue(classify_temperature_breach('MED_ACTIVE_COOLING',40.1) == 'TOO_HIGH')
    self.assertTrue(classify_temperature_breach('MED_ACTIVE_COOLING',40) == 'NORMAL') 
    self.assertTrue(classify_temperature_breach('MED_ACTIVE_COOLING',25) == 'NORMAL') 
    self.assertTrue(classify_temperature_breach('MED_ACTIVE_COOLING',0) == 'NORMAL') 
    self.assertTrue(classify_temperature_breach('MED_ACTIVE_COOLING',-0.01) == 'TOO_LOW') 
    self.assertTrue(classify_temperature_breach('MED_ACTIVE_COOLING',-1) == 'TOO_LOW') 
    self.assertTrue(classify_temperature_breach('MED_ACTIVE_COOLING',-25) == 'TOO_LOW')
    
    self.assertTrue(classify_temperature_breach('None',-25) == 'TOO_LOW') 
    self.assertTrue(classify_temperature_breach('None',25) == 'TOO_HIGH') 
    self.assertTrue(classify_temperature_breach('None',0) == 'NORMAL') 

  def test_infers_breach_as_per_limits(self):
    self.assertTrue(infer_breach(20, 50, 100) == 'TOO_LOW')
    self.assertTrue(infer_breach(2, 3, 5) == 'TOO_LOW')
    self.assertTrue(infer_breach(4, 1, 10) == 'NORMAL')
    self.assertTrue(infer_breach(-4, -100, -2) == 'NORMAL')
    self.assertTrue(infer_breach(0.4, 0.1, 1.0) == 'NORMAL')
    self.assertTrue(infer_breach(1.2, 0.1, 1.0) == 'TOO_HIGH')
    self.assertTrue(infer_breach(0.02, 0.1, 1.0) == 'TOO_LOW')


if __name__ == '__main__':
  unittest.main()
