from peakalgorithm import detect_peaks
from Datacollector import collector


def peakfinder():
	

	ecgd = collector()

	myindices = detect_peaks(ecgd)

if __name__ == '__main__':
	peakfinder()
