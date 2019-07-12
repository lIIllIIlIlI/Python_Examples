########################################################
# There are three different use cases that require different formats:
#
# 1. User config file - Yaml
#
# 2. in/out file for further processing - csv
#
# 3. internal dump/load - pickle
#
# All three variants need to be adressed separately
#
########################################################


import yaml
# YAML --------------------------------------------------------------------------
Variants:
- CWA950_48V_GM
- CWA950_48V_PPT
- eCC
- eCC_HV3
- CWA150_2
- WUP4
- CWP250_BMW
- CWP150_BMW
- E174_CWA950_400V
- E179_EOP_Renault
- E180_CWA450
- E181_WUP4_24V_PWM
- E182_CWP250_Audi
- E186_EOP_Audi
- all

# Target Controller
Controller:  
  CWA150_2: ARM
  WUP4: ARM
  CWA950_48V_GM: dsPIC
  CWA950_48V_PPT: dsPIC
  CWP250_BMW: ARM
  CWP150_BMW: ARM
  E174_CWA950_400V: dsPIC
  E179_EOP_Renault: ARM
  E180_CWA450: ARM
  E181_WUP4_24V_PWM: dsPIC
  E182_CWP250_Audi: ARM
  E186_EOP_Audi: ARM
  eCC: dsPIC
  eCC_HV3: dsPIC

# init data
myList = ['a', 'b']
myDict = {'c': 1, 'd':2}

# Write yaml (PROBLEM: Does not look like the above, names of variables are discarded)
with open("test.yml", 'w') as yamlFile:
	yaml.dump(myList, yamlFile, default_flow_style = False)
	yaml.dump(myDict , yamlFile, default_flow_style = False)
[/code]

# open reading
try:                   
    with open('my_yaml.yml', 'r') as my_yaml:
        my_yaml_reader = yaml.load(my_yaml)
        variable = my_yaml_reader['Variants']
        another_variable = my_yaml_reader['Controller']
except:
    print("Could not read yaml file, please create proper configuration!")
    
# Refresh general file by opening in write mode    
open(logFilePath,"w+")
-------------------------------------------------------------------------------------


# CSV -------------------------------------------------------------------------------

 elfElementList = listFiles(elfPath, extension)
    for elfElement in elfElementList:
        addColumnCsvFile(elfElement, currentTime)

    print("\n\n\n")
    with open(currentTime + ".prof", 'r', newline='') as csvfile:
        memReader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in memReader:
            print("{:<20}{:>10}{:>10}".format(*row))
            try:
                ramUsageSum += int(row[1])
                romUsageSum += int(row[2])
            except:
                pass
            
  with open(currentTime + ".prof", 'a', newline='') as csvfile:
        memWriter = csv.writer(csvfile, delimiter=' ',
                               quotechar='|', quoting=csv.QUOTE_MINIMAL)
        memWriter.writerow(['Sum', ramUsageSum, romUsageSum])
     
            
 def initCsvFile():
    """
    Deletes all values of temporary excel file
    """
    global currentTime
    # Create profile
    tmpFd = open(currentTime + ".prof", "w+")
    tmpFd.close()

    # Add Metadata to profile
    addMetadataToCsvFile()

    try:
        with open(currentTime + ".prof", 'a', newline='') as csvfile:
            memWriter = csv.writer(
                csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            memWriter.writerow(['Element', 'Ram', 'Rom'])
    except:
        memLogger.error("Unable to refresh profile. Resulting profile might be corrupted."
                        "Continuing ...")

   

with open(currentTime + ".prof", 'a', newline='') as csvfile:
                memWriter = csv.writer(csvfile, delimiter=' ',
                                       quotechar='|', quoting=csv.QUOTE_MINIMAL)
                memWriter.writerow(['Version control', 'no', ''])
                memWriter.writerow(['Folder name', elfPath, ''])
                memWriter.writerow(['', '', ''])

# ------------------------------------------------------------------------------------
