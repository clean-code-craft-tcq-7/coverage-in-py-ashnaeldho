
from limits import LIMITS
from send_alerts import send_to_controller, send_to_email


def infer_breach(value, lowerLimit, upperLimit):
  if value < lowerLimit:
    return 'TOO_LOW'
  if value > upperLimit:
    return 'TOO_HIGH'
  return 'NORMAL'



def check_and_alert(alertTarget, batteryChar, temperatureInC):
  Flg = 0
  lowerlimit, upperlimit = LIMITS[batteryChar['coolingType']]
  breachType =\
    infer_breach(temperatureInC, lowerlimit, upperlimit)
  if alertTarget == 'TO_CONTROLLER':
    Flg= send_to_controller(breachType)
    return Flg
  elif alertTarget == 'TO_EMAIL':
    Flg= send_to_email(breachType)
    return Flg
