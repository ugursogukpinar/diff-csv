import sys
import csv
import argparse

from read_csv import read_csv
from database import Sqlite

'''
It's created to find differences between two csv files  
'''
def get_diff(old_csv_file_path, new_csv_file_path, primary_key = 'ID', based_on = []):
    db = Sqlite()
    create_sqlite_table(db, old_csv_file_path, 'old_csv')
    new_csv_file = create_sqlite_table(db, new_csv_file_path, 'new_csv')

    writer = csv.writer(sys.stdout, delimiter=',', quoting=csv.QUOTE_ALL, lineterminator='\r')
    
    # Print new csv file header first
    columns = new_csv_file['columns']
    columns.append('DIFF_STATUS')
    writer.writerow(columns)

    # get rows which presents in old_csv but not in new_csv
    deleted_rows = db.execute('''
        select oc.* from old_csv oc
        left join new_csv nc on (oc.{0} = nc.{0})
        where NC.{0} is NULL
    '''.format(primary_key))

    for row in deleted_rows:
        writer.writerow(list(row) + ['DELETED'])

    # get rows which presents in new_csv but not in old_csv
    inserted_rows = db.execute('''
        select nc.* from new_csv nc
        LEFT join old_csv oc on (nc.{0} = oc.{0})
        where OC.{0} is NULL
    '''.format(primary_key))

    for row in inserted_rows:
        writer.writerow(list(row) + ['INSERTED'])

    if not len(based_on):
        based_on = new_csv_file['columns']
    
    compare_criteria = ['oc.{0} != nc.{0}'.format(based) for based in based_on]

    altered_rows = db.execute('''
        select nc.* from new_csv nc
        left join old_csv oc on (nc.{0} = oc.{0})
        where oc.{0} IS NOT NULL and ({1})
    '''.format(primary_key, ' OR '.join(compare_criteria)))

    for row in altered_rows:
        writer.writerow(list(row) + ['UPDATED'])

def create_sqlite_table(db, csv_file_path, table_name):
    csvfile = read_csv(csv_file_path)
    db.create_table(table_name, csvfile['columns'])
    db.insert_rows(table_name, csvfile['columns'], csvfile['data'])
    return {
        'columns': csvfile['columns']
    }


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('old_csv',  type=str, help='Path of old csv file')
    parser.add_argument('new_csv', type=str, help='Path of new csv file')
    parser.add_argument('--primary-key', type=str, help='Foreign key between two csv files')
    parser.add_argument('--based-on', dest='based_on', nargs='+')
    args = parser.parse_args()
    get_diff(args.old_csv, args.new_csv, primary_key=args.primary_key, based_on=args.based_on)


if __name__ == '__main__':
    main()