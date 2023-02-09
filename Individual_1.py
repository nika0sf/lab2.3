#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print(*(letter for i, letter in enumerate(input()) if letter == "и" and not i % 2), sep="\n")
