#!/usr/bin/env bash
echo "begin start activity...."
#接受参数 启动scheme
scheme=$1
adb shell am start -a android.intent.action.VIEW -d $scheme
sleep 5s

python monitor_adb.py $scheme


#
#
#fileNum=1
#for((i=1;  ;i++))
#do
#   echo "begin swipe...."
#   adb shell input swipe 800 800 200 200
#   if [ $i == 3 ]
#   then
#   i=1;
#
#   echo "begin dumpsys and save...."
#   adb shell dumpsys gfxinfo com.dianping.v1 reset framestats > /Users/zhangxutong/docs/logs/log$fileNum
#   ((fileNum++));
#   fi
#done

