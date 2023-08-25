#!/bin/bash

location="${1}"

if [[ -z "${location}" ]] || [[ "${location}" =~ [0-9] ]]; then
  echo 'numeric'
else
  curl https://wttr.in/"${read}"
fi