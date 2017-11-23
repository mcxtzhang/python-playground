import time
import sys

KEY_BEGIN = "Profile data in ms:"
KEY_END = "View hierarchy:"

KEY = "---PROFILEDATA---"
KEY_FRAME_COMPLETE = "FrameCompleted,";

fileName = sys.argv[1]
file_object = open(fileName)
try:
	fileString = file_object.read( )
	#remove useless log
	beginIndex = fileString.index(KEY_BEGIN) + len(KEY_BEGIN)
	endIndex = fileString.index(KEY_END)
	fileString = fileString[beginIndex:endIndex].strip()


	list = []
	

	indexComplete = fileString.find(KEY_FRAME_COMPLETE)
	
	while indexComplete > -1 :

	    temp =""
	
	    profileIndex = fileString.index(KEY);
	    temp =temp + fileString[0 : profileIndex].strip()

	
	    completeIndex = fileString.index(KEY_FRAME_COMPLETE) + len(KEY_FRAME_COMPLETE)
	    secondProfileIndex = fileString.index(KEY, profileIndex + len(KEY))
	    temp = temp + fileString[completeIndex: secondProfileIndex]
	
	    list.append(temp)
	
	    fileString = fileString[secondProfileIndex + len(KEY) : ]

	    indexComplete = fileString.find(KEY_FRAME_COMPLETE)
	    #print(temp)

finally:
	file_object.close( )


print '\n travesal list'
# output files
for i, val in enumerate(list):
	#time.strftime('%Y_%m_%d_%H_%M_%S',time.localtime(time.time()))
	file_output=open("monitor_result_%s_%s" %( time.strftime('%Y_%m_%d_%H_%M_%S',time.localtime(time.time())) , i),'w')
	file_output.write(val)
	file_output.close()
    #print ("index %s   value %s" % (i + 1, val))



