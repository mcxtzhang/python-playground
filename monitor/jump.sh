#!/bin/bash
scheme="dianping://feeddetail?type=1'&'mainid=451230597'&'styletype=1'&'queryid=d6a7bed0-67d5-4f45-a021-7d0169ae29a9'&'videosrc=home_feed"

scheme="dianping://router_feeddetail?type=1'&'mainid=451230597'&'styletype=1'&'queryid=d6a7bed0-67d5-4f45-a021-7d0169ae29a9'&'videosrc=home_feed"

#adb shell am start ${scheme}
adb shell am start "dianping://router_feeddetail?type=1'&'mainid=451230597'&'styletype=1'&'queryid=d6a7bed0-67d5-4f45-a021-7d0169ae29a9'&'videosrc=home_feed"


#adb shell am start "dianping://router_feeddetail?type=29'&'mainid=8195443'&'styletype=1'&'queryid=d6cfd10c-981c-493d-9817-d7e46a78c905'&'videosrc=home_feed"