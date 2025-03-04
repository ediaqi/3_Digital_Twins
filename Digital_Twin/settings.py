LOG_LEVEL = "INFO"

DUMMY_DATA = {
        "indoor": {
            "temperature": 15.5,
            "rh": 55.3,
            "atmPressure": 1013.8,
            "pm1": 2.5,
            "pm10": 550,
            "pm25": 9.7,
            "co2": 1555.2,
            "co": 550,
            "tvecc": 310.4,
            "no2": 100,
            "o3": 400
        },
        "outdoor": {
            "no2": 44.1,
            "o3": 127.5,
            "so2": 12.8,
            "co": 0.82,
            "pm25": 27.6,
            "pm1": 10,
            "pm10": 36.9,
            "no": 20.3,
            "co2": 421.5,
            "temp": 12.3,
            "rh": 45.2,
            "atm": 1016.2,
            "noise": 78.4
        },
        "additionalInfo": {
            "cars": 42,
            "trucks": 15,
            "buses": 8,
            "motorcycles": 21
        },
        "ventilation": {
            "window": True
        },
        "filteringUnit": {
            "x": 132,
            "y": 178,
            "z": 87
        }
    }


TIMEZONE = 'Europe/Zagreb'

INDOOR_ENVIRONMENT_FEATURES = {
                "CO2_values": ["CO2_device_316", "CO2_device_4", "CO2_device_7", "CO2_device_13", 
                                "NetCO2-CO2(ppm)_LS0623020168", "NetCO2-CO2(ppm)_LS0623020169"],
                "Temperature_values": ["temperature_device_316", "temperature_device_4", "temperature_device_7", 
                                        "temperature_device_13", "NetBME280-TEMP_EXT(°C)_LS0623020168", 
                                        "NetBME280-TEMP_EXT(°C)_LS0623020169"],
                "PM10_values" : ["PM10_device_316", "PM10_device_4", "PM10_device_7", "PM10_device_13",
                                "NetPM-PM10(µg/m3)_LS0623020168", "NetPM-PM10(µg/m3)_LS0623020169"],
                "CO_values" : ["CO_device_316", "CO_device_4", "CO_device_7", "CO_device_13",
                                "NetADC_CO-CO( ppb)_LS0623020168", "NetADC_CO-CO( ppb)_LS0623020169"],
                "PM25_values" : ["PM25_device_316", "PM25_device_4", "PM25_device_7", "PM25_device_13",
                                "NetPM-PM25(µg/m3)_LS0623020168", "NetPM-PM25(µg/m3)_LS0623020169"],
                "PM1_values" : ["PM1_device_316", "PM1_device_4", "PM1_device_7", "PM1_device_13"],
                "humidity_values" : ["humidity_device_316", "humidity_device_4", "humidity_device_7",
                                    "humidity_device_13", "NetBME280-PERC(%)_LS0623020168", 
                                    "NetBME280-PERC(%)_LS0623020169"],
                "atmospheric_pressure_values" : ["atmospheric_pressure_device_316", "atmospheric_pressure_device_4",
                                                "atmospheric_pressure_device_7", "atmospheric_pressure_device_13",
                                                "NetBME280-HPA(hPa)_LS0623020168", "NetBME280-HPA(hPa)_LS0623020169"],
                "TVOC_values" : ["TVOC_device_316", "TVOC_device_4", "TVOC_device_7", "TVOC_device_13",
                                "NetPid_P1-PPB(ppm)_LS0623020168", "NetPid_P1-PPB(ppm)_LS0623020169"],
                "NO2_values": ["NetADC_NO2-NO2(ppb)_LS0623020168", "NetADC_NO2-NO2(ppb)_LS0623020169"],
                "O3_values": ["NetADC_O3-O3(ppb)_LS0623020168", "NetADC_O3-O3(ppb)_LS0623020169"]
                }

OUTDOOR_ENVIROMENT_FEATURES = {
            "CO2_values": ["CO2_device_402"],
            "Temperature_values": ["temperature_device_402"],
            "PM10_values" : ["PM10_device_402"],
            "CO_values" : ["CO_device_402"],
            "PM1_values" : ["PM1_device_402"],
            "PM25_values" : ["PM25_device_402"],
            "humidity_values" : ["humidity_device_402"],
            "atmospheric_pressure_values" : ["atmospheric_pressure_device_402"],
            "O3_values" : ["O3_device_402"],
            "NO2_values" : ["NO2_device_402"],
            "SO2_values" : ["SO2_device_402"],
            "NO_values" : ["NO_device_402"],
            "Noise_values" : ["noise_device_402"]
    }

