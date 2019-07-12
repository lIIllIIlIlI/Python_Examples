import subprocess
 
  command = ["hello","world"]
  process = subprocess.Popen(command, bufsize=1, universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            for line in iter(process.stdout.readline, ''):  
                runLogger.info(line.rstrip())
            process.wait()
            if process.returncode:
                logString = "FAIL"
                resultLogger.error(logString)
            else:
                logString = "SUCCESS"
                resultLogger.info(logString)

              
 command = ['svn', 'propget', frozenProperty, "--show-inherited-props", folder]
        process = subprocess.Popen(command, bufsize=1, universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        for line in iter(process.stdout.readline, ''):  
            print(line)
        
 command = ['size', '--version']
    callCmd = subprocess.Popen(command,
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    stdout, stderr = callCmd.communicate()
    if callCmd.returncode:
        memLogger.error("Cmd Call returned with error message '"'{}'"', make sure 'size' from "
                        "binutils is installed properly, terminating ... ".format(stderr))
        sys.exit(0)
    
command = ['readelf', '--sections', elfElement]
    callCmd = subprocess.Popen(command,
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    for line in iter(callCmd.stdout.readline, ''):
       counter++;
       if counter > 10000:
           break
   stdout, stderr = callCmd.communicate()
   if(stderr):
      
     
callCmd = subprocess.Popen(command,
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    for line in iter(callCmd.stdout.readline, ''):
  
    for line in iter(callCmd.stderr.readline, ''):
  
    

 
        
 # Carefull: Some commands won't terminate, therefore python will read infinite blank lines. 
 # Therefore install a Counter to only read n lines of both stdout and stderr.
