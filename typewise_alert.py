
from sender import *
from breach_detecter import *
from breach_classifier import *

def check_and_alert(alertTarget, batteryChar, temperatureInC,controllerFunctionPointer=send_to_controller,emailFunctionPointer=send_to_email):
  breachType =\
    classify_temperature_breach(batteryChar['coolingType'], temperatureInC)
  if alertTarget == 'TO_CONTROLLER':
    controllerFunctionPointer(breachType)
  elif alertTarget == 'TO_EMAIL':
    emailFunctionPointer(breachType)
