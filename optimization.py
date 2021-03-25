import json
import os 

input_dir = os.path.join(os.getcwd(), 'input')
output_dir = f'{input_dir}/modified'

chassis_name = 'Eco1C1G1T1'

input_file = f'{input_dir}/{chassis_name}.input.json'

# print(input_sensor)
with open(input_file) as f:
    data = json.load(f)


# ymax should be smaller for On min
# ymin should be larger for Off min

for field in data:
    if field["collection"] == "models":
        params = field["parameters"]

        # predefinition in the higher scope
        ymax = 0
        ymin = 0
        n = 0
        k = 0

        # these values need to be changed
        ## TODO: develop algorithms to determine these values

        inc_slope_para = 1.05
        dec_slope_para = 1.05
        stronger_prom_para = 1.50
        weaker_prom_para = 1.5
        strong_rbs_para = 1.50
        weak_rbs_para = 1.50

        for param in params:
            if param["name"] == "ymax":
                ymax = param["value"]

                param["value"] = ymax * stronger_prom_para

            elif param["name"] == "ymin":
                ymin = param["value"]

                param["value"] = ymin * weaker_prom_para

            elif param["name"] == "alpha":
                n = param["value"]

                param["value"] = n * inc_slope_para
            
            elif param["name"] == "beta":
                k = param["value"]

                param["value"] = k * weak_rbs_para

            else:
                pass
            
with open(f'{output_dir}/{chassis_name}.input.json', 'w') as new_file:
    json.dump(data, new_file)