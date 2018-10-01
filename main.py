from win_gui.main_gui import *
from thunder.dytt_thunder import *
from message_spider.dytt_spider import *
from message_spider.spider_config import url_dytt

import threading

urls = []
link_message = ""
urls_index = 0

def get_urls_and_linkmessage(spider):
    global urls
    global link_message
    for x in spider.get_all_thunderlink():
        link_message += x["影片名："]
        link_message += "\n"
        link_message += x["磁力链接："]
        link_message += "\n\n"
        urls.append(x['磁力链接：'])

def change_entry_a(entry):
    global urls_index
    if urls_index == 0:
        urls_index = len(urls) - 1
    else:
        urls_index = urls_index - 1
    entry.delete(0, END)
    entry.insert(20, urls[urls_index])

def change_entry_b(entry):
    global urls_index
    if urls_index ==len(urls)-1:
        urls_index = 0
    else:
        urls_index = urls_index + 1
    entry.delete(0,END)
    entry.insert(20,urls[urls_index])

def download_current():
    thunder = my_thunder(urls[urls_index])
    #new_thread = threading.Thread(target=thunder.download)
    new_thread = threading.Thread(target=thunder.start_target)
    new_thread.start()
    #thunder.download()

def mainGUI_config(mainWin):
    # INSERT索引表示在光标处插入,END索引号表示在最后插入
    mainWin.entry_01.insert(END, url_dytt)
    mainWin.text_01.insert(1.0, link_message)
    mainWin.entry_02.insert(20, urls[0])
    mainWin.btn_01.config(command=lambda: change_entry_a(mainWin.entry_02))
    mainWin.btn_02.config(command=lambda: change_entry_b(mainWin.entry_02))
    mainWin.btn_03.config(command=download_current)

def main():
    print("++++主程序启动++++")
    mainWin = MainGUI()
    spider = dytt_spider()

    get_urls_and_linkmessage(spider)
    mainGUI_config(mainWin)
    mainWin.open_gui()

if __name__ =="__main__":
    main()