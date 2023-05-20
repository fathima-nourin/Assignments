import json

with open("sample_data.json", "r") as file:
    json_data = file.read()

parsed_data = json.loads(json_data)
output_list = []
if "parametersList" in parsed_data:
    parameter_list = parsed_data["parametersList"]
    for parameters in parameter_list:
        parameterName = parameters["parameterName"]
        maximum = parameters["max"]
        minimum = parameters["min"]
        average = parameters["avg"]
        parameter_dict = {
            "parameterName": parameterName,
            "min_value": minimum,
            "max_value": maximum,
            "avg_value": average
        }
        output_list.append(parameter_dict)

    json_output = json.dumps(output_list)
    with open("outuput.json", "w") as file:
        file.write(json_output)
