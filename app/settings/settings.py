# coding: UTF-8
import os
from os.path import join, dirname
import sys
sys.path.append("/opt/anaconda3/lib/python3.7/site-packages")
from dotenv import load_dotenv


dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

CK = os.environ.get("CONSUMER_KEY")
CS = os.environ.get("CONSUMER_SECRET")
AT = os.environ.get("ACCES_TOKEN")
ATS = os.environ.get("ACCES_TOKEN_SECRET")




