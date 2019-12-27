import requests
import threading
from urllib.parse import urljoin
from gtmd.app import app
from gtmd.monitor import monitor
import multiprocessing



from fe import conf

thread: threading.Thread = None
p = multiprocessing.Process(target=monitor)

# 修改这里启动后端程序，如果不需要可删除这行代码
def run_backend():
    # rewrite this if rewrite backend
    app.run()


def pytest_configure(config):
    global thread
    print("frontend begin test")
    p.start()
    thread = threading.Thread(target=run_backend)
    thread.start()


def pytest_unconfigure(config):
    url = urljoin(conf.URL, "shutdown")
    requests.get(url)
    thread.join()
    p.kill()
    print("frontend end test")
