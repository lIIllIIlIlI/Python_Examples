import yaml

# open reading
try:                   
    with open('my_yaml.yml', 'r') as my_yaml:
        my_yaml_reader = yaml.load(my_yaml)
        variable = my_yaml_reader[1]
        another_variable = my_yaml_reader[4]
except:
    print("Could not read yaml file, please create proper configuration!")
    
# Refresh general file by opening in write mode    
open(logFilePath,"w+")
