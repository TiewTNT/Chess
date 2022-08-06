from threading import Thread

def xxx():
	print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')

threads = []
for i in range(100):
	threads.append(Thread(target=xxx))

for task in threads:
	task.start()
