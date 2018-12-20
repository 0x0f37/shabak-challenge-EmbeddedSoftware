import struct
import time

class Data():
	def __init__(self,a,lenght,data):
		self.a=a
		self.lenght=lenght
		self.data=data
		assert(len(self.data) == self.lenght) #for sanity check - never trust data from user
		self.res=''
		if self.a == '\0':
			self.parse1()
		elif self.a == '\1':
			self.parse2()
		else:
			self.parse_int()
			
	def get_type(self):
		return ord(self.a)
		
	def __str__(self):
		return str(self.res)
	
	def parse1(self):
		if not self.data or self.lenght != 8:
			return
		self.res=struct.unpack("<II",self.data)
		
	def parse2(self):
		if not self.data or self.lenght != 8:
			return
		self.res=struct.unpack("<ff",self.data)
		
	def parse_int(self):
		self.res= str(ord(self.a))+' '+str(self.lenght)

def read_file():
	f=open(r"./external_mem_dump.bin","rb")
	data=f.read()
	f.close()
	return data

def parse_data(data):
	res=[]
	while len(data)>= 5:
		(a,lenght,)=struct.unpack("<cI",data[0:5])
		if lenght > 8 : #ignor
			#print hex(ord(data[0])),hex(ord(data[1])),hex(ord(data[2])),hex(ord(data[3])),hex(ord(data[4])),hex(ord(data[5]))
			data = data[5:]
			continue
		data = data[5:]
		d = data[:lenght]
		data = data[lenght:]
		res += [Data(a,lenght,d)]
		
	return res
	
def parse_time_to_sec(t):
	return time.mktime(time.strptime(str(t),"(%H%M%S, %d%m%y)"))

def main():
	data = read_file()
	res = parse_data(data)
	diff_time =  75*4
	t = 0
	change_to = 15*4
	end_time=parse_time_to_sec("(012100, 301018)")

	for (i,x) in enumerate(res):
		if x.get_type() == 0:  #RESET
			t = parse_time_to_sec(x)
			diff_time = 75*4
			change_to = 15*4
		elif x.get_type() == 1 : #LOCATION
			print x
			t += diff_time
			diff_time = change_to
			if t >= end_time:
				print 'location: ',x
				return
				
		elif x.get_type() == 2 : #EVERY 15 *4sec
			change_to = 15*4
		elif x.get_type() == 3 : #EVERY 150 *4sec
			change_to = 150*4
		else:
			assert(False)
			

if __name__=='__main__':
	main()