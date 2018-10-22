import csv
import sys

import numpy as np

def read_csv(file_path, **kwargs):
    with open(file_path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter = kwargs.get('delimitter', ','))
        rows = [row for row in reader]
        columns = rows.pop(0) # get header
        
        # Convert cells which are empty string to None
        rows = np.array(rows)
        rows[rows==''] = None
        rows = rows.tolist()

        return {
            'columns': columns,
            'data': rows
        }

if __name__ == '__main__':
    read_csv(sys.argv[1])
