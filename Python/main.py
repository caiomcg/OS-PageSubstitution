#!/usr/bin/env python

"""
Author: Caio Marcelo Campoy Guedes
E-Mail: caiomcg@gmail.com

License:

MIT License

Copyright (c) 2016 Caio Marcelo Campoy Guedes

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

"""

from Utils import Utils #Import Utils module.

from FIFO import FIFO #Import FIFO module.
from LRU import LRU #Import LRU module.
from OTM import OTM #Import OTM module.

if __name__ == "__main__": #Runs only if main was not imported as a module.
	input = Utils.getData() #Get data from the user.

	fifo = FIFO(input) #Create a FIFO objet.
	lru  = LRU(input) #Create a LRU objet.
	otm  = OTM(input) #Create an OTM objet.

	fifo.run() #Run the algorithm.
	lru.run() #Run the algorithm.
	otm.run() #Run the algorithm.
	
	print(fifo) #Show the object information(missing pages).
	print(otm) #Show the object information(missing pages).
	print(lru) #Show the object information(missing pages).