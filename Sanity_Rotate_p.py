"""
A testsuite for checking rotate image
"""

import os
import sys
import time

sys.path.append('../utils/')
from myutils import MyUtils


RES_OK = 0
RES_ERR = -1


class SanityTest:
    """ The test class object"""

    def __init__(self, utils):
        self.utils = utils
        self.jira = utils.jira
        self.logger = utils.logger
        self.env = utils.test_cfg['env']['env']
        self.bs1_cfg = utils.test_cfg['hub1']
        self.cam1_cfg = utils.test_cfg['device1']
        self.jira_cfg = utils.test_cfg['jira']
        self.path = os.path.dirname(os.path.abspath(__file__))
        self.run_num = 0

    def arloshc_t495_turn_on_rotate_image(self):
        """
        A test case function - Automate Sanity Test - Rotate Image
        """

        # defining tc
        tc = self.jira.testcase('ARLOSHC-T495', 'Turn on rotate image')
        # to check flip value on rotate
        # setting camera resource
        json_flip_on = {"action": "set", "properties": {"flip": True}, "resource": "cameras/" + self.cam1_cfg['sn']}
        result, data = self.utils.bs_api.shell.send_vz_cmd(json_flip_on)
        result, data = self.utils.check_4_string(str(data), '\'flip\': True')
        print(result, data)


        # save logs to csv file is required
        self.jira.save_results_csv(result, tc, data)

    def arloshc_t495_turn_off_rotate_image(self):
        """
        A test case function - Automate Sanity Test - Rotate Image
        """

        # defining tc
        tc = self.jira.testcase('ARLOSHC-T495', 'Turn off rotate image')

        # to check flip value off rotate

        json_flip_off = {"action": "set", "properties": {"flip": False}, "resource": "cameras/" + self.cam1_cfg['sn']}
        result, data = self.utils.bs_api.shell.send_vz_cmd(json_flip_off)
        result, data = self.utils.check_4_string(str(data), '\'flip\': False')

        # save logs to csv file
        self.jira.save_results_csv(result, tc, data)

    def save_logs(self):
        """ Saves all the logs into a zip file """
        bs_log_ok, bs_log_filename = self.utils.bs_api.get_systemlogs_tftp(timestamp=True)
        log_list = [bs_log_filename, 'Isp.log', 'Mcu.log']
        test_name = self.jira_cfg['test_title']
        self.utils.collect_logs(mypath, file_list=log_list, test_name=test_name, test_cycle=self.run_num)

    # delete the temp bs log
        if os.path.exists(bs_log_filename):
            os.remove(bs_log_filename)


if __name__ == '__main__':
    # the path to the test directory
    mypath = os.path.dirname(os.path.abspath(__file__))

    # log filename
    log_filename = 'sanity_test_rotate_image.log'

    # the MyUtils tools
    utils = MyUtils(log_filename, mypath)

    # the test class
    test = SanityTest(utils)
    test.arloshc_t481_turn_on_rotate_image()
    test.arloshc_t481_turn_off_rotate_image()
    test.save_logs()
    utils.logger.log_this('Main: See results.csv for list of results')
    
    # these are final changes made file, to merge.
