import time
from win10toast import ToastNotifier

Notifi = ToastNotifier() 
localtime = time.asctime( time.localtime(time.time()) )

var_running = 1 
var_sendtime = 1

Notifi.show_toast("Every 15 Seconds", "Started Now! Now minimise the console and do your Daily Work")
print('''
█████████████████████████████████████████████████████████████████████████████████████████
█▄─▄▄─█▄─█─▄█▄─▄▄─█▄─▄▄▀█▄─█─▄███▀░██░▄▄▄███▄─▀█▀─▄█▄─▄█▄─▀█▄─▄█▄─██─▄█─▄─▄─█▄─▄▄─█─▄▄▄▄█
██─▄█▀██▄▀▄███─▄█▀██─▄─▄██▄─▄█████░██▄▄▄▒████─█▄█─███─███─█▄▀─███─██─████─████─▄█▀█▄▄▄▄─█
▀▄▄▄▄▄▀▀▀▄▀▀▀▄▄▄▄▄▀▄▄▀▄▄▀▀▄▄▄▀▀▀▀▄▄▄▀▄▄▄▄▀▀▀▄▄▄▀▄▄▄▀▄▄▄▀▄▄▄▀▀▄▄▀▀▄▄▄▄▀▀▀▄▄▄▀▀▄▄▄▄▄▀▄▄▄▄▄▀
''')
print("[+]: Booted Up, Now minimise the console and do your Daily Work")

while var_running < 6:
	time.sleep(220) #15 Minutes = 300 Seconds, 300 - 80 = 220
	print(f"[+]: Sended Notification to User at {localtime} X{var_sendtime}")
	Notifi.show_toast("Every 15 Seconds", "Time to Relax your Eyes for a Few Seconds", duration=8)
	var_sendtime += 1