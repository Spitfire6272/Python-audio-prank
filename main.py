import subprocess
import ctypes
import time
mp3 = "ping.mp3"#replace with your preferred mp3 file.
vlc_path = "C:\Program Files (x86)\VideoLAN\VLC\vlc.exe"#path to my VLC. Replace as required. if broken, put r before "c:"
command = [vlc_path, "--intf", "dummy", mp3]
subprocess.Popen(command, creationflags=subprocess.CREATE_NEW_PROCESS_GROUP)
def maxxer():
    APPCOMMAND_VOLUME_UP = 0xA0000
    WM_APPCOMMAND = 0x319
    hwnd = ctypes.windll.user32.GetForegroundWindow()
    for _ in range(50):
        ctypes.windll.user32.PostMessageW(hwnd, WM_APPCOMMAND, hwnd, APPCOMMAND_VOLUME_UP)
if __name__ == "__main__":
    while True:
        maxxer()
        time.sleep(0.1)
