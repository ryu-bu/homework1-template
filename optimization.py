import json
import os 

input_dir = os.path.join(os.getcwd(), "input")
output_dir = f"{input_dir}/modified"

chassis_name = "Eco1C1G1T1"

input_file = f"{input_dir}/{chassis_name}.input.json"

# print(input_sensor)
with open(input_file) as f:
    data = json.load(f)

# ymax should be smaller for On min
# ymin should be larger for Off min


# predefinition in the higher scope
ymax = 0
ymin = 0
n = 0
k = 0

# these values need to be changed
 ## TODO: develop algorithms to determine these values
 
inc_slope_para = 1.05
dec_slope_para = 1.05
stronger_prom_para = 1.5
weaker_prom_para = 1.5
strong_rbs_para = 2
weak_rbs_para = 14

for field in data:
    if field["collection"] == "models" and field['name'] == 'LacI_sensor_model':
        # LacI is Lac repressor, Thus is weak promoter
        # Ribosome Bind Site of LacI required fully optimized
        LacI_params = field["parameters"]
        for param in LacI_params:
            if param["name"] == "ymax":
                ymax = param["value"]

                param["value"] = ymax / weaker_prom_para

            elif param["name"] == "ymin":
                ymin = param["value"]

                param["value"] = ymin * weaker_prom_para

            elif param["name"] == "alpha":
                n = param["value"]

                param["value"] = n / inc_slope_para
            
            elif param["name"] == "beta":
                k = param["value"]

                param["value"] = k * weak_rbs_para

            else:
                pass
            
            
    if field["collection"] == "models" and field['name'] == 'TetR_sensor_model':
        #Tet_R is Tetracycline repressor, Thus is strong promoter
        TetR_params = field["parameters"]
        for param in TetR_params:
            if param["name"] == "ymax":
                ymax = param["value"]

                param["value"] = ymax / weaker_prom_para

            elif param["name"] == "ymin":
                ymin = param["value"]

                param["value"] = ymin * weaker_prom_para

            elif param["name"] == "alpha":
                n = param["value"]

                param["value"] = n / inc_slope_para
            
            elif param["name"] == "beta":
                k = param["value"]

                param["value"] = k / strong_rbs_para

            else:
                pass
            
    if field["collection"] == "models" and field['name'] == 'AraC_sensor_model':
        #LuxR is usually strong promoter
        AraC_params = field["parameters"]
        for param in AraC_params:
            if param["name"] == "ymax":
                ymax = param["value"]

                param["value"] = ymax / weaker_prom_para

            elif param["name"] == "ymin":
                ymin = param["value"]

                param["value"] = ymin * weaker_prom_para

            elif param["name"] == "alpha":
                n = param["value"]

                param["value"] = n * inc_slope_para
            
            elif param["name"] == "beta":
                k = param["value"]

                param["value"] = k / strong_rbs_para

            else:
                pass
            
            
    if field["collection"] == "models" and field['name'] == 'LuxR_sensor_model':
        #LuxR is usually strong promoter
        LuxR_params = field["parameters"]
        for param in LuxR_params:
            if param["name"] == "ymax":
                ymax = param["value"]

                param["value"] = ymax * weaker_prom_para

            elif param["name"] == "ymin":
                ymin = param["value"]

                param["value"] = ymin / weaker_prom_para

            elif param["name"] == "alpha":
                n = param["value"]

                param["value"] = n / inc_slope_para
            
            elif param["name"] == "beta":
                k = param["value"]

                param["value"] = k / strong_rbs_para

            else:
                pass
            
with open(f'{output_dir}/{chassis_name}.input.json', 'w') as new_file:
    json.dump(data, new_file)
