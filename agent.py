import psutil

class psUtil():
    def __init__(self):
        self.data = []

    def _get_process_if(self):
        None
    
    def getinfo(self):
        #Disk
        diskUse = psutil.disk_usage('/')
        Info = {}
        Info['disk'] = {'used' : diskUse[1], 'free' :diskUse[2]}
        print Info 

    def publish(self):
        None
 
if __name__ == '__main__':
    self = psUtil()
    self.getinfo()