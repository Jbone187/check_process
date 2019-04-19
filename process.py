import sys
import psutil


def checkIfProcessRunning(processName):

    # Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False


def kill_active_process():

    # Checks for active process
    if len(sys.argv) > 1 and checkIfProcessRunning(sys.argv[1]) == True:

        checkIfProcessRunning(sys.argv[1])

        print('Yes a ' + sys.argv[1] +
              ' process was running and Services were Killed')

        # Loops over name associated with process
        for proc in psutil.process_iter(attrs=['pid', 'name']):

            if sys.argv[1] in proc.info['name']:
                proc.kill()
                break
            elif checkIfProcessRunning(sys.argv[1]) == False:

                print('No process ' + sys.argv[1] +
                      ' is Not Running')

    else:
        print("No Data was Return on Process")


kill_active_process()
