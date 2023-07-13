#!/bin/bash

cp_flag="yes"


while [ $cp_flag == "yes" ];
do
  echo "enter filename:"
  read firstfile

  echo "enter the destination filename:"
  read secondfile_name

  echo "enter destination path:"
  read dest_path

  cp ${firstfile} ${dest_path}/${secondfile_name} | pv -p -etI


  if [ $? -eq 0 ]    # $? inbuild varaible 
  then 
    echo "successfully entered"
  else
    echo "unsuccessfull"
  fi

  echo "type yes to copy more files else no"
  read cp_flag
done



