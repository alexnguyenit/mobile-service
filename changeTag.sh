#!/bin/bash

sed "s/tagVersion/$1/g" kubefile.yml > kubefile-done.yml