
Advent of Code is an Advent calendar of small programming puzzles for a variety of skill sets and skill levels that can be solved in any programming language you like. People use them as a speed contest, interview prep, company training, university coursework, practice problems, or to challenge each other.

You don't need a computer science background to participate - just a little programming knowledge and some problem solving skills will get you pretty far. Nor do you need a fancy computer; every problem has a solution that completes in at most 15 seconds on ten-year-old hardware.

If you'd like to support Advent of Code, you can do so indirectly by helping to share it with others, or directly via [PayPal or Coinbase] (https://adventofcode.com/d2021/support).

Advent of Code is a registered trademark in the United States.

## Events

| Year | Mon | Tue | Wed | Thu | Fri | Sat | Sun |
| --- | --- | --- | --- | --- | --- | --- | --- |
|[2015](./y2015/)||[01](./y2015/d01)|[02](./y2015/d02)|[03](./y2015/d03)|[04](./y2015/d04)|[05](./y2015/d05)|[06](./y2015/d06)|
||[07](./y2015/d07)|[08](./y2015/d08)|[09](./y2015/d09)|[10](./y2015/d10)|[11](./y2015/d11)|[12](./y2015/d12)|[13](./y2015/d13)
||[14](./y2015/d14)|15|16|17|18|19|20
||21|22|23|24|25|
||
|[2016](./y2016/)||||[01](./y2016/d01)|[02](./y2016/d02)|[03](./y2016/d03)|[04](./y2016/d04)|
||[05](./y2016/d05)|[06](./y2016/d06)|[07](./y2016/d07)|[08](./y2016/d08)|[09](./y2016/d09)|[10](./y2016/d10)|11|
||12|13|14|15|16|17|18|
||19|20|21|22|23|24|25|
||
|[2017](./y2017/)|||||[01](./y2017/d01)|[02](./y2017/d02)|[03](./y2017/d03)|
||[04](./y2017/d04)|[05](./y2017/d05)|[06](./y2017/d06)|[07](./y2017/d07)|[08](./y2017/d08)|[09](./y2017/d09)|[10](./y2017/d10)|
||[11](./y2017/d11)|[12](./y2017/d12)|13|14|15|16|17|
||18|19|20|21|22|23|24|
||25|
||
|[2018](./y2018/)||||||[01](./y2018/d01)|[02](./y2018/d02)|
||[03](./y2018/d03)|[04](./y2018/d04)|[05](./y2018/d05)|[06](./y2018/d06)|[07](./y2018/d07)|[08](./y2018/d08)|[09](./y2018/d09)|
||[10](./y2018/d10)|[11](./y2018/d11)|[12](./y2018/d12)|13|14|15|16|
||17|18|19|20|21|22|23|24|
||24|25|
||
|[2019](./y2019/)|||||||[01](./y2019/d01)|
||[02](./y2019/d02)|[03](./y2019/d03)|[04](./y2019/d04)|[05](./y2019/d05)|[06](./y2019/d06)|[07](./y2019/d07)|[08](./y2019/d08)|
||[09](./y2019/d09)|[10](./y2019/d10)|[11](./y2019/d11)|[12](./y2019/d12)|13|14|15|
||16|17|18|19|20|21|22|
||23|24|24|25|
||
|[2020](./y2020/)||[01](./y2020/d01)|[02](./y2020/d02)|[03](./y2020/d03)|[04](./y2020/d04)|[05](./y2020/d05)|[06](./y2020/d06)|
||[07](./y2020/d07)|[08](./y2020/d08)|[09](./y2020/d09)|[10](./y2020/d10)|[11](./y2020/d11)|[12](./y2020/d12)|13|
||14|15|16|17|18|19|20|
||21|22|23|24|25|
||
|[2021](./y2021/)|||[01](./y2021/d01)|[02](./y2021/d02)|[03](./y2021/d03)|[04](./y2021/d04)|[05](./y2021/d05)|
||[06](./y2021/d06)|[07](./y2021/d07)|[08](./y2021/d08)|[09](./y2021/d09)|[10](./y2021/d10)|[11](./y2021/d11)|[12](./y2021/d12)|
||[13](./y2021/d13)|[14](./y2021/d14)|[15](./y2021/d15)|[16](./y2021/d16)|[17](./y2021/d17)|[18](./y2021/d18)|[19](./y2021/d19)|
||[20](./y2021/d20)|[21](./y2021/d21)|[22](./y2021/d22)|[23](./y2021/d23)|[24](./y2021/d24)|[25](./y2021/d25)|
||
|[2022](./y2022/)||||[01](./y2022/d01)|[02](./y2022/d02)|[03](./y2022/d03)|[04](./y2022/d04)|
||[05](./y2022/d05)|[06](./y2022/d06)|[07](./y2022/d07)|[08](./y2022/d08)|[09](./y2022/d09)|[10](./y2022/d10)|[11](./y2022/d11)|
||[12](./y2022/d12)|[13](./y2022/d13)|[14](./y2022/d14)|15|16|17|18|
||19|20|21|22|23|24|25|
||

## How to run the sollutions
```
python launch.py --help

    usage: launch.py [-h] [--year YEAR] [--day DAY] [--part PART]

    optional arguments:
    -h, --help   show this help message and exit
    --year YEAR
    --day DAY
    --part PART

python launch.py --year=2021 --day=14 --part=2

    |00|00|00|040| ---------------- START ------------------
    |00|00|00|047| RESULT (2942885922173, 2942885922173)
    |00|00|00|047| ----------------- STOP ------------------
```
All parameters are optional. If one parameter is ommitted, all values for that parameter will be considered.

Running in VSCode terminal is recommended in order to get some basic formatting (colors, special characters).

The second part of the result is static and is used to assert the computed result. The two parts must be identical.

## Credits

Puzzles, Code, & Design: Eric Wastl

Beta Testing:

Tim Giannetti
Ben Lucek
JP Burke
Aneurysm9
Andrew Skalski
Community Managers: Danielle Lucek and Aneurysm9
