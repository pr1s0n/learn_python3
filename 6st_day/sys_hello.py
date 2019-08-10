#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import sys
'a test module'
__author__ = 'pr1s0n'
def test():
	args = sys.argv
	if len(args) == 1:
		print("hello,world!")
	elif len(args) == 2:
		print("hello,%s!" % args[1])
	else:
		print("too many args!")
if __name__ == '__main__':
	test()