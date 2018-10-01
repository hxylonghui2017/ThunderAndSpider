import os, time
#import threading
from thunder.thunder_config import *

class my_thunder:
    def __init__(self, url):
        self.url = url
        self.filename = os.path.split(self.url)[1]
        self.args = r'"{thunder_path}" {url}'.format(thunder_path=thunder_path, url=url)

    def start_target(self):
        print("准备下载---{name}".format(name=self.filename))
        os.system(self.args)
        #new_thread = threading.Thread(target=os.system, args=(self.args,))
        #new_thread.start()

    def check_start(self):
        check_file=self.filename+".xltd"
        return os.path.exists(os.path.join(save_path, check_file))

    def check_end(self):
        return os.path.exists(os.path.join(save_path, self.filename))
    '''
    def download(self):
        self.start_target()
        print("正在下载{name}".format(name=self.filename))
        if self.check_start():
            while True:
                time.sleep(60)
                if self.check_end():
                    print("下载完成")
                    return True
        else:
            print("下载失败")
            return False
    '''