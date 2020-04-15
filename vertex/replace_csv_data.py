import os
from datetime import datetime



class ReplaceDataInCSV(object):


    def update_file_with_current_date(self, file_path):

        """ please enter the folder_path separator with '\\' ex: 'C:\\test',
            If param pass action = delete, Delete all files in a directory,
            if param pass action = create, Create empty directory
        :type folder_path: 'str'
        :return True/False
        """

        self.file_path = str(file_path).strip().lower()
        current_date = datetime.today().strftime('%Y%m')
        is_file_updated = False

        if len(self.file_path) > 0:
            if os.path.isfile(self.file_path):
                if self.verify_file_type_csv_or_txt(self.file_path):
                    try:
                        with open(self.file_path, "r") as reader:
                            reader = ''.join([i for i in reader]).replace("######", current_date)
                        with open(self.file_path, 'w') as writer:
                            writer.writelines(reader)
                        print("File updated successfully.")
                        is_file_updated = True
                    except OSError as error:
                        print('Error while updating file. ' + str(error))
            elif os.path.isdir(self.file_path):
                raise TypeError("Only folder path passed. File can't update.".format(file_path))
            else:
                raise TypeError("Error: File not found at '{}'.".format(file_path))
        else:
            raise TypeError("Empty parameter passed.")
        return is_file_updated

    def verify_file_type_csv_or_txt(self, file_path):
        # Ensure the file has the right extension
        self.file_path = str(file_path).strip().lower()
        is_file_csv_or_txt = False
        if not (self.file_path.endswith('.csv') or (self.file_path.endswith('.txt'))):
            raise NameError("File must be a '.csv' or '.txt' extension")
        else:
            is_file_csv_or_txt = True
        return is_file_csv_or_txt

    def update_file_with_current_date2(self, file_path, year='', month=''):

        """ please enter the folder_path separator with '\\' ex: 'C:\\test',
            file type should be .csv or .txt, others type will throw NameError.
        :type file_path: 'str', year=YYYY :'str', month=MM :'str'
        :return True/False
        """
        self.year = str(year).strip().lower()
        self.month = str(month).strip().lower()
        self.file_path = str(file_path).strip().lower()
        current_date = ''
        is_file_updated = False

        if len(self.year) == 0 and len(self.month) == 0:
            current_date = datetime.today().strftime('%Y%m')
        elif len(self.year) == 4 and len(self.month) == 2 and self.month.isnumeric() and self.year.isnumeric():
            current_date = self.year + self.month
        else:
            raise TypeError("Error: Invalid year='{}', month='{}'.".format(year, month))

        if len(self.file_path) > 0:
            if os.path.isfile(self.file_path):
                if self.verify_file_type_csv_or_txt(self.file_path):
                    try:
                        with open(self.file_path, "r") as reader:
                            reader = ''.join([i for i in reader]).replace("######", current_date)
                        with open(self.file_path, 'w') as writer:
                            writer.writelines(reader)
                        print("File updated successfully.")
                        is_file_updated = True
                    except OSError as error:
                        print('Error while updating file. ' + str(error))
            elif os.path.isdir(self.file_path):
                raise TypeError("Only folder path passed. File can't update.".format(file_path))
            else:
                raise TypeError("Error: File not found at '{}'.".format(file_path))
        else:
            raise TypeError("Empty parameter passed.")
        return is_file_updated

"""
    

    def _update_file_date(self):
        year_month = str(datetime.today().strftime('%Y%m'))
        with open("D:\\vertex\\belgium_data_output2.txt", "r") as reader:
            reader = ''.join([i for i in reader]).replace("######", year_month)

        with open("D:\\vertex\\belgium_data_output2.csv", 'w') as writer:
            writer.writelines(reader)

    def _replace_back_csv_data(self):
        year_month = str(datetime.today().strftime('%Y%m'))
        text = open("D:\\vertex\\belgium_data_output.csv", "r")
        text = ''.join([i for i in text]).replace(year_month, "######")
        with open("D:\\vertex\\belgium_data_output.csv", 'w') as writer:
            writer.writelines(text)

"""

c = ReplaceDataInCSV()
print(c.update_file_with_current_date2("c:\\log\\file5.txt"))
#print(c.update_file_with_current_date("D:\\vertex\\belgium_data_output3.png"))

