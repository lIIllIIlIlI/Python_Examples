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