CONNECTING_INPUTS_INDOOR = {'CO2_values':'co2',
                    'CO_values': "co",
                    "O3_values": "o3",
                    "NO2_values": 'no2',
                    'Temperature_values':'temperature',
                    'PM10_values': 'pm10',
                    'PM25_values':'pm25',
                    "PM1_values" : "pm1",
                    'humidity_values':'rh',
                    'atmospheric_pressure_values':'atmPressure',
                    'TVOC_values':'tvecc'}

CONNECTING_INPUTS_OUTDOOR = {
                        'CO2_values':'co2',
                    'CO_values': "co",
                    "O3_values": "o3",
                    "NO2_values": 'no2',
                    'Temperature_values':'temp',
                    'PM10_values': 'pm10',
                    'PM25_values':'pm25',
                    'humidity_values':'rh',
                    'atmospheric_pressure_values':'atm',
                    'Noise_values': "noise",
                    "SO2_values":'so2',
                    "NO_values" : 'no',
                    "PM1_values": "pm1",
}

MAX_DUMMIES_FOR_TRAFFIC = {
        'car': 14,
        'truck': 4,
        'bus': 3,
        'motorcycle': 3
    }

CO2_N_VALUES= {'CO2_device_316': 36.55775361927357,
                'CO2_device_4': 36.55775361927357,
                'CO2_device_7': 36.55775361927357,
                'CO2_device_13': 36.55775361927357,
                'NetCO2-CO2(ppm)_LS0623020168': 22.734708358869707,
                'NetCO2-CO2(ppm)_LS0623020169': 23.217935934155342
                }

SENSOR_PLACEMENT = {'4': [115, 137, 13],
            '316': [115, 137, 100],
            'LS0623020169': [115, 137, 145],
            'LS0623020168': [310, 225, 13],
            '7': [310, 225, 100],
            '13': [310, 225, 145]
            }

RENAMING_FEATURES_FILTERING_UNIT = {
    '4': 'filtering_unit_distance_to_sensor_4',
    '316': 'filtering_unit_distance_to_sensor_316',
    'LS0623020169': 'filtering_unit_distance_to_sensor_LS0623020169',
    'LS0623020168': 'filtering_unit_distance_to_sensor_LS0623020168',
    '7': 'filtering_unit_distance_to_sensor_7',
    '13': 'filtering_unit_distance_to_sensor_13'
}

## MASS BALANCE PARAMETERS 

P_LAMBDA_MASS_BALANCE = {'PM1_device_316': -0.057281043790827234,
                        'PM25_device_316': -0.04397828954896086,
                        'PM10_device_316': -0.02380977198963783,
                        'PM1_device_4':-0.057281043790827234,
                        'PM25_device_4':-0.04397828954896086,
                        'PM10_device_4':-0.02380977198963783,
                        'PM1_device_7':-0.057281043790827234,
                        'PM25_device_7':-0.04397828954896086,
                        'PM10_device_7':-0.02380977198963783,
                        'PM1_device_13':-0.057281043790827234,
                        'PM25_device_13':-0.04397828954896086,
                        'PM10_device_13':-0.02380977198963783,
                        'NetPM-PM10(µg/m3)_LS0623020168': -0.03137949975673056,
                        'NetPM-PM25(µg/m3)_LS0623020168': -0.05804347634868194,
                        'NetPM-PM10(µg/m3)_LS0623020169': -0.024034002601319587,
                        'NetPM-PM25(µg/m3)_LS0623020169': -0.04410814322979983
                        }

LAMBDA_MASS_BALANCE = {'PM1_device_316': -0.03515100000437102,
                    'PM25_device_316': -0.0371645000046222,
                    'PM10_device_316': -0.037157500004621744,
                    'PM1_device_4':-0.03515100000437102,
                    'PM25_device_4':-0.0371645000046222,
                    'PM10_device_4':-0.037157500004621744,
                    'PM1_device_7':-0.03515100000437102,
                    'PM25_device_7':-0.0371645000046222,
                    'PM10_device_7':-0.037157500004621744,
                    'PM1_device_13':-0.03515100000437102,
                    'PM25_device_13':-0.0371645000046222,
                    'PM10_device_13':-0.037157500004621744,
                    'NetPM-PM10(µg/m3)_LS0623020168': -0.04848219444545886,
                    'NetPM-PM25(µg/m3)_LS0623020168': -0.04848219444545886,
                    'NetPM-PM10(µg/m3)_LS0623020169': -0.035903305555573535,
                    'NetPM-PM25(µg/m3)_LS0623020169': -0.03563288888895624
                    }

