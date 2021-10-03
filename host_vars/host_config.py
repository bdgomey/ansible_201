import csv

with open('interfaces.csv', 'r') as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    count = 0
    for line in reader:
        if count == 0:
            count += 1
            continue

        # interface,description,ip,host
        # 0              1       2   3

        dictionary_name = f'''
ip_interfaces
'''

        file_name = f'{line[3]}'
        with open(file_name, 'w') as yml_file:
            yml_file.writelines(dictionary_name)
        count += 1

with open('interfaces.csv', 'r') as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    count = 0
    for line in reader:
        if count == 0:
            count += 1
            continue

        # interface,description,ip
        # 0              1       2

        generated_yml = f'''


- interface: {line[0]}
  description: {line[1]}
  ip: {line[2]}


'''

        file_name = f'{line[3]}'
        with open(file_name, 'a') as yml_file:
            yml_file.writelines(generated_yml)
        count += 1

