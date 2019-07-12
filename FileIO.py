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
