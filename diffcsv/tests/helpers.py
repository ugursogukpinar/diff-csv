import csv

from faker import Faker


def generate_random_csv(file_path, length=100, change_range=5):
    """

    This method generates csv file which has
    following header

    id,key,value,created_at

    :param file_path:
    :param length:
    :param change_range: how many changes effect on v2
    :return: csv_file
    """

    myFactory = Faker()
    file_v2 = file_path + '_v2'
    generate_count = 0

    with open(file_path, 'w') as csv_file:
        with open(file_v2, 'w') as csv_file_2:

            csv_file_v1 = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csv_file_v2 = csv.writer(csv_file_2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csv_file_v1.writerow(['ID','KEY','VALUE','CREATED_AT'])
            csv_file_v2.writerow(['ID','KEY','VALUE','CREATED_AT'])

            for row in range(length):
                id = row
                key = myFactory.random_number()
                value = myFactory.word()
                created_at = myFactory.date_object()
                csv_file_v1.writerow([id, key, value, created_at])

                if generate_count < change_range + 1:
                    # Deleted
                    pass
                elif generate_count < change_range + 6:
                    # Updated
                    key_2 = myFactory.random_number()
                    value_2 = myFactory.word()
                    csv_file_v2.writerow([id, key_2, value_2, created_at])
                elif generate_count < change_range + 11:
                    # Inserted
                    csv_file_v2.writerow([id + length, key, value, created_at])
                else:
                    csv_file_v2.writerow([id, key, value, created_at])

                generate_count += 1

    return file_path, file_v2