#!/usr/bin/env bash
PI_DIR=/media/$USER/RPI-RP2
function pi_dir_exists () {
  if [ -d "$PI_DIR" ];
   then return 1
   else return 0
  fi
}
pi_dir_exists
if [ ! $? ];
 then
  mpremote bootloader 2> /dev/null
  echo 'blatted'
fi
pi_dir_exists
while [ ! $? ]
  do sleep 1
  pi_dir_exists
done
cp flash_nuke.uf2 "$PI_DIR"
pi_dir_exists
while [ ! $? ]
  do sleep 1
  pi_dir_exists
done
cp rp2-pico-w-latest.uf2 "$PI_DIR"
echo 'uPython copied - waiting 5 secs'
sleep 5