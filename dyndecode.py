
from src.decoder.decoder import Decoder

if __name__ == '__main__':
    import argparse
    import sys

    parser = argparse.ArgumentParser(
        prog='DynonParser',
        description='Check & convert Dynon serial data to CSV format',
        epilog='Coverts Dynon D1x0 EFIS or EMS data & Skyview ADAHRS, System & EFIS data')
    parser.add_argument('infile', nargs='?', type=argparse.FileType('r'),
                    default=sys.stdin)
    parser.add_argument('outfile', nargs='?', type=argparse.FileType('w'),
                    default=sys.stdout)
    parser.add_argument("-q", "--quiet",
                    action="store_false", dest="verbose", default=True,
                    help="don't print status messages to stdout")

    args = parser.parse_args()
    Decoder().translate(args.infile)



    