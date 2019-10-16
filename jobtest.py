import ats
import sys
from ats.easypy import run

def main():
	import argparse
	parser = argparse.ArgumentParser(usage="%(prog)s [options]", description="Job file test")
	parser.add_argument("--script", type=str, help="Script to execute", required=True)
	args, _ = parser.parse_known_args()

	if args.script == "testscript1":
		run(testscript="/local/ws1/production/tests/5d81def1cbd3495ddcef1e03/testscript1.py")
	elif args.script == "testscript2":
		run(testscript="/local/ws1/production/tests/5d81def1cbd3495ddcef1e03/testscript2.py")
	else:
		print("No such file")
		exit(1)
