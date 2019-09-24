from ats import aetest
import logging


class ScriptCommonSetup(aetest.CommonSetup):

	@aetest.subsection
	def check_script_arguments(self):
		
		import argparse
		parser = argparse.ArgumentParser(usage="%(prog)s [options]", description="Greets the user")
		parser.add_argument("--name", dest="name", type=str, help="Name to display greeting", required=True)
		args, _ = parser.parse_known_args()
		self.parent.parameters.update(name=args.name)
		pass


class FirstTestcase(aetest.Testcase):

	@aetest.test
	def print_greeting(self, name):
		logging.info(50*"-"+"> Hello {}!".format(name))


class SecondTestcase(aetest.Testcase):

	@aetest.test
	def print_name_caps_before(self, name):
		self.parent.parameters.update(name=name.upper())
		logging.info(50*"-"+"> {}".format(name))

	@aetest.test
	def print_name_caps_after(self, name):
		self.parent.parameters.update(name=name.lower())
		logging.info(50*"-"+"> {}".format(name))


class ThirdTestcase(aetest.Testcase):

	@aetest.test
	def print_name(self, name):
		logging.info(50*"-"+"> {}".format(name))


class ScriptCommonCleanup(aetest.CommonCleanup):

	@aetest.subsection
	def remove_testbed_configurations(self):
		pass


if __name__ == '__main__':
	aetest.main()
