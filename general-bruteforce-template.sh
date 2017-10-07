#!/usr/bin/env bash

main() {
    pwfile=''

    n=0
    while read -r line; do
        n=$((n+1))
        if crackpw \
               2>/dev/null
        then
            echo 'Found after %s tries:\t%s' "$n" "$line"
            return
        else
            printf 'Trying\t%s\t%s\n' "$n" "$line"
        fi

    done < "$pwfile"
}

main
