import csv
import os

from unittest import TestCase

from tests.helpers import generate_random_csv
from diffcsv.main import get_diff

class TestDiffCsv(TestCase):
    def test_five_difference_for_each_diff_type(self):
        self.change_counts = 5
        self.old_csv_file, self.new_csv_file = generate_random_csv('/tmp/diff_csv', change_range=self.change_counts)

        output_file = '/tmp/output.csv'
        with open(output_file, 'w') as f_output:
            get_diff(self.old_csv_file,self.new_csv_file, primary_key='ID',output_file= f_output)

        with open(output_file, 'r') as csvfile:
            csv_reader = csv.DictReader(csvfile, delimiter=',')
            change_counts = {
                "DELETED": 0,
                "UPDATED": 0,
                "INSERTED": 0,
            }

            for row in csv_reader:
                change_counts[row['DIFF_STATUS']]+=1

            self.assertEqual(change_counts['DELETED'], self.change_counts)
            self.assertEqual(change_counts['UPDATED'], self.change_counts)
            self.assertEqual(change_counts['INSERTED'], self.change_counts)

        os.remove(self.old_csv_file)
        os.remove(self.new_csv_file)
        os.remove(output_file)