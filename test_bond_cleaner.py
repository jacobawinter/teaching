
import camelot
import pandas as pd
import re
import os


os.chdir("/Users/jacobwinter/Library/CloudStorage/Dropbox/Documents/Projects/Tax_or_Tap_Zambia/01_Data/local_borrowing/ZMB_TBOND_raw")


files = os.listdir()

# Filter out only PDF files
pdf_files = [file for file in files if file.endswith('.pdf')]
#doc_files = [file for file in files if file.endswith('.docx')]

pdf = pdf_files[0]

df = camelot.read_pdf(pdf, pages='1')[0].df
#First row to be the header
df[0] = df[0].str.replace('\n', ' ')

df.columns = df.iloc[0]
df = df[1:]
df['year'] = re.search(r'\d{4}', pdf).group(0)
df['month'] = re.search(r'-\d{2}-', pdf).group(0)
df['month'] = df['month'].str.replace('-', '')

df