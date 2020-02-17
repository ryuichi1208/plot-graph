#!/bin/bash

grep '01/May/2016' /var/log/httpd/access_log | awk '{print $4}' | cut -b 2-15 | sort | uniq -c
