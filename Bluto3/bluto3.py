#!/usr/bin/python

import argparse
import traceback
from termcolor import colored
from modules.resolve import main as resolve_dns
from modules import execute
from modules import descriptor_
from modules.use_age import debug_out

parser = argparse.ArgumentParser(prog='Bluto', formatter_class=lambda prog: argparse.RawDescriptionHelpFormatter(prog,max_help_position=50), usage=descriptor_.des())

requiredNamed = parser.add_argument_group('Required Arguments')
requiredNamed.add_argument('-d', '--domain', help='Target Domain', required=True)

parser.add_argument('-e', '--email', help='Enable Email Enumeration', required=False, action='store_true')
parser.add_argument('-a', '--api', help='Hunter API key', required=False)
parser.add_argument('--debug', help=argparse.SUPPRESS, required=False, action='store_true')

zn_group = parser.add_argument_group('DNS Arguments', 'Specify what DNS related checks you want to carry out')
zn_group.add_argument('-b', '--brute', help='Enable SubDomain bruteforcing', required=False, action='store_true')
zn_group.add_argument('-z', '--zone', help='Enable ZoneTransfer Checks', required=False, action='store_true')
zn_group.add_argument('-dns', '--dns', help='Carry out DNS enumeration', required=False, action='store_true')
zn_group.add_argument('-i', '--intrusive', help='Carrys out DNS queries on Authoritive', required=False, action='store_true')
zn_group.add_argument('-t', '--timeo', help='Set timeout value | Default 5', required=False)
zn_group.add_argument('-ts', '--top', help='Most popular subdomains eg. Top1000', required=False)

args = parser.parse_args()
if __name__ == "__main__":

	if args.debug:
		print colored('Debug Enabled:','red', 'on_yellow')
		print colored('Arg Output', 'red', 'on_yellow')
		debug_out(args.__dict__)
	try:
		if args.dns is False and args.brute is False and args.zone is False:
			resolve_dns(args)
			execute._brute(args)
		else:

			if args.dns:
				resolve_dns(args)
			if args.brute is False and args.zone is True:
				execute.zone_trans(args)
			if args.brute:
				execute._brute(args)
			if (args.api) or (args.email):
				'placeholder'

	except Exception:
		print traceback.print_exc()
	except KeyboardInterrupt:
		print '\n\nRage Quit!!'
