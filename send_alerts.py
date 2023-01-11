def send_to_controller(breachType): 
  header = 0xfeed
  print(f'{header}, {breachType}')
  FLAG_SEND_TO_CONTROLLER = 1
  return FLAG_SEND_TO_CONTROLLER


def send_to_email(breachType):
  FLAG_SEND_TO_EMAIL = 0 
  recepient = "a.b@c.com"
  if breachType == 'TOO_LOW':
    print(f'To: {recepient}')
    print('Hi, the temperature is too low')
    FLAG_SEND_TO_EMAIL = 1
    return FLAG_SEND_TO_EMAIL
  elif breachType == 'TOO_HIGH':
    print(f'To: {recepient}')
    print('Hi, the temperature is too high')
    FLAG_SEND_TO_EMAIL = 1
    return FLAG_SEND_TO_EMAIL
  return 
