#!/bin/bash

dir=$1
text=$2


output=$(find $dir -type f -print0 | xargs -0 grep "$text" | cut -d: -f1 | uniq)


if [[ "$output" ]]; then
    echo "'$text' is present in:"
    echo "$output"
else
    echo "No results for yout search '$text'"
fi
