

from math import ceil

#global_constants
header_length = 20

def main():
	count =0
	print("Input Total Datagram Length :", end=' ')
	total_datagram = int(input())
	data_length = total_datagram - header_length




	print("Input MTU Length :", end=' ')
	total_mtu_length = int(input())
	mtu_data_allowed = total_mtu_length - header_length

	num_fragments = ceil(data_length / mtu_data_allowed)
	print("Number of fragments = {}".format(num_fragments))

	for i in range(num_fragments - 1):
		print("\nFor Fragment '{}'".format(i+1))
		print("Range  = {}-{}".format(mtu_data_allowed*i, mtu_data_allowed*(i+1) - 1))
		print("MF = 1")
		print("TL: {} ".format(mtu_data_allowed))
		count += mtu_data_allowed
		print("Offset = {}".format((mtu_data_allowed // 8) * i))

	print("\nFor Fragment '{}'".format(num_fragments))
	print("Range  = {}-{}".format(mtu_data_allowed*(num_fragments - 1), data_length - 1))
	print("MF = 0")
	print("TL : {}".format(data_length-count))
	print("Offset = {}".format((mtu_data_allowed // 8) * (num_fragments - 1)))

if __name__ == "__main__":
	main()