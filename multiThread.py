import threading
import subprocess

def runScripts(sn):
    subprocess.run(["python", sn])

if __name__ == "__main__":
    bot1 = threading.Thread(target=runScripts, args=("googleForm.py",))
    bot2 = threading.Thread(target=runScripts, args=("googleForm2.py",))
    bot3 = threading.Thread(target=runScripts, args=("googleForm3.py",))

    bot1.start()
    bot2.start()
    bot3.start()

    bot1.join()
    bot2.join()
    bot3.join()

    print("scripts running ^_^")