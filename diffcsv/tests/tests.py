import csv

from unittest import TestCase, main
from diffcsv.tests.helpers import generate_random_csv

from diffcsv.main import get_diff

class TestDiffCsv(TestCase):

    def setUp(self):
        self.change_counts = 5
        self.csv_file_v1, self.csf_file_v2 = generate_random_csv('/tmp/diff_csv',change_range=self.change_counts)

    def test_get_device_class(self):

        output_file = '/tmp/output.csv'
        with open(output_file, 'w') as f_output:
            get_diff(self.csv_file_v1,self.csf_file_v2, primary_key='ID',output_file= f_output)

        with open(output_file, 'rb') as csvfile:
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

if __name__ == '__main__':
    main()