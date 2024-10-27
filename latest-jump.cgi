#!/bin/sh

echo Content-type: text/html
echo
echo '<HTML>'
echo '<HEAD>'
echo '<META HTTP-EQUIV="Pragma" CONTENT="no-cache" >'

echo -n '<META HTTP-EQUIV="refresh" CONTENT="0; URL='
ls -F | grep -E "[0-9][0-9][0-9][0-9][0-9][0-9]/" | tail -n 1 | awk '{print "./"$0}'| tr -d '\n'
echo '">'


echo '</HEAD>'
echo '<BODY>'


echo '</BODY>'
echo '</HTML>'
