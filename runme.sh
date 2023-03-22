#!/usr/bin/env bash

pyver=python3.8
venv=.venv

if [[ ! -e $venv ]]; then
    $pyver -m venv .venv
    . $venv/bin/activate
    pip install -U pip
    pip install -r requirements.txt
    pushd package
    pip install -e .
    popd
else
    . $venv/bin/activate
fi


echo ""
echo "Running example:"
echo ""
python runme.py