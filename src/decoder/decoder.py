from src.decoder.decoded_data import EMSData, SystemData, ADAHRSData
from src.decoder.exceptions import InvalidDataException, InvalidDataTypeException


class SkyviewDataType:
    ADAHR = 'adahr'
    SYSTEM = 'system'
    EMS = 'ems'


class SkyviewDecoder:
    adahr_data = None
    system_data = None
    ems_data = None

    _ADAHR_STEP = [8,4,5,3,4,6,4,3,3,2,4,3,4,3,6,3,2,2]
    _SYSTEM_STEP = [8,3,5,4,4,3,1,1,2,3,3,1,1,1,1,1,3,5,1,3,5,1,3,5,1,1,1,4,10,2,2]
    _EMS_STEP = [8,3,4,4,4,3,3,3,3,3,3,3,3,3,4,5,5,4,4,4,4,4,4,4,4,4,4,4,4,4,4,6,6,6,6,6,6,6,6,6,6,6,6,6,16,3,1,2,2]

    def decode(self, data: str) -> ADAHRSData | SystemData | EMSData:
        if not data.startswith('!'):
            raise InvalidDataException

        try:
            data_type = int(data[1])     # 1=ADAHR / 2=SYSTEM / 3=EMS
            data_version = int(data[2])  # ADAHR=1 / SYSTEM=2 / EMS=2

            if data_type == 1 and data_version == 1:
                self.adahr_data = self.parse(data, SkyviewDataType.ADAHR)
                return self.adahr_data
            elif data_type == 2 and data_version == 2:
                self.system_data = self.parse(data, SkyviewDataType.SYSTEM)
                return self.system_data
            elif data_type == 3 and data_version == 2:
                self.ems_data = self.parse(data, SkyviewDataType.EMS)
                return self.ems_data
            else:
                raise InvalidDataException
        except ValueError:
            raise
            raise InvalidDataException

    def parse(self, data: str, data_type: str) -> ADAHRSData | SystemData | EMSData:
        if data_type == SkyviewDataType.ADAHR:
            step = self._ADAHR_STEP
        elif data_type == SkyviewDataType.SYSTEM:
            step = self._SYSTEM_STEP
        elif data_type == SkyviewDataType.EMS:
            step = self._EMS_STEP
        else:
            raise InvalidDataTypeException

        return self._post_parse(self._slicer(data[3:], step), data_type)

    def _slicer(self, data: str, step: list[int]) -> list[str]:
        offset = 0
        sliced_data = []

        for i in range(len(step)):
            this_step = step[i]
            this_data = data[offset:offset+this_step]
            offset += this_step
            sliced_data.append(this_data)

        return sliced_data

    def _post_parse(self, data: list[str], data_type: str) -> ADAHRSData | SystemData | EMSData:
        print(data)
        if data_type == SkyviewDataType.ADAHR:
            return self._map_adahr_data(data)
        elif data_type == SkyviewDataType.SYSTEM:
            return self._map_system_data(data)
        elif data_type == SkyviewDataType.EMS:
            return self._map_ems_data(data)
        else:
            raise InvalidDataTypeException

    def _parse_value(self, value: str, multiply: int | None = None, division: int | None = None):
        # Not available data
        if 'X' in value:
            return None

        # minus data
        if '-' in value:
            new_value = int(value.replace('-', ''))
            new_value *= -1
        # plus or else
        else:
            new_value = int(value.replace('+', ''))

        if multiply:
            new_value = float(new_value) * multiply
        if division:
            new_value = float(new_value) / division

        return new_value

    def _map_adahr_data(self, data: list[str]) -> ADAHRSData:
        return ADAHRSData(
            system_time=data[0],
            pitch=self._parse_value(data[1], division=10),
            roll=self._parse_value(data[2], division=10),
            mag_heading=self._parse_value(data[3]),
            ias=self._parse_value(data[4], division=10),
            pressure_alt=self._parse_value(data[5]),
            turn_rate=self._parse_value(data[6]),
            lateral_accel=self._parse_value(data[7], division=100),
            vertical_accel=self._parse_value(data[8], division=100),
            aoa=self._parse_value(data[9]),
            vertical_speed=self._parse_value(data[10]),
            oat=self._parse_value(data[11]),
            tas=self._parse_value(data[12], division=10),
            barometer_setting=self._parse_value(data[13], division=100) + 29.97,
            density_alt=self._parse_value(data[14]),
            wind_dir=self._parse_value(data[15]),
            wind_speed=self._parse_value(data[16]),
        )

    def _map_system_data(self, data: list[str]) -> SystemData:
        return SystemData(
            system_time=data[0],
            heading_bug=self._parse_value(data[1]),
            altitude_bug=self._parse_value(data[2], multiply=10),
            airspeed_bug=self._parse_value(data[3], division=10),
            vertical_speed_bug=self._parse_value(data[4], division=10),
            course=self._parse_value(data[5]),
            cdi_src_type=self._parse_value(data[6]),
            cdi_src_port=self._parse_value(data[7]),
            cdi_scale=self._parse_value(data[8], division=10),
            cdi_deflection=self._parse_value(data[9]),
            glide_slope=self._parse_value(data[10]),
            ap_engaged=self._parse_value(data[11]),
            ap_roll_mode=self._parse_value(data[12]),
            not_used_1=data[13],
            ap_roll_force=self._parse_value(data[14]),
            ap_roll_pos=self._parse_value(data[15]),
            ap_roll_slip=self._parse_value(data[16]),
            ap_pitch_force=self._parse_value(data[17]),
            ap_pitch_pos=self._parse_value(data[18]),
            ap_pitch_slip=self._parse_value(data[19]),
            ap_yaw_force=self._parse_value(data[20]),
            ap_yaw_pos=self._parse_value(data[21]),
            ap_yaw_slip=self._parse_value(data[22]),
            transponder_status=self._parse_value(data[23]),
            transponder_reply=self._parse_value(data[24]),
            transponder_code=data[25],
            not_used_2=data[26],
        )

    def _map_ems_data(self, data: list[str]) -> EMSData:
        return EMSData(
            system_time=data[0],
            oil_pressure=self._parse_value(data[1]),
            oil_temp=self._parse_value(data[2]),
            RPM_L=self._parse_value(data[3]),
            RPM_R=self._parse_value(data[4]),
            manifold_pressure=self._parse_value(data[5], division=10),
            fuel_flow_1=self._parse_value(data[6], division=10),
            fuel_flow_2=self._parse_value(data[7], division=10),
            fuel_pressure=self._parse_value(data[8], division=10),
            fuel_level_L=self._parse_value(data[9], division=10),
            fuel_level_R=self._parse_value(data[10], division=10),
            fuel_remaining=self._parse_value(data[11], division=10),
            volts_1=self._parse_value(data[12], division=10),
            volts_2=self._parse_value(data[13], division=10),
            amps=self._parse_value(data[14], division=10),
            hobbs_time=self._parse_value(data[15], division=10),
            tach_time=self._parse_value(data[16], division=10),
            thermocouple_1=self._parse_value(data[17]),
            thermocouple_2=self._parse_value(data[18]),
            thermocouple_3=self._parse_value(data[19]),
            thermocouple_4=self._parse_value(data[20]),
            thermocouple_5=self._parse_value(data[21]),
            thermocouple_6=self._parse_value(data[22]),
            thermocouple_7=self._parse_value(data[23]),
            thermocouple_8=self._parse_value(data[24]),
            thermocouple_9=self._parse_value(data[25]),
            thermocouple_10=self._parse_value(data[26]),
            thermocouple_11=self._parse_value(data[27]),
            thermocouple_12=self._parse_value(data[28]),
            thermocouple_13=self._parse_value(data[29]),
            thermocouple_14=self._parse_value(data[30]),
            gp_input_1=data[31],
            gp_input_2=data[32],
            gp_input_3=data[33],
            gp_input_4=data[34],
            gp_input_5=data[35],
            gp_input_6=data[36],
            gp_input_7=data[37],
            gp_input_8=data[38],
            gp_input_9=data[39],
            gp_input_10=data[40],
            gp_input_11=data[41],
            gp_input_12=data[42],
            gp_input_13=data[43],
            contacts=data[44],
            power_percent=self._parse_value(data[45]),
            egt_leaning_status=data[46],
        )