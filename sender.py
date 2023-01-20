from configuration import *
from printer import *

def send_to_controller(breachType):
  print_send_controller(header,breachType)


def send_to_email(breachType):  
  if breachType == 'TOO_LOW':
    print_send_email(recepient,'too low')

  elif breachType == 'TOO_HIGH':
    print_send_email(recepient,'too high')
