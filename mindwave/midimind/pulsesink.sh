#!/bin/bash

pacmd load-module module-pipe-sink file=/tmp/pulse.fifo
pacmd load-module module-combine-sink slaves=yoursink,fifo_output
pacmd set-default-sink combined


pcm.writeFile {
      type file
      slave.pcm null
      file "/tmp/alsa.fifo"
      format "raw"
}

pactl load-module module-null-sink sink_name=<midimind_monitor> file=/tmp/midimind.fifo
