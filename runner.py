import imp, os.path, sys, time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
import mockingbeat

class MyHandler(PatternMatchingEventHandler):
	patterns = []

	@staticmethod
	def dispatch(event):
		if event.src_path == ifn:
			load()

ifn = ofn = None

def load():
	stdout = sys.stdout
	with file(ofn, 'w') as sys.stdout:
		try:
			reload(mockingbeat)
			mod = imp.load_source(ifn.rsplit('/', 1)[-1].split('.', 1)[0], ifn, file(ifn, 'r'))
		except:
			import traceback
			traceback.print_exc()
	sys.stdout = stdout

def main(_ifn, _ofn):
	global ifn, ofn
	ifn = os.path.abspath(_ifn)
	ofn = _ofn
	MyHandler.patterns.append(ifn)
	load()
	observer = Observer()
	observer.schedule(MyHandler, os.path.dirname(ifn), recursive=True)
	observer.start()
	try:
		while True:
			time.sleep(0.1)
	except KeyboardInterrupt:
		observer.stop()
	observer.join()

if __name__=='__main__':
	main(*sys.argv[1:])
