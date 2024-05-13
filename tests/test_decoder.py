from src.decoder import SkyviewDecoder, ADAHRSData, SystemData, EMSData

ADAHR_SAMPLE = "!1121144703-014+00003310811+01736+003-03+1013-033+110831245+01650023176C"
SYSTEM_SAMPLE = "!2221144704359XXXXX1600+010XXX00XXXXXXXX00X0X+00999900+00+99990+00XXXXX00104543XXXXXXXXXX3A"
EMS_SAMPLE = "!3221144705060+09323632363272057057164263263000280280+1200001300020+197+592+197+592+197+592+197+592+197+592+197+592+197+197+0012T+0013T+0001T+0164P+1990P+0928C+0001T+0000G+0263G+0263G+0599P+0928C+0928CZZZZZZZZZZZZZZZZ045L26"


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
