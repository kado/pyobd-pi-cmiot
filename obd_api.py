import json
import httplib

def send_data(p_placa, p_pids, p_dtc_status, p_dtc_ff, p_fuel_status, p_load, 
                 p_temp, p_short_term_fuel_trim_1, p_long_term_fuel_trim_1, 
                 p_short_term_fuel_trim_2, p_long_term_fuel_trim_2, p_fuel_pressure, 
                 p_manifold_pressure, p_rpm, p_speed, p_timing_advance, p_intake_air_temp, 
                 p_maf, p_throttle_pos, p_secondary_air_status, p_o2_sensor_positions, 
                 p_o211, p_o212, p_o213, p_o214, p_o221, p_o222, p_o223, p_o224, 
                 p_obd_standard, p_o2_sensor_position_b, p_aux_input, p_engine_time, 
                 p_engine_mil_time, p_per_driver_torque, p_per_engine_torque,
                 p_ref_engine_torque, p_engine_percent_torque, p_fuel_tank_level,
                 p_actual_gear, p_calculated_gear, p_latitude, p_longitude):

    URL = "cargomodal.sinmaf.com.co"
    data = [p_placa,"0",p_pids, p_dtc_status, p_dtc_ff, p_fuel_status, p_load, 
            p_temp, p_short_term_fuel_trim_1, p_long_term_fuel_trim_1, 
            p_short_term_fuel_trim_2, p_long_term_fuel_trim_2, p_fuel_pressure, 
            p_manifold_pressure, p_rpm, p_speed, p_timing_advance, p_intake_air_temp, 
            p_maf, p_throttle_pos, p_secondary_air_status, p_o2_sensor_positions, 
            p_o211, p_o212, p_o213, p_o214, p_o221, p_o222, p_o223, p_o224, 
            p_obd_standard, p_o2_sensor_position_b, p_aux_input, p_engine_time, 
            p_engine_mil_time, p_per_driver_torque, p_per_engine_torque,
            p_ref_engine_torque, p_engine_percent_torque, p_fuel_tank_level,
            p_actual_gear, p_calculated_gear, p_latitude, p_longitude]

    #Con modulo httplib.
	try:
		connection = httplib.HTTPConnection(URL)
		headers = {'Content-Type': 'application/json'}
		json_data = json.dumps(data)

		connection.request("POST", "/iot/api/values", json_data, headers)
		response = connection.getresponse()
		return (response.status)
	except Exception as err:
		print("Data loss, couldn't send it to API: " + str(err))
		return -1 