LAMBDAD_MASS_BALANCE = {'PM1_device_316': -0.0010146554146679833,
                        'PM25_device_316': -0.0011013514471519578,
                        'PM10_device_316': -0.0011361499115912469,
                        'PM1_device_4':-0.0010146554146679833,
                        'PM25_device_4':-0.0011013514471519578,
                        'PM10_device_4':-0.0011361499115912469,
                        'PM1_device_7':-0.0010146554146679833,
                        'PM25_device_7':-0.0011013514471519578,
                        'PM10_device_7':-0.0011361499115912469,
                        'PM1_device_13':-0.0010146554146679833,
                        'PM25_device_13':-0.0011013514471519578,
                        'PM10_device_13':-0.0011361499115912469,
                        'NetPM-PM10(µg/m3)_LS0623020168': -0.0011086250406676836,
                        'NetPM-PM25(µg/m3)_LS0623020168': -0.0010859397158107526,
                        'NetPM-PM10(µg/m3)_LS0623020169': -0.001140100995024063,
                        'NetPM-PM25(µg/m3)_LS0623020169': -0.0011177390476888988
                        }

INDOOR_COL_FOR_MASS_BALANCE = ['PM1_device_316', 'PM25_device_316', 'PM10_device_316', 'PM1_device_4',
                                'PM25_device_4', 'PM10_device_4', 'PM1_device_7', 'PM25_device_7',
                                'PM10_device_7', 'PM1_device_13', 'PM25_device_13', 'PM10_device_13',
                                'NetPM-PM10(µg/m3)_LS0623020168', 'NetPM-PM25(µg/m3)_LS0623020168',
                                'NetPM-PM10(µg/m3)_LS0623020169','NetPM-PM25(µg/m3)_LS0623020169']

INDOOR_OUTDOOR_CONNECTION_MASS_BALANCE = {
                    'PM1_device_316':'PM1_device_402',
                    'PM25_device_316':'PM25_device_402',
                    'PM10_device_316':'PM10_device_402',
                    'PM1_device_4':'PM1_device_402',
                    'PM25_device_4':'PM25_device_402',
                    'PM10_device_4':'PM10_device_402',
                    'PM1_device_7':'PM1_device_402',
                    'PM25_device_7':'PM25_device_402',
                    'PM10_device_7':'PM10_device_402',
                    'PM1_device_13':'PM1_device_402',
                    'PM25_device_13':'PM25_device_402',
                    'PM10_device_13':'PM10_device_402',
                    'NetPM-PM10(µg/m3)_LS0623020168':'PM10_device_402',
                    'NetPM-PM25(µg/m3)_LS0623020168':'PM25_device_402',
                    'NetPM-PM10(µg/m3)_LS0623020169':'PM10_device_402',
                    'NetPM-PM25(µg/m3)_LS0623020169':'PM25_device_402',
}

LAG_FEATURES = ['CO2_device_316', 'TVOC_device_316',
        'CO_device_316', 'PM1_device_316',
        'PM25_device_316', 'PM10_device_316', 'temperature_device_316',
        'humidity_device_316', 'atmospheric_pressure_device_316',
        'CO2_device_4', 'TVOC_device_4', 'CO_device_4', 'PM1_device_4',
        'PM25_device_4', 'PM10_device_4', 'temperature_device_4',
        'humidity_device_4', 'atmospheric_pressure_device_4', 'CO2_device_7',
        'TVOC_device_7', 'CO_device_7', 'PM1_device_7', 'PM25_device_7',
        'PM10_device_7', 'temperature_device_7', 'humidity_device_7',
        'atmospheric_pressure_device_7', 'CO2_device_13', 'TVOC_device_13',
        'CO_device_13', 'PM1_device_13', 'PM25_device_13', 'PM10_device_13',
        'temperature_device_13', 'humidity_device_13',
        'atmospheric_pressure_device_13', 'NetCO2-CO2(ppm)_LS0623020168',
        'NetADC_O3-O3(ppb)_LS0623020168', 'NetADC_CO-CO( ppb)_LS0623020168',
        'NetPM-PM10(µg/m3)_LS0623020168', 'NetPM-PM25(µg/m3)_LS0623020168',
        'NetPid_P1-PPB(ppm)_LS0623020168', 'NetBME280-PERC(%)_LS0623020168',
        'NetBME280-TEMP_EXT(°C)_LS0623020168',
        'NetBME280-HPA(hPa)_LS0623020168', 'NetADC_NO2-NO2(ppb)_LS0623020168',
        'NetCO2-CO2(ppm)_LS0623020169', 'NetADC_O3-O3(ppb)_LS0623020169',
        'NetADC_CO-CO( ppb)_LS0623020169', 'NetPM-PM10(µg/m3)_LS0623020169','NetPM-PM25(µg/m3)_LS0623020169', 'NetPid_P1-PPB(ppm)_LS0623020169',
        'NetBME280-PERC(%)_LS0623020169', 'NetBME280-TEMP_EXT(°C)_LS0623020169',
        'NetBME280-HPA(hPa)_LS0623020169', 'NetADC_NO2-NO2(ppb)_LS0623020169',
        'NO2_device_402', 'O3_device_402', 'SO2_device_402', 'CO_device_402',
        'PM1_device_402', 'PM25_device_402', 'PM10_device_402', 'NO_device_402',
        'CO2_device_402', 'temperature_device_402', 'humidity_device_402',
        'atmospheric_pressure_device_402', 'noise_device_402']

