# Cpu-graph-waybar
This is a litte programme in python can display a little CPU graph on waybar and also other bar and dock 

you have to add this litle programm to /bin/ "sudo cp cpu-graph.py /bin/" and make it executable 
 "sudo chmod 777 /bin/cpu-graph.py" and now its executable

on waybar you have to go to your config file "/etc/xdg/waybar/config.jsonc"
and add for exemple this line at the end:

"custom/cpu-graph": {
  "format": "{}",
  "interval": 1,
  "exec": "cpu-graph.py"
},

and you add "custom/cpu-graph" on the top of the config file with the other fonction

after all that normaly its ok 

PS: sorry for my bad english
