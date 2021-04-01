#!/bin/bash

for i in {1..20}; do
  echo "test $i"
  ./perf.sh &
done