TARGETS_FOR_ML_MODELS = {
    'CO2':['CO2_device_316', 'CO2_device_4', 'CO2_device_7', 'CO2_device_13', 'NetCO2-CO2(ppm)_LS0623020168', 'NetCO2-CO2(ppm)_LS0623020169'],
    'CO':['CO_device_316', 'CO_device_4', 'CO_device_7', 'CO_device_13', 'NetADC_CO-CO( ppb)_LS0623020168', 'NetADC_CO-CO( ppb)_LS0623020169'],
    'TVOC':['TVOC_device_316', 'TVOC_device_4', 'TVOC_device_7', 'TVOC_device_13', 'NetPid_P1-PPB(ppm)_LS0623020168', 'NetPid_P1-PPB(ppm)_LS0623020169'],
    'PM25':['PM25_device_316', 'PM25_device_4', 'PM25_device_7', 'PM25_device_13', 'NetPM-PM25(µg/m3)_LS0623020168', 'NetPM-PM25(µg/m3)_LS0623020169'],
    'PM10':	['PM10_device_316', 'PM10_device_4', 'PM10_device_7', 'PM10_device_13', 'NetPM-PM10(µg/m3)_LS0623020168', 'NetPM-PM10(µg/m3)_LS0623020169'],
    'temperature':['temperature_device_316', 'temperature_device_4', 'temperature_device_7', 'temperature_device_13', 'NetBME280-TEMP_EXT(°C)_LS0623020168', 'NetBME280-TEMP_EXT(°C)_LS0623020169'],
    'humidity':['humidity_device_316', 'humidity_device_4', 'humidity_device_7', 'humidity_device_13', 'NetBME280-PERC(%)_LS0623020168', 'NetBME280-PERC(%)_LS0623020169'],
    'atmospheric_pressure':['atmospheric_pressure_device_316', 'atmospheric_pressure_device_4', 'atmospheric_pressure_device_7', 'atmospheric_pressure_device_13', 'NetBME280-HPA(hPa)_LS0623020168', 'NetBME280-HPA(hPa)_LS0623020169'],
}

MODELS_PATH_FILTRATION = './models_loading/models/models_filtration'
SCALERS_PATH_FILTRATION = './models_loading/models/scalers_filtration'

MODELS_PATH_NO_FILTRATION = './models_loading/models/models_no_filtration'
SCALERS_PATH_NO_FILTRATION = './models_loading/models/scalers_no_filtration'

