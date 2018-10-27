import mock

from unittest import TestCase
from .helpers import generate_random_csv

from ..main import get_diff

class TestDiffCsv(TestCase):

    def setUp(self):
        self.csv_file_v1, self.csf_file_v2 = generate_random_csv('/tmp/diff_csv')

    def test_get_device_class(self):
        pass