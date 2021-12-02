import numpy as np
import matplotlib.pyplot as plt

def process_sonar_data(total_bins):
	"""
	Process the given data.
	"""
	print("Beginning processing of festive elvish sonar data...")

	sonar_datafile = 'day1_input_data.csv'
	depths = read_input_data(sonar_datafile)
	# _, binned_y = bin_data(depths, n_bins=total_bins)
	plot_data(depths)

	total_count, pos_slope_pts, neg_slope_pts = find_number_of_increases(depths)

	print(f'...woohoo! {total_count} total depth increasess!')

	slope_plot(pos_slope_pts, neg_slope_pts, total_count)

def read_input_data(datafile):
	"""
	Read data from provided CSV file.
	"""
	data=[]
	with open(datafile, "r") as fin:
		for line in fin:
			num = line.strip('\n').strip(',')
			data.append(int(num))

	# print(len(data))
	return data

def bin_data(unbinned_data, n_bins=100):
	"""
	Optionally, bin the data into given number of bins 
	for visual inspection, with roughly the same number
	of data points per bin. 
	"""
	bins = np.quantile(unbinned_data, np.linspace(0, 1, n_bins+1))
	bin_means = (np.histogram(unbinned_data, bins, weights=unbinned_data)[0] / np.histogram(unbinned_data, bins)[0])

	return bins, bin_means

def plot_data(y, flags=None):
	"""
	Make a scatter plot.
	"""
	x = np.linspace(0, len(y), len(y))

	fig, ax = plt.subplots()
	ax.set_xlabel('Sonar Sweep No.')
	ax.set_ylabel('Seafloor Depth (units ?)')
	ax.set_title('Elves Festive Sonar Data')
	ax.plot(x, y, color='black')

	plt.show()

def slope_plot(y1, y2, total):
	"""
	Make it visually obvious where increases occur.
	"""
	x_ref = np.linspace(0, 2000, 9)        # some messaging to correct x-axis for the piecewise way we're plotting
	x1 = np.linspace(0, len(y1), len(y1))
	x2 = np.linspace(0, len(y2), len(y2))

	fig, ax = plt.subplots()
	ax.set_xlabel('Sonar Sweep No.')
	ax.set_ylabel('Seafloor Depth (units ?)')
	ax.set_title('Highlighting Areas of Increased Depth')
	ax.plot(x1, y1, color='red')
	ax.plot(x2, y2, color='blue')
	ax.set_xticks([int(x*2) for x in x_ref])
	ax.set_xticklabels([int(x) for x in x_ref])
	plt.text(200, 3000, f'Total No. of Increases: {total}')

	plt.show()

def find_number_of_increases(data):
	"""
	Count every time a depth increases,
	regardless if it's a depth we've seen before.
	"""
	total_increases = 0
	positive_slope_pts=[]
	negative_slope_pts=[]

	for i in range(len(data)-1):
		i += 1   
		# I prefer to "look ahead" and go by i directly, 
		# but following example in the instructinos
		if data[i-1] < data[i]:
			total_increases += 1                           
			positive_slope_pts.append(data[i-1])
			positive_slope_pts.append(data[i])   
			# add to positive slope pts (we'll duplicate pts where there are consecutive increases, but no biggie for visual test)  
			negative_slope_pts.append(None)
			negative_slope_pts.append(None)
			# add breaks where the opposite slope occurs

		else:
			# print(f'current depth {data[i]}, next depth {data[i+1]}')
			negative_slope_pts.append(data[i-1])
			negative_slope_pts.append(data[i]) 
			positive_slope_pts.append(None) 
			positive_slope_pts.append(None) 

	return total_increases, positive_slope_pts, negative_slope_pts

if __name__ == '__main__':
	process_sonar_data(100)