COLUMNS_ORDER_FOR_MODEL = [
    "CO2_device_316", "TVOC_device_316", "CO_device_316", "PM1_device_316", "PM25_device_316", 
    "PM10_device_316", "temperature_device_316", "humidity_device_316", "atmospheric_pressure_device_316", 
    "CO2_device_4", "TVOC_device_4", "CO_device_4", "PM1_device_4", "PM25_device_4", "PM10_device_4", 
    "temperature_device_4", "humidity_device_4", "atmospheric_pressure_device_4", 
    "CO2_device_7", "TVOC_device_7", "CO_device_7", "PM1_device_7", "PM25_device_7", "PM10_device_7", 
    "temperature_device_7", "humidity_device_7", "atmospheric_pressure_device_7", 
    "CO2_device_13", "TVOC_device_13", "CO_device_13", "PM1_device_13", "PM25_device_13", 
    "PM10_device_13", "temperature_device_13", "humidity_device_13", "atmospheric_pressure_device_13", 
    "NetCO2-CO2(ppm)_LS0623020168", "NetADC_O3-O3(ppb)_LS0623020168", "NetADC_CO-CO( ppb)_LS0623020168", 
    "NetPM-PM10(µg/m3)_LS0623020168", "NetPM-PM25(µg/m3)_LS0623020168", "NetPid_P1-PPB(ppm)_LS0623020168", 
    "NetBME280-PERC(%)_LS0623020168", "NetBME280-TEMP_EXT(°C)_LS0623020168", "NetBME280-HPA(hPa)_LS0623020168", 
    "NetADC_NO2-NO2(ppb)_LS0623020168", "NetCO2-CO2(ppm)_LS0623020169", "NetADC_O3-O3(ppb)_LS0623020169", 
    "NetADC_CO-CO( ppb)_LS0623020169", "NetPM-PM10(µg/m3)_LS0623020169", "NetPM-PM25(µg/m3)_LS0623020169", 
    "NetPid_P1-PPB(ppm)_LS0623020169", "NetBME280-PERC(%)_LS0623020169", "NetBME280-TEMP_EXT(°C)_LS0623020169", 
    "NetBME280-HPA(hPa)_LS0623020169", "NetADC_NO2-NO2(ppb)_LS0623020169", "NO2_device_402", 
    "O3_device_402", "SO2_device_402", "CO_device_402", "PM1_device_402", "PM25_device_402", 
    "PM10_device_402", "NO_device_402", "CO2_device_402", "temperature_device_402", 
    "humidity_device_402", "atmospheric_pressure_device_402", "noise_device_402", 
    "car_0", "car_1", "car_2", "car_3", "car_4", "car_5", "car_6", "car_7", "car_8", "car_9", 
    "car_10", "car_11", "car_12", "car_13", "car_14", "truck_0", "truck_1", "truck_2", 
    "truck_3", "truck_4", "bus_0", "bus_1", "bus_2", "bus_3", "motorcycle_0", "motorcycle_1", 
    "motorcycle_2", "motorcycle_3", "Small_window", "CO2_device_316_1", "CO2_device_316_5", 
    "CO2_device_316_10", "CO2_device_4_1", "CO2_device_4_5", "CO2_device_4_10", "CO2_device_7_1", 
    "CO2_device_7_5", "CO2_device_7_10", "CO2_device_13_1", "CO2_device_13_5", "CO2_device_13_10", 
    "NetCO2-CO2(ppm)_LS0623020168_1", "NetCO2-CO2(ppm)_LS0623020168_5", "NetCO2-CO2(ppm)_LS0623020168_10", 
    "NetCO2-CO2(ppm)_LS0623020169_1", "NetCO2-CO2(ppm)_LS0623020169_5", "NetCO2-CO2(ppm)_LS0623020169_10", 
    "filtering_unit_distance_to_sensor_4", "filtering_unit_distance_to_sensor_316", 
    "filtering_unit_distance_to_sensor_LS0623020169", "filtering_unit_distance_to_sensor_LS0623020168", 
    "filtering_unit_distance_to_sensor_7", "filtering_unit_distance_to_sensor_13", 
    "PM1_device_316_dI/dt", "PM1_device_316_S", "PM25_device_316_dI/dt", "PM25_device_316_S", 
    "PM10_device_316_dI/dt", "PM10_device_316_S", "PM1_device_4_dI/dt", "PM1_device_4_S", 
    "PM25_device_4_dI/dt", "PM25_device_4_S", "PM10_device_4_dI/dt", "PM10_device_4_S", 
    "PM1_device_7_dI/dt", "PM1_device_7_S", "PM25_device_7_dI/dt", "PM25_device_7_S", 
    "PM10_device_7_dI/dt", "PM10_device_7_S", "PM1_device_13_dI/dt", "PM1_device_13_S", 
    "PM25_device_13_dI/dt", "PM25_device_13_S", "PM10_device_13_dI/dt", "PM10_device_13_S", 
    "NetPM-PM10(µg/m3)_LS0623020168_dI/dt", "NetPM-PM10(µg/m3)_LS0623020168_S", 
    "NetPM-PM25(µg/m3)_LS0623020168_dI/dt", "NetPM-PM25(µg/m3)_LS0623020168_S", 
    "NetPM-PM10(µg/m3)_LS0623020169_dI/dt", "NetPM-PM10(µg/m3)_LS0623020169_S", 
    "NetPM-PM25(µg/m3)_LS0623020169_dI/dt", "NetPM-PM25(µg/m3)_LS0623020169_S", "day_sin", 
    "hour_sin", "CO2_device_316_lag_1_mode", "TVOC_device_316_lag_1_mode", "CO_device_316_lag_1_mode", 
    "PM1_device_316_lag_1_mode", "PM25_device_316_lag_1_mode", "PM10_device_316_lag_1_mode", 
    "temperature_device_316_lag_1_mode", "humidity_device_316_lag_1_mode", 
    "atmospheric_pressure_device_316_lag_1_mode", "CO2_device_4_lag_1_mode", 
    "TVOC_device_4_lag_1_mode", "CO_device_4_lag_1_mode", "PM1_device_4_lag_1_mode", 
    "PM25_device_4_lag_1_mode", "PM10_device_4_lag_1_mode", "temperature_device_4_lag_1_mode", 
    "humidity_device_4_lag_1_mode", "atmospheric_pressure_device_4_lag_1_mode", 
    "CO2_device_7_lag_1_mode", "TVOC_device_7_lag_1_mode", "CO_device_7_lag_1_mode", 
    "PM1_device_7_lag_1_mode", "PM25_device_7_lag_1_mode", "PM10_device_7_lag_1_mode", 
    "temperature_device_7_lag_1_mode", "humidity_device_7_lag_1_mode", 
    "atmospheric_pressure_device_7_lag_1_mode", "CO2_device_13_lag_1_mode", 
    "TVOC_device_13_lag_1_mode", "CO_device_13_lag_1_mode", "PM1_device_13_lag_1_mode", 
    "PM25_device_13_lag_1_mode", "PM10_device_13_lag_1_mode", "temperature_device_13_lag_1_mode", 
    "humidity_device_13_lag_1_mode", "atmospheric_pressure_device_13_lag_1_mode", 
    "NetCO2-CO2(ppm)_LS0623020168_lag_1_mode", "NetADC_O3-O3(ppb)_LS0623020168_lag_1_mode", 
    "NetADC_CO-CO( ppb)_LS0623020168_lag_1_mode", "NetPM-PM10(µg/m3)_LS0623020168_lag_1_mode", 
    "NetPM-PM25(µg/m3)_LS0623020168_lag_1_mode", "NetPid_P1-PPB(ppm)_LS0623020168_lag_1_mode", 
    "NetBME280-PERC(%)_LS0623020168_lag_1_mode", "NetBME280-TEMP_EXT(°C)_LS0623020168_lag_1_mode", 
    "NetBME280-HPA(hPa)_LS0623020168_lag_1_mode", "NetADC_NO2-NO2(ppb)_LS0623020168_lag_1_mode", 
    "NetCO2-CO2(ppm)_LS0623020169_lag_1_mode", "NetADC_O3-O3(ppb)_LS0623020169_lag_1_mode", 
    "NetADC_CO-CO( ppb)_LS0623020169_lag_1_mode", "NetPM-PM10(µg/m3)_LS0623020169_lag_1_mode", 
    "NetPM-PM25(µg/m3)_LS0623020169_lag_1_mode", "NetPid_P1-PPB(ppm)_LS0623020169_lag_1_mode", 
    "NetBME280-PERC(%)_LS0623020169_lag_1_mode", "NetBME280-TEMP_EXT(°C)_LS0623020169_lag_1_mode", 
    "NetBME280-HPA(hPa)_LS0623020169_lag_1_mode", "NetADC_NO2-NO2(ppb)_LS0623020169_lag_1_mode", 
    "NO2_device_402_lag_1_mode", "O3_device_402_lag_1_mode", "SO2_device_402_lag_1_mode", 
    "CO_device_402_lag_1_mode", "PM1_device_402_lag_1_mode", "PM25_device_402_lag_1_mode", 
    "PM10_device_402_lag_1_mode", "NO_device_402_lag_1_mode", "CO2_device_402_lag_1_mode", 
    "temperature_device_402_lag_1_mode", "humidity_device_402_lag_1_mode", 
    "atmospheric_pressure_device_402_lag_1_mode", "noise_device_402_lag_1_mode"]

COLUMNS_IN_INPUT = {
    'CO2': 'co2', 
    'CO': 'co',
    'TVOC': 'tvecc',
    'PM10': 'pm10',
    'PM25': 'pm25', 
    'temperature': 'temperature',
    'humidity': 'rh',
    'atmospheric_pressure': 'atmPressure',
}
