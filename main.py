from ctypes import *

mqt = CDLL("/home/ek/Repo/git/mosquitto/lib/libmosquitto.so")

major = c_int()
minor = c_int()
revision = c_int()
mqt.mosquitto_lib_version(byref(major), byref(minor), byref(revision))
print(f'{major}.{minor}.{revision}')






