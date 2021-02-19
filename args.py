import argparse
from cml_api import CrystalMathLabsAPI
from temple_api import TempleOSRSAPI

def parse_args(args):
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--competition-id', help='Competition ID', required=True, type=int)
    parser.add_argument('-s', '--sleep-duration', help='How many seconds to wait between updates', required=False, default=60, type=int)

    competition_type_parser = parser.add_mutually_exclusive_group(required=False)

    competition_type_parser.add_argument('-t', '--temple', action='store_const', dest='api', const=lambda: TempleOSRSAPI(), help='Use the Temple OSRS API')
    competition_type_parser.add_argument('-c', '--crystal', action='store_const', dest='api', const=lambda: CrystalMathLabsAPI(), help='Use the Crystal Math Labs API')
    competition_type_parser.set_defaults(api=lambda: TempleOSRSAPI())
    return parser.parse_args(args)

