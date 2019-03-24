#!/bin/bash

function get_current_time_stamp()
{
echo `date "+%Y/%m/%d %H:%M:%S"`
}

function send_error()
{
echo -e "\e[1;45m [ Error ] `get_current_time_stamp` - $1 -\e[0m"
}

function send_success()
{
echo -e "\e[1;32m [ Success ] `get_current_time_stamp` - $1 -\e[0m"
}

function send_info()
{
echo -e "\e[1;34m [ Info ] `get_current_time_stamp` - $1 -\e[0m"
}

function send_warn()
{
echo -e "\e[1;33m [ Warn ] `get_current_time_stamp` - $1 -\e[0m"
}

export get_current_time_stamp
export send_error
export send_success
export send_info
export send_warn



#项目在Linux平台的初始化脚本；

run_path=$(cd `dirname $0`;pwd)

tmp_path="$run_path/tmp"
log_path="$run_path/log"
script_path="/var/python3/shell"


if [ ! -d "$tmp_path" ];then
    mkdir "$tmp_path"
fi

if [ ! -d "$log_path" ];then
    mkdir "$log_path"
fi

if [ ! -d "$script_path" ];then
    send_error "$script_path not found..."
fi



