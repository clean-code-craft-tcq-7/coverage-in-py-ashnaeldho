class StubSender:
  def __init__(self):
    self.controllerCounter={'TOO_LOW':0,
                            'TOO_HIGH':0,
                            'NORMAL':0}

    self.emailCounter={'TOO_LOW':0,
                        'TOO_HIGH':0,
                        'NORMAL':0}


  def stub_send_to_controller(self,breachType):
    self.controllerCounter[breachType] += 1

  def stub_send_to_email(self,breachType):
    if (breachType == 'TOO_LOW') or (breachType == 'TOO_HIGH'):
      self.emailCounter[breachType] += 1
