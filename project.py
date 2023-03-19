""""
Questions for EDA:
Q:
When percentage of “just right” in “Fit” is less than 50%, then find out which brand, material, shape, neck and length

Q: When percentage of just right  in “Length” is less than 50%, then find out which brand, material, shape and length

Q: Create a table showing brands with average fit, length, transparency and deduce which is the best and worst brand in terms of fitness and length

Q: Find the correlation between fitness and length from customer review


'Gender', 'Category', 'Sub-Category', 'Site_Name', 'Product_URL',
'Brand_Name', 'Product_name', 'Price', 'Image_URLs', 'Ratings',
'Number_of_Ratings', 'Size_and_Dimensions', 'Available_Colors',
'Product_Details', 'Fit_and_Size', 'Material_and_Care',
'Specifications', 'Fit', 'Length', 'Transparency', 'Customer_Images']
"""

import csv

import pandas as pd

import re

read = pd.read_csv('sample.csv')

fitLess50 = []
lengthLess50 = []

class Column():
    fit = read.Fit
    length = read.Length
    brand = read.Brand_Name
    materialAndCare = read.Material_and_Care
    specifications = read.Specifications  #shape, neck and length
    
def extract(row):
        # Material
    if isinstance(Column.materialAndCare[row], str):
        materialLine = Column.materialAndCare[row].split(' | ')
        material = 'Material: ' + materialLine[0]
    else:
        material = 'NA'
        
    # Shape, Neck and Length
    if isinstance(Column.specifications[row], str):
        specificationsLine = Column.specifications[row].split(' | ')
        shape = specificationsLine[0]
        neck = specificationsLine[1]
        splength = specificationsLine[2]
    else:
        shape = 'NA'
        neck = 'NA'
        splength = 'NA'
    
    return [Column.brand[row], material, shape, neck, splength]

def  dataScrap(column, arr):
    for row in range(column.size):
        if isinstance(column[row], str):
            columnRow = column[row].split(' | ')
            justRight = columnRow[2]
            # Just Right Percentage
            percentage = int(justRight[slice(12, len(justRight)-2)])
            
            if percentage < 50:
                data = extract(row)
                arr.append(data)
                
    print(arr)
                

print('\nWhen Percentage of Just Right in Fit is less than 50% \n')
dataScrap(Column.fit, fitLess50)
print('\n\nWhen Percentage of Just Right  in Length is less than 50%\n')
dataScrap(Column.length, lengthLess50)

df = pd.DataFrame(fitLess50)
print(df)