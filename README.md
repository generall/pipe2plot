# pipe2plot
Plotting data from pipe/files using matplotlib http://matplotlib.org/.

It is a simple interface for plotting data from pipe or files. This tool may be useful for exploratory data analysis.

## Use cases

The tool displays data from multiple files or from pipe in online mode.

### Example: from files

```
$ ./pipe2plot.py f1 f2
```

where f1 and f2 - some files. E.g.:
f1:
```
1 2
2 2
3 2
4 2
5 2
...
```
<img src=https://raw.github.com/generall/pipe2plot/master/screenshots/scr_1.png width=50% height=50% />

### Example: from pipe

Example of plotting ping times in real time:
```
$ ping 127.0.0.1 | stdbuf -oL awk '{print $7}' | ./pipe2plot.py -d =
```
`stdbuf -oL` is used for cancel pipe buffering.

<img src=https://raw.github.com/generall/pipe2plot/master/screenshots/scr_2.png width=50% height=50% />

## Availible flags
```
Usage: pipe2plot.py [options] [files (default = stdin)]
-i           NOT Ignore unparsed values;
-b int       Buffer size ( default = infinity );
-t val       <not implemented> Template for line e.g. "x1 y1 x2 y2" (default="y1 y2 y3 ..." );
-d val       Delimeter regexp ( default = "\s+" );
-s val       Style of grafs according to matplotlib;
```
