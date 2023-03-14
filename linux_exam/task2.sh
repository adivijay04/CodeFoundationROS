#!/bin/bash

arg1=$1

if [ $arg1 == 'small_square' ]; then
    rosrun linux_exam small_square.py

elif [ $arg1 == 'medium_square' ]; then
    rosrun linux_exam medium_square.py

elif [ $arg1 == 'big_square' ]; then
    rosrun linux_exam big_square.py
fi
