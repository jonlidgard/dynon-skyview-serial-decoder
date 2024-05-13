from dataclasses import dataclass
from datetime import datetime


# deg = 0-359


@dataclass
class ADAHRSData:
    system_time: str  # HHMMSSFF
    pitch: float  # unit: deg / n * 10 / positive = pitch up / XXXX is unavailable
    roll: float  # unit: deg / n * 10 / positive = right bank / XXXXX
    mag_heading: int  # unit: deg / XXX
    ias: float  # IAS / unit: knots / n * 10 / XXXX
    pressure_alt: int  # unit : feet / at 29.92Hg / can be minus (sea level) / XXXXXX
    turn_rate: int  # unit: deg / XXXX
    lateral_accel: float  # unit: g / n * 100 / positive = left skid (ball right) / XXX
    vertical_accel: float  # unit: g / n * 100 / positive = going up accel / XXX
    aoa: int  # AOA / unit: % / XX
    vertical_speed: int  # unit: ft/min / positive = climbing / XXX(4)
    oat: int  # OAT(Outside Air Temperature) / unit: deg celcius / XXX
    tas: float  # TAS / unit: knot / n * 10 / XXXX
    barometer_setting: float  # Barometer setting / unit: inHg / n * 100 / offset from 27.50 / XXX
    density_alt: int  # unit: feet / positive = above set level / XXXXXX
    wind_dir: int  # unit: deg / XXX
    wind_speed: int  # unit: knots / XX


@dataclass
class SystemData:
    system_time: str  # HHMMSSFF
    heading_bug: int  # unit: deg / XXX
    altitude_bug: int  # unit: feet / n / 10 / XXXXX
    airspeed_bug: float  # unit: knots / n * 10 / XXXX
    vertical_speed_bug: int  # unit: feet / n * 10 / XXXX
    course: int  # unit : deg / (3)
    cdi_src_type: int  # CDI Source Type / 0=GPS 1=NAV 2=LOC / (1)
    cdi_src_port: int  # 0-5 / GPSX, NAVX, LOCX / (1)
    cdi_scale: int  # 00-50 / unit: nm / n * 10 / XX
    cdi_deflection: int  # unit: % / positive: deflected right / XXX
    glide_slope: int  # unit: % / positive: upward from gs / XXX
    ap_engaged: int  # 0-7 / 0=off 1=roll only 2=pitch only 3=roll&pitch 4=yaw 5=roll&yaw 6=pitch&yaw 7=pitch&roll&yaw
    # raw currently not supported / 0 if ap not available / (1)
    ap_roll_mode: int  # 0-4 / 0=Heading 1=Track 2=NAV 3=GPS Steering / 0 if ap roll not engaged / (1)
    not_used_1: str  # X(1)

    # ap_x_force = 0-80 / raw force from servo / max 80 before slip / 0 if ap not engaged / (3)
    # ap_x_pos = 0-9999 / position of servo output / 800 is full rotation output / 0 if ap not engaged / XXXXX
    # ap_x_slip = 0-1 / 0=no slip 1=slip at least 3 seconds / 0 if ap not engaged / (1)
    ap_roll_force: int  # 0-80 / positive = right wing downward force / (3)
    ap_roll_pos: int  # positive = right wing downward
    ap_roll_slip: int
    ap_pitch_force: int  # positive = nose up dir
    ap_pitch_pos: int  # positive = nose up dir
    ap_pitch_slip: int
    ap_yaw_force: int  # positive = rightward dir
    ap_yaw_pos: int  # positive = rightward dir
    ap_yaw_slip: int

    transponder_status: int  # 0=SBY 1=GND 2=ON 3=ALT / (1)
    transponder_reply: int  # 0=No reply in last second 1=at least 1 reply in last second / (1)
    transponder_code: str  # 0000-7777

    not_used_2: str  # XXXXXXXXXX(10)


@dataclass
class EMSData:
    system_time: str  # HHMMSSFF
    oil_pressure: int  # unit : psi / (3)
    oil_temp: int  # unit : deg celcius / XXX
    RPM_L: int  # (4)
    RPM_R: int  # (4)
    manifold_pressure: float  # 0-600 / unit: inHg / n * 10 / (3)
    fuel_flow_1: float  # unit: gallons per hour / n * 10 / (3)
    fuel_flow_2: float  # unit: gallons per hour / n * 10 / (3)
    fuel_pressure: float  # unit: PSI / n * 10 / XXX
    fuel_level_L: float  # unit: gallons / if MAIN tank exists, it will be MAIN / n * 10 / XXX
    fuel_level_R: float  # unit: gallons / n * 10 / XXX
    fuel_remaining: float  # unit: gallons / calculated by fuel computer / n * 10 / XXX
    volts_1: float  # 000-360 / n * 10 / (3)
    volts_2: float  # 000-360 / n * 10 / (3)
    amps: float  # n * 10 / (3)
    hobbs_time: float  # unit: hours / n * 10 / (5)
    tach_time: float  # unit: hours / n * 10 / (5)
    thermocouple_1: int  # unit: deg celcius / (3)
    thermocouple_2: int  # unit: deg celcius / (3)
    thermocouple_3: int  # unit: deg celcius / (3)
    thermocouple_4: int  # unit: deg celcius / (3)
    thermocouple_5: int  # unit: deg celcius / (3)
    thermocouple_6: int  # unit: deg celcius / (3)
    thermocouple_7: int  # unit: deg celcius / (3)
    thermocouple_8: int  # unit: deg celcius / (3)
    thermocouple_9: int  # unit: deg celcius / (3)
    thermocouple_10: int  # unit: deg celcius / (3)
    thermocouple_11: int  # unit: deg celcius / (3)
    thermocouple_12: int  # unit: deg celcius / (3)
    thermocouple_13: int  # unit: deg celcius / (3)
    thermocouple_14: int  # unit: deg celcius / (3)
    gp_input_1: str  # unit: variable / n * 10 / +- value unit / +1234C (6)
    gp_input_2: str  # unit: variable / n * 10 / +- value unit / +1234C (6)
    gp_input_3: str  # unit: variable / n * 10 / +- value unit / +1234C (6)
    gp_input_4: str  # unit: variable / n * 10 / +- value unit / +1234C (6)
    gp_input_5: str  # unit: variable / n * 10 / +- value unit / +1234C (6)
    gp_input_6: str  # unit: variable / n * 10 / +- value unit / +1234C (6)
    gp_input_7: str  # unit: variable / n * 10 / +- value unit / +1234C (6)
    gp_input_8: str  # unit: variable / n * 10 / +- value unit / +1234C (6)
    gp_input_9: str  # unit: variable / n * 10 / +- value unit / +1234C (6)
    gp_input_10: str  # unit: variable / n * 10 / +- value unit / +1234C (6)
    gp_input_11: str  # unit: variable / n * 10 / +- value unit / +1234C (6)
    gp_input_12: str  # unit: variable / n * 10 / +- value unit / +1234C (6)
    gp_input_13: str  # unit: variable / n * 10 / +- value unit / +1234C (6)
    contacts: str  # Not in use / Z*16(16)

    power_percent: int  # 0-200 / unit: % / XXX
    egt_leaning_status: str  # L=lean of peak P=peak R:rich of peak X: not available / (1)




