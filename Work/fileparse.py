# fileparse.py
#
# Exercise 3.3
import csv

'''

def parse_csv(filename):
'''
    # Parsing a csv file into a list of records

'''
    with open(filename) as f:
        rows = csv.reader(f)

        # Read the file headers
        headers = next(rows)
        records = []
        for row in rows:
            if not row:
                continue
            record = dict(zip(headers, row))
            records.append(record)
'''

'''

def parse_csv(filename, coloumn_names):
'''
# Parsing a csv file into a list of records with the only columns that are specified

'''
    with open(filename) as f:
        rows = csv.reader(f)

        # Read the file headers
        headers = next(rows)
        records = []
        # extracting the indices of the coloumn name specified, if no coloumn name is provided entire header list should be populated
        if coloumn_names:
            indices = [headers.index(coloumns) for coloumns in coloumn_names]
            headers = coloumn_names
        else:
            indices = []

        for row in rows:
            if not row:
                continue
            row = [row[index] for index in indices]
            record = dict(zip(headers, row))
            records.append(record)

'''

'''

def parse_csv(filename, coloumn_names, type_conversion):
'''
# Parsing a csv file into a list of records with the only columns that are specified. Type conversion is also done for specific columns mentioned above
'''
    with open(filename) as f:
        rows = csv.reader(f)

        # Read the file headers
        headers = next(rows)
        records = []
        # extracting the indices of the coloumn name specified, if no coloumn name is provided entire header list should be populated
        if coloumn_names:
            indices = [headers.index(coloumns) for coloumns in coloumn_names]
            headers = coloumn_names
        else:
            indices = []

        for row in rows:
            if not row:
                continue
            row = [row[index] for index in indices]
            if type_conversion:
                row = [func(val) for func, val in zip(type_conversion, row)]
            record = dict(zip(headers, row))
            records.append(record)
'''

# working without column names

def parse_csv(filename, coloumn_names, type_conversion, has_headers):
    ''' Parsing a csv file into a list of records with the only columns that are specified. Type conversion is also done for specific columns mentioned above'''
    with open(filename) as f:
        rows = csv.reader(f)

        # Read the file headers
        if has_headers == True:
            headers = next(rows)
            records = []
        # extracting the indices of the coloumn name specified, if no coloumn name is provided entire header list should be populated
            if coloumn_names:
                indices = [headers.index(coloumns) for coloumns in coloumn_names]
                headers = coloumn_names
            else:
                indices = []
                for row in rows:
                    if not row:
                        continue
                    row = [row[index] for index in indices]
                    if type_conversion:
                        row = [func(val) for func, val in zip(type_conversion, row)]
                        record = dict(zip(headers, row))
                        records.append(record)

        else:
            records = []
            for row in rows:
                if not row:
                    continue
                if type_conversion:
                    row = [func(val) for func, val in zip(type_conversion, row)]
                    record = set(zip(row))
                    records.append(record)
    return records
