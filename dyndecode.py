
from src.decoder import SkyviewDecoder, D1x0Decoder, ADAHRSData, SystemData, EMSData, D1x0EFISData, D1x0EMSData

ADAHR_SAMPLE = "!1121144703-014+00003310811+01736+003-03+1013-033+110831245+01650023176C"
SYSTEM_SAMPLE = "!2221144704359XXXXX1600+010XXX00XXXXXXXX00X0X+00999900+00+99990+00XXXXX00104543XXXXXXXXXX3A"
EMS_SAMPLE = "!3221144705060+09323632363272057057164263263000280280+1200001300020+197+592+197+592+197+592+197+592+197+592+197+592+197+197+0012T+0013T+0001T+0164P+1990P+0928C+0001T+0000G+0263G+0263G+0599P+0928C+0928CZZZZZZZZZZZZZZZZ045L26"
D1x0_EFIS_SAMPLE = "00082119+058-00541301200+9141+011-01+15003EA0C701A4"
#D1x0_EMS_SAMPLE= "0012224826351340262441240122631320562191191OAT00090TRE-0061FLP0001020481378139214061421143514503583533633743843951103D2"
D1x0_EMS_SAMPLE= "1345060330751460580351330051190280119080096TRE-0025TRA00024OAT-004600190855092909160932090809271731631881741871711103B0"
class TestDecoder:
    def test_slicer(self):
        data = "12345678910"
        step = [1,2,3,1,1,2,1]

        result = SkyviewDecoder()._slicer(data, step)

        assert result[0] == '1'
        assert result[1] == '23'
        assert result[2] == '456'
        assert result[3] == '7'
        assert result[4] == '8'
        assert result[5] == '91'
        assert result[6] == '0'

    def test_adahr_data_decode(self):
        result = SkyviewDecoder().decode(ADAHR_SAMPLE)

        assert type(result) is ADAHRSData

    def test_system_data_decode(self):
        result = SkyviewDecoder().decode(SYSTEM_SAMPLE)

        assert type(result) is SystemData

    def test_ems_data_decode(self):
        result = SkyviewDecoder().decode(EMS_SAMPLE)

        assert type(result) is EMSData

    def test_d1x0_efis_data_decode(self):
        result = D1x0Decoder().decode(D1x0_EFIS_SAMPLE)

        assert type(result) is D1x0EFISData
#        print( D1x0Decoder().output_CSV_line(D1x0_EFIS_SAMPLE))
        assert D1x0Decoder()._is_valid_efis_data(D1x0_EFIS_SAMPLE) == True

    def test_d1x0_ems_data_decode(self):
        result = D1x0Decoder().decode(D1x0_EMS_SAMPLE)

        assert type(result) is D1x0EMSData
#        print( D1x0Decoder().output_CSV_header(D1x0_EMS_SAMPLE))
#        print( D1x0Decoder().output_CSV_line(D1x0_EMS_SAMPLE))
        assert D1x0Decoder()._is_valid_ems_data(D1x0_EMS_SAMPLE) == True

        D1x0Decoder().translate("test_ems_data3.txt")

#x = TestDecoder()
#x.test_slicer()
#x.test_ems_data_decode()
#x.test_adahr_data_decode()
#x.test_system_data_decode()
#x.test_d1x0_efis_data_decode()
#x.test_d1x0_ems_data_decode()


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
    D1x0Decoder().translate(args.infile)



    