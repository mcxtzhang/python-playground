#!/usr/bin/python
# -*- coding: UTF-8 -*-

import re


class JunkyCounter:
    def __init__(self, source, file_name):
        self.__source = source
        self.__file_name = file_name
        pass

    def print_count(self):
        result = re.split("\s+", src)
        # print result

        count_total = 0
        count_more_17 = 0
        count_more_16 = 0
        count_more_15 = 0
        count_more_14 = 0
        for item in result:
            # print item
            item_result = re.split("=", item)
            # print item_result
            ms = item_result[0][0:-2]
            # print ms

            per_count = int(item_result[1])

            count_total = count_total + per_count

            if int(ms) >= 16:
                count_more_16 = count_more_16 + per_count

            if int(ms) >= 17:
                count_more_17 = count_more_17 + per_count

            if int(ms) >= 15:
                count_more_15 = count_more_15 + per_count

            if int(ms) >= 14:
                count_more_14 = count_more_14 + per_count

        print "-----------%s-----------" % self.__file_name
        print "total_frames:%s" % count_total
        print "count_equals_and_more_17ms:%s" % count_more_17
        print "count_equals_and_more_16ms:%s" % count_more_16


if __name__ == "__main__":
    src = "5ms=272 6ms=80 7ms=71 8ms=71 9ms=57 10ms=44 11ms=35 12ms=36 13ms=25 14ms=21 15ms=19 16ms=17 17ms=65 18ms=28 19ms=11 20ms=12 21ms=7 22ms=7 23ms=7 24ms=7 25ms=3 26ms=5 27ms=2 28ms=5 29ms=5 30ms=8 31ms=8 32ms=8 34ms=4 36ms=3 38ms=7 40ms=6 42ms=7 44ms=2 46ms=4 48ms=8 53ms=6 57ms=7 61ms=4 65ms=6 69ms=6 73ms=5 77ms=2 81ms=2 85ms=5 89ms=7 93ms=2 97ms=1 101ms=1 105ms=0 109ms=1 113ms=2 117ms=1 121ms=2 125ms=2 129ms=3 133ms=1 150ms=24 200ms=14 250ms=8 300ms=16 350ms=7 400ms=8 450ms=11 500ms=5 550ms=6 600ms=4 650ms=1 700ms=0 750ms=3 800ms=3 850ms=0 900ms=0 950ms=3 1000ms=1 1050ms=1 1100ms=0 1150ms=0 1200ms=0 1250ms=0 1300ms=0 1350ms=0 1400ms=0 1450ms=0 1500ms=0 1550ms=0 1600ms=0 1650ms=0 1700ms=0 1750ms=0 1800ms=0 1850ms=0 1900ms=0 1950ms=0 2000ms=0 2050ms=0 2100ms=0 2150ms=0 2200ms=0 2250ms=0 2300ms=0 2350ms=0 2400ms=0 2450ms=0 2500ms=0 2550ms=0 2600ms=0 2650ms=0 2700ms=0 2750ms=0 2800ms=0 2850ms=0 2900ms=0 2950ms=0 3000ms=0 3050ms=0 3100ms=0 3150ms=0 3200ms=0 3250ms=0 3300ms=0 3350ms=0 3400ms=0 3450ms=0 3500ms=0 3550ms=0 3600ms=0 3650ms=0 3700ms=0 3750ms=0 3800ms=0 3850ms=0 3900ms=0 3950ms=0 4000ms=0 4050ms=0 4100ms=0 4150ms=0 4200ms=0 4250ms=0 4300ms=0 4350ms=0 4400ms=0 4450ms=0 4500ms=0 4550ms=0 4600ms=0 4650ms=0 4700ms=0 4750ms=0 4800ms=0 4850ms=0 4900ms=0 4950ms=0"
    c1 = JunkyCounter(src, "log_xiaomi")
    c1.print_count()
    print "Janky frames: 413 (35.66%)"

    src = "5ms=53 6ms=10 7ms=4 8ms=24 9ms=15 10ms=6 11ms=1 12ms=3 13ms=2 14ms=1 15ms=1 16ms=2 17ms=2 18ms=0 19ms=2 20ms=0 21ms=0 22ms=1 23ms=0 24ms=1 25ms=1 26ms=1 27ms=2 28ms=0 29ms=1 30ms=1 31ms=0 32ms=3 34ms=1 36ms=0 38ms=1 40ms=0 42ms=0 44ms=0 46ms=1 48ms=0 53ms=2 57ms=0 61ms=0 65ms=0 69ms=1 73ms=1 77ms=0 81ms=0 85ms=0 89ms=1 93ms=0 97ms=1 101ms=0 105ms=1 109ms=0 113ms=0 117ms=0 121ms=0 125ms=0 129ms=0 133ms=0 150ms=4 200ms=1 250ms=0 300ms=0 350ms=0 400ms=0 450ms=0 500ms=0 550ms=0 600ms=0 650ms=0 700ms=0 750ms=0 800ms=0 850ms=0 900ms=0 950ms=0 1000ms=0 1050ms=0 1100ms=0 1150ms=0 1200ms=0 1250ms=0 1300ms=0 1350ms=0 1400ms=0 1450ms=0 1500ms=0 1550ms=0 1600ms=0 1650ms=0 1700ms=0 1750ms=0 1800ms=0 1850ms=0 1900ms=0 1950ms=0 2000ms=0 2050ms=0 2100ms=0 2150ms=0 2200ms=0 2250ms=0 2300ms=0 2350ms=0 2400ms=0 2450ms=0 2500ms=0 2550ms=0 2600ms=0 2650ms=0 2700ms=0 2750ms=0 2800ms=0 2850ms=0 2900ms=0 2950ms=0 3000ms=0 3050ms=0 3100ms=0 3150ms=0 3200ms=0 3250ms=0 3300ms=0 3350ms=0 3400ms=0 3450ms=0 3500ms=0 3550ms=0 3600ms=0 3650ms=0 3700ms=0 3750ms=0 3800ms=0 3850ms=0 3900ms=0 3950ms=0 4000ms=0 4050ms=0 4100ms=0 4150ms=0 4200ms=0 4250ms=0 4300ms=0 4350ms=0 4400ms=0 4450ms=0 4500ms=0 4550ms=0 4600ms=0 4650ms=0 4700ms=0 4750ms=0 4800ms=0 4850ms=0 4900ms=0 4950ms=0"
    c1 = JunkyCounter(src, "log_sanxing_s8")
    c1.print_count()
    print "Janky frames: 30 (19.74%)"

    src = "5ms=20 6ms=41 7ms=10 8ms=7 9ms=7 10ms=10 11ms=7 12ms=1 13ms=0 14ms=0 15ms=1 16ms=3 17ms=65 18ms=37 19ms=6 20ms=1 21ms=0 22ms=2 23ms=1 24ms=0 25ms=0 26ms=0 27ms=0 28ms=0 29ms=0 30ms=1 31ms=0 32ms=0 34ms=0 36ms=0 38ms=0 40ms=0 42ms=0 44ms=0 46ms=0 48ms=0 53ms=1 57ms=0 61ms=0 65ms=0 69ms=0 73ms=0 77ms=0 81ms=0 85ms=1 89ms=0 93ms=0 97ms=0 101ms=0 105ms=0 109ms=0 113ms=0 117ms=0 121ms=0 125ms=0 129ms=0 133ms=0 150ms=1 200ms=1 250ms=0 300ms=0 350ms=0 400ms=0 450ms=0 500ms=0 550ms=0 600ms=0 650ms=0 700ms=0 750ms=0 800ms=0 850ms=0 900ms=0 950ms=0 1000ms=0 1050ms=0 1100ms=0 1150ms=0 1200ms=0 1250ms=0 1300ms=0 1350ms=0 1400ms=0 1450ms=0 1500ms=0 1550ms=0 1600ms=0 1650ms=0 1700ms=0 1750ms=0 1800ms=0 1850ms=0 1900ms=0 1950ms=0 2000ms=0 2050ms=0 2100ms=0 2150ms=0 2200ms=0 2250ms=0 2300ms=0 2350ms=0 2400ms=0 2450ms=0 2500ms=0 2550ms=0 2600ms=0 2650ms=0 2700ms=0 2750ms=0 2800ms=0 2850ms=0 2900ms=0 2950ms=0 3000ms=0 3050ms=0 3100ms=0 3150ms=0 3200ms=0 3250ms=0 3300ms=0 3350ms=0 3400ms=0 3450ms=0 3500ms=0 3550ms=0 3600ms=0 3650ms=0 3700ms=0 3750ms=0 3800ms=0 3850ms=0 3900ms=0 3950ms=0 4000ms=0 4050ms=0 4100ms=0 4150ms=0 4200ms=0 4250ms=0 4300ms=0 4350ms=0 4400ms=0 4450ms=0 4500ms=0 4550ms=0 4600ms=0 4650ms=0 4700ms=0 4750ms=0 4800ms=0 4850ms=0 4900ms=0 4950ms=0"
    c1 = JunkyCounter(src, "log_rongyao8_7.0")
    c1.print_count()
    print "Janky frames: 118 (52.68%)"

    src = "5ms=36 6ms=15 7ms=7 8ms=4 9ms=3 10ms=1 11ms=1 12ms=4 13ms=1 14ms=1 15ms=2 16ms=0 17ms=1 18ms=0 19ms=0 20ms=0 21ms=0 22ms=0 23ms=0 24ms=1 25ms=0 26ms=0 27ms=1 28ms=0 29ms=0 30ms=0 31ms=0 32ms=0 34ms=0 36ms=0 38ms=0 40ms=0 42ms=0 44ms=0 46ms=0 48ms=0 53ms=0 57ms=0 61ms=0 65ms=0 69ms=0 73ms=0 77ms=0 81ms=0 85ms=0 89ms=0 93ms=1 97ms=0 101ms=0 105ms=0 109ms=0 113ms=0 117ms=0 121ms=0 125ms=0 129ms=0 133ms=0 150ms=1 200ms=1 250ms=1 300ms=0 350ms=0 400ms=0 450ms=0 500ms=0 550ms=0 600ms=0 650ms=0 700ms=0 750ms=0 800ms=0 850ms=0 900ms=0 950ms=0 1000ms=0 1050ms=0 1100ms=0 1150ms=0 1200ms=0 1250ms=0 1300ms=0 1350ms=0 1400ms=0 1450ms=0 1500ms=0 1550ms=0 1600ms=0 1650ms=0 1700ms=0 1750ms=0 1800ms=0 1850ms=0 1900ms=0 1950ms=0 2000ms=0 2050ms=0 2100ms=0 2150ms=0 2200ms=0 2250ms=0 2300ms=0 2350ms=0 2400ms=0 2450ms=0 2500ms=0 2550ms=0 2600ms=0 2650ms=0 2700ms=0 2750ms=0 2800ms=0 2850ms=0 2900ms=0 2950ms=0 3000ms=0 3050ms=0 3100ms=0 3150ms=0 3200ms=0 3250ms=0 3300ms=0 3350ms=0 3400ms=0 3450ms=0 3500ms=0 3550ms=0 3600ms=0 3650ms=0 3700ms=0 3750ms=0 3800ms=0 3850ms=0 3900ms=0 3950ms=0 4000ms=0 4050ms=0 4100ms=0 4150ms=0 4200ms=0 4250ms=0 4300ms=0 4350ms=0 4400ms=0 4450ms=0 4500ms=0 4550ms=0 4600ms=0 4650ms=0 4700ms=0 4750ms=0 4800ms=0 4850ms=0 4900ms=0 4950ms=0"
    c1 = JunkyCounter(src, "log_8.0_nesus_6p")
    c1.print_count()
    print "Janky frames: 7 (8.54%)"

    src = "5ms=14748 6ms=13911 7ms=3487 8ms=4716 9ms=2459 10ms=182 11ms=1134 12ms=1708 13ms=183 14ms=121 15ms=157 16ms=1750 17ms=38618 18ms=4076 19ms=1765 20ms=785 21ms=235 22ms=112 23ms=55 24ms=34 25ms=42 26ms=19 27ms=17 28ms=11 29ms=5 30ms=9 31ms=9 32ms=9 34ms=9 36ms=4 38ms=6 40ms=7 42ms=4 44ms=9 46ms=4 48ms=10 53ms=8 57ms=5 61ms=9 65ms=2 69ms=4 73ms=1 77ms=5 81ms=3 85ms=4 89ms=7 93ms=2 97ms=2 101ms=1 105ms=1 109ms=4 113ms=2 117ms=0 121ms=0 125ms=1 129ms=2 133ms=1 150ms=12 200ms=3 250ms=4 300ms=3 350ms=0 400ms=0 450ms=0 500ms=0 550ms=0 600ms=0 650ms=0 700ms=0 750ms=0 800ms=0 850ms=0 900ms=0 950ms=0 1000ms=0 1050ms=0 1100ms=0 1150ms=0 1200ms=0 1250ms=0 1300ms=0 1350ms=0 1400ms=0 1450ms=0 1500ms=0 1550ms=0 1600ms=0 1650ms=0 1700ms=0 1750ms=0 1800ms=0 1850ms=0 1900ms=0 1950ms=0 2000ms=0 2050ms=0 2100ms=0 2150ms=0 2200ms=0 2250ms=0 2300ms=0 2350ms=0 2400ms=0 2450ms=0 2500ms=1 2550ms=0 2600ms=0 2650ms=0 2700ms=0 2750ms=0 2800ms=0 2850ms=0 2900ms=0 2950ms=0 3000ms=0 3050ms=0 3100ms=0 3150ms=0 3200ms=0 3250ms=0 3300ms=0 3350ms=0 3400ms=0 3450ms=0 3500ms=0 3550ms=0 3600ms=0 3650ms=0 3700ms=0 3750ms=0 3800ms=0 3850ms=0 3900ms=0 3950ms=0 4000ms=0 4050ms=0 4100ms=0 4150ms=0 4200ms=0 4250ms=0 4300ms=0 4350ms=0 4400ms=0 4450ms=0 4500ms=0 4550ms=0 4600ms=0 4650ms=0 4700ms=0 4750ms=0 4800ms=0 4850ms=0 4900ms=0 4950ms=0"
    c1 = JunkyCounter(src, "log_huawei")
    c1.print_count()
    print "Janky frames:frames: 47246 (52.21%)"

    src = "5ms=92 6ms=16 7ms=9 8ms=1 9ms=2 10ms=0 11ms=0 12ms=1 13ms=2 14ms=1 15ms=0 16ms=1 17ms=40 18ms=15 19ms=1 20ms=1 21ms=2 22ms=0 23ms=0 24ms=0 25ms=1 26ms=0 27ms=1 28ms=0 29ms=0 30ms=0 31ms=0 32ms=1 34ms=0 36ms=0 38ms=1 40ms=1 42ms=0 44ms=0 46ms=1 48ms=0 53ms=0 57ms=0 61ms=2 65ms=0 69ms=0 73ms=1 77ms=0 81ms=0 85ms=0 89ms=1 93ms=0 97ms=1 101ms=0 105ms=0 109ms=0 113ms=0 117ms=0 121ms=0 125ms=0 129ms=0 133ms=0 150ms=2 200ms=1 250ms=0 300ms=1 350ms=0 400ms=0 450ms=1 500ms=1 550ms=0 600ms=0 650ms=0 700ms=0 750ms=0 800ms=0 850ms=0 900ms=0 950ms=0 1000ms=0 1050ms=0 1100ms=0 1150ms=0 1200ms=0 1250ms=0 1300ms=0 1350ms=0 1400ms=0 1450ms=0 1500ms=0 1550ms=0 1600ms=0 1650ms=0 1700ms=0 1750ms=0 1800ms=0 1850ms=0 1900ms=0 1950ms=0 2000ms=0 2050ms=0 2100ms=0 2150ms=0 2200ms=0 2250ms=0 2300ms=0 2350ms=0 2400ms=0 2450ms=0 2500ms=0 2550ms=0 2600ms=0 2650ms=0 2700ms=0 2750ms=0 2800ms=0 2850ms=0 2900ms=0 2950ms=0 3000ms=0 3050ms=0 3100ms=0 3150ms=0 3200ms=0 3250ms=0 3300ms=0 3350ms=0 3400ms=0 3450ms=0 3500ms=0 3550ms=0 3600ms=0 3650ms=0 3700ms=0 3750ms=0 3800ms=0 3850ms=0 3900ms=0 3950ms=0 4000ms=0 4050ms=0 4100ms=0 4150ms=0 4200ms=0 4250ms=0 4300ms=0 4350ms=0 4400ms=0 4450ms=0 4500ms=0 4550ms=0 4600ms=0 4650ms=0 4700ms=0 4750ms=0 4800ms=0 4850ms=0 4900ms=0 4950ms=0"
    c1 = JunkyCounter(src, "log_7.0_nova2")
    c1.print_count()
    print "Janky frames: 76 (37.81%)"
