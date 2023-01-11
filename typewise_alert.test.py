import unittest
import typewise_alert


class TypewiseTest(unittest.TestCase):
  def test_infers_breach_as_per_limits(self):
      #PASSIVE_COOLING_TEST
    self.assertTrue(typewise_alert.infer_breach(0, 0, 35) == 'NORMAL')
    self.assertEqual(typewise_alert.infer_breach(35, 0, 35) , 'NORMAL')
    self.assertEqual(typewise_alert.infer_breach(-1, 0, 35) , 'TOO_LOW')
    self.assertEqual(typewise_alert.infer_breach(1, 0, 35) , 'NORMAL')
    self.assertEqual(typewise_alert.infer_breach(34, 0, 35) , 'NORMAL')
    self.assertEqual(typewise_alert.infer_breach(36, 0, 35), 'TOO_HIGH')
    #HI_ACTIVE_COOLING_TEST
    self.assertTrue(typewise_alert.infer_breach(0, 0, 45) == 'NORMAL')
    self.assertTrue(typewise_alert.infer_breach(45, 0, 45) == 'NORMAL')
    self.assertTrue(typewise_alert.infer_breach(-1, 0, 45) == 'TOO_LOW')
    self.assertTrue(typewise_alert.infer_breach(1, 0, 45) == 'NORMAL')
    self.assertTrue(typewise_alert.infer_breach(44, 0, 45) == 'NORMAL')
    self.assertTrue(typewise_alert.infer_breach(46, 0, 45) == 'TOO_HIGH')
    #MED_ACTIVE_COOLING_TEST
    self.assertTrue(typewise_alert.infer_breach(0, 0, 40) == 'NORMAL')
    self.assertTrue(typewise_alert.infer_breach(40, 0, 40) == 'NORMAL')
    self.assertTrue(typewise_alert.infer_breach(-1, 0, 40) == 'TOO_LOW')
    self.assertTrue(typewise_alert.infer_breach(1, 0, 40) == 'NORMAL')
    self.assertTrue(typewise_alert.infer_breach(39, 0, 40) == 'NORMAL')
    self.assertTrue(typewise_alert.infer_breach(41, 0, 40) == 'TOO_HIGH')
    
    #SEND_ALERTS TEST
    batteryChar = {'coolingType' : 'PASSIVE_COOLING'}
    self.assertTrue(typewise_alert.check_and_alert('TO_CONTROLLER', batteryChar, 1) == 1)
    self.assertTrue(typewise_alert.check_and_alert('TO_EMAIL', batteryChar, -1) == 1)
    self.assertTrue(typewise_alert.check_and_alert('TO_EMAIL', batteryChar, 36) == 1)
    self.assertTrue(typewise_alert.check_and_alert('TO_EMAIL', batteryChar, 1) == 0)
    self.assertTrue(typewise_alert.check_and_alert('TO_EMAIL', batteryChar, 34) == 0)


if __name__ == '__main__':
  unittest.main()
