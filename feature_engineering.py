#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 01:34:50 2020

@author: synup
"""

import pandas as pd
import numpy as np

file ='synup_locations_data.csv'

df = pd.read_csv(file)
df.info()
isnull(df)