# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 13:32:55 2021

@author: shobhit deshwal
"""

import glassdoor_scrapper as gs
import pandas as pd

path = "C:/Users/shobhit deshwal/Desktop/Ken_Jee_salary_pred/chromedriver_win32/chromedriver"


df = gs.get_jobs('data scientist', 15 , False, path, 15)