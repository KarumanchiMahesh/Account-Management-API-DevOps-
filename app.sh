#!/bin/bash

id=$1
amt=$2
def="account_id"
col=2
row=0
err="false"

while IFS=, read -r field1 field2
do
    row=$(( row + 1 ))
    if [ $# == 1 -a "$id" == "$field1" ]
        then
        err="false"
        echo $field2
        break
    elif [ "$id" == "$field1" ]
        then
        sed -i ""$row"s/.*/"$id,$(($amt+$field2))"/" datastore.csv
        err="false"
        echo $(($amt+$field2))
        break  
    fi
    err="true"
done < datastore.csv

if [ "$err" == "true" -a $# == 1 ]; then
    echo -1
    err="false"
elif [ "$err" == "true" ]
    then
    printf '%s\n' "$id,$amt" | paste -sd ' ' >> datastore.csv
    echo $amt
    err="false"
fi