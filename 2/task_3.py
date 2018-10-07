import yaml

data = {
    'Name': 'Irina',
    'Age': '40',
    'Weight': '48',
    'City': 'Moscow',
}

with open('Yaml_data.yaml', 'w', encoding='utf-8') as f_in:
    yaml.dump(data, f_in, default_flow_style=False, allow_unicode=True)

with open("Yaml_data.yaml", 'r', encoding='utf-8') as f_out:
    data_record = yaml.load(f_out)

if data == data_record:
    print("\nДанные успешно сохранились!\n")

for keys in data_record.keys():
    print("%s -> %s" % (keys, data_record[keys]))
