#Homework 4 Kumar, Sumit

import fileinput
import sys
import argparse
import collections
from operator import itemgetter
from itertools import imap

parser = argparse.ArgumentParser(description='Inventory Management')
parser.add_argument('-f', metavar="File", type=str)
parser.add_argument("actionFile", metavar='FILE', nargs="*", help="File name to read action from")
args = parser.parse_args()

arr=[]
i = 0

def try_int(val):
	try:
		return int(val)
	except ValueError:
		return val


def write_funct(arr):
    myfile = open(args.f,'w')
    myfile.write('PartID\t\tDescription\t\tFootprint\t\tQuantity\n')
    
    for x in arr:
		part = str(x['PartID'])
		description = str(x['Description'])
		footprint =  str(x['Footprint'])
		Quantity = str(x['Quantity'])
		tab = '\t\t'
		value = part + tab + description + tab + footprint + tab + Quantity +'\n'
		myfile.write(value)
	

def add(arr):
			
	d = collections.OrderedDict()		
	d['PartID'] = wrds[2]
	d['Description'] = wrds[4]
	d['Footprint'] = wrds[6]
	d['Quantity'] = wrds[8]			
	arr.append(d)
	write_funct(arr)
	print "\nOK"

def sort(arr):
			newlist = arr
			newlist = sorted(arr, key=lambda k: k[wrds[2]])
			arr=newlist
			write_funct(arr)
			print "OK"	
			
def list():
		try:
		
		 with open(args.f,'r+') as f:
			arr=[]
			i=0
			for line in f:
	   
	 			if i>0:
	 				d = collections.OrderedDict()
					value = line.split()
					d['PartID'] = value[0]
					d['Description'] = value[1]
					d['Footprint'] = value[2]
					d['Quantity'] = value[3]
			
					arr.append(d)
			
				i=i+1
		
			print '\nPartID \t \t','Description\t \t   ','Footprint\t \t','Quantity\t \t'
			if wrds[2]=='with':
				
				for x in arr:
		 			if x[wrds[3]] == wrds[4]:
		 				print x['PartID'],'\t \t', x['Description'],'\t', x['Footprint'],'\t \t', x['Quantity']
		 				
		 	elif wrds[2]=='sort':
				newlist = arr
				print '\n'
				newlist = sorted(arr, key=lambda k: k[wrds[4]])
			
				for x in newlist:
					print x['PartID'],'\t \t', x['Description'],'\t', x['Footprint'],'\t \t', x['Quantity']
		 				
		 	
		except KeyError as e:
		 	print e
		 	
		
		except IndexError:
			for x in arr:
		 		print x['PartID'],'\t \t', x['Description'],'\t', x['Footprint'],'\t \t', x['Quantity']
		 		print '\n'
		 		
def set(arr):
	try:
		 	for x in arr:
		 		if x[wrds[4]] == wrds[5]:
		 			x[wrds[1]] = int(wrds[2])
		 			write_funct(arr)
		 			print "\nOK"
		 					 			
	except KeyError as e:
		 	print e
		 	
def remove(arr):
	try:
			newA = []
			i=0
		 	for x in arr:
		 		if x[wrds[1]] != wrds[2]:
					newA.insert(i,x)
		 			
				i=i+1
			print "\nOK"
			write_funct(newA)
			
					 	 	
		except KeyError:
		 	print "Invalid!"


with open(args.f,'r+') as f:
	for line in f:
	   
	 	if i>0:
	 		d = collections.OrderedDict()
			value = line.split()
			d['PartID'] = value[0]
			d['Description'] = value[1]
			d['Footprint'] = value[2]
			d['Quantity'] = value[3]
			
			arr.append(d)
			
		i=i+1

for line in imap(str.strip, fileinput.input(args.actionFile)):
	wrds = line.split()

#Check if add
	if wrds[0]=='add':
		add(arr)
#Check if remove function has to be called	
	if wrds[0]=='remove':
		remove(arr)
		 	

#Check if set
	if wrds[0]=='set':
		set(arr)
		
#Check if list
	if wrds[0]=='list':
		list()	 	
		 	
#Check if sort
	if wrds[0]=='sort':
		sort(arr)