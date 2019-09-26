from ats import aetest
import logging


class ScriptCommonSetup(aetest.CommonSetup):

	@aetest.subsection
	def check_script_arguments(self):
		pass

	@aetest.subsection
	def connect_to_devices(self):
		pass

	@aetest.subsection
	def configure_interfaces(self):
		pass


class FirstTestcase(aetest.Testcase):

	@aetest.test
	def print_hello(self):
		logging.info("Hello\t__CIMTESTDIR__")


class ScriptCommonCleanup(aetest.CommonCleanup):

	@aetest.subsection
	def remove_testbed_configurations(self):
		pass

	@aetest.subsection
	def disconnect_from_devices(self):
		pass


if __name__ == '__main__':
	aetest.main()
