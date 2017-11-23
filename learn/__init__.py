map = {}
map["a"]=1

print map['a']

print '\n travesal list'
# output files
for i, val in enumerate(list):
    # time.strftime('%Y_%m_%d_%H_%M_%S',time.localtime(time.time()))
    file_output = open(
        "monitor_result_%s_%s" % (time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime(time.time())), i), 'w')
    file_output.write(val)
    file_output.close()
    # print ("index %s   value %s" % (i + 1, val))