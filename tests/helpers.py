import csv

from faker import Faker


def generate_random_csv(old_file_path, length=100, change_range=5):
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
    new_file_path = old_file_path + '_v2'
    generate_count = 0

    with open(old_file_path, 'w') as fp_old_csv_file:
        with open(new_file_path, 'w') as fp_new_csv_file:

            old_csv_file = csv.writer(fp_old_csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            new_csv_file = csv.writer(fp_new_csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            old_csv_file.writerow(['ID','KEY','VALUE','CREATED_AT'])
            new_csv_file.writerow(['ID','KEY','VALUE','CREATED_AT'])

            for row in range(1,length):
                id = row
                key = myFactory.random_number()
                value = myFactory.word()
                created_at = myFactory.date_object()
                old_csv_file.writerow([id, key, value, created_at])

                if generate_count < change_range:
                    # Deleted
                    pass
                elif change_range <= generate_count < 2* change_range:
                    # Updated
                    key_2 = key = myFactory.random_number()
                    value_2 = myFactory.word()
                    new_csv_file.writerow([id, key_2, value_2, created_at])
                elif 2 * change_range <= generate_count < 3 *change_range:
                    # Inserted
                    new_csv_file.writerow([id + length, key, value, created_at])
                    new_csv_file.writerow([id, key, value, created_at])
                else:
                    new_csv_file.writerow([id, key, value, created_at])

                generate_count += 1

    return old_file_path, new_file_path