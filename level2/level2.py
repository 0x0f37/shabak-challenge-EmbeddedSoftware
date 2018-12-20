from PIL import Image

def xor_img(img1,img2):
	xor = ''.join([chr(ord(x)^ord(y)) for x,y in zip(img1.tobytes(),img2.tobytes())])
	data = ''.join(xor.split('\0'))
	return data

def xor_index(data,index):
	return ''.join([chr(ord(x)^index) for x in data])

def get_secret(isend,iorg,index):
	img_send = Image.open(isend)
	img_org = Image.open(iorg)
	diff_data = xor_img(img_send,img_org)
	data = xor_index(diff_data,index)
	return data
	
def main():
	s = ''
	s += get_secret('./img0.png','./57cf4c_0bf3bbad5f74409bad0a3a10b1dbd537_mv2.png',0) + '\n'
	s += get_secret('./img1.png','./57cf4c_0aa6e7ffcc024f7ba2b6611f72f2432d_mv2.png',1) + '\n'
	s += get_secret('./img2.png','./57cf4c_56a9ed0fd9c84c98935307aebb4783f7_mv2.png',2) + '\n'
	s += get_secret('./img3.png','./57cf4c_d9f88c5ddc93488d91ac03c56cc901ae_mv2.png',3) + '\n'
	s += get_secret('./img4.png','./57cf4c_4080f95bf84349e5887042c3a06f7114_mv2.png',4) + '\n'
	s += get_secret('./img5.png','./57cf4c_0bf3bbad5f74409bad0a3a10b1dbd537_mv2.png',5) + '\n'
	s += get_secret('./img6.png','./57cf4c_afea1f0bb82348d9bdc24653ea3208f9_mv2.png',6) + '\n'
	s += get_secret('./img7.png','./57cf4c_56a9ed0fd9c84c98935307aebb4783f7_mv2.png',7) + '\n'
	s += get_secret('./img8.png','./57cf4c_0aa6e7ffcc024f7ba2b6611f72f2432d_mv2.png',8) + '\n'
	print s

if __name__ == '__main__':
	main()