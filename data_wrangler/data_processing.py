import os
import pandas as pd

DEFAULT_INPUT_PATH = './Olive/input/'
DEFAULT_OUTPUT_PATH = './Olive/input/'
DEFAULT_FILENAME = 'output'


class DataWrangler:
    def __init__(self):
        self.__input_path = DEFAULT_INPUT_PATH
        self.__output_path = DEFAULT_OUTPUT_PATH
        self.__filename = DEFAULT_FILENAME
        self.__csv_files = []
        self.df = pd.DataFrame()

    def __find_csv_files(self):
        files = os.scandir(self.__input_path)
        for file in files:
            if os.path.isfile(file):
                if file.name[-4:].lower() == '.csv':
                    self.__csv_files.append(file.name)

        # if no files are found, raise an exception.
        if len(self.__csv_files) <= 0:
            raise Exception('No CSV files found in {}'.format(self.__input_path))

    def __read_csv_files_into_df(self):
        for file in self.__csv_files:
            df = pd.read_csv(self.__input_path + file)

            # check to make sure there is a timestamp and id column before attempting to sort, and de-dupe.
            assert 'timestamp' in df.columns, "Missing column 'timestamp' in '{}'".format(file)
            assert 'id' in df.columns, "Missing column 'id' in '{}'".format(file)

            df['csv_filename'] = file

            self.df = pd.concat([self.df, df], axis=0)

    def __convert_timestamp_to_datetime(self):
        self.df['timestamp'] = pd.to_datetime(self.df['timestamp'])

    def __sort_and_drop_duplicates(self, most_recent):
        if most_recent:
            self.df = self.df.sort_values(by='timestamp', ascending=False)
        else:
            self.df = self.df.sort_values(by='timestamp', ascending=True)
        self.df = self.df.drop_duplicates(subset='id')
        self.df = self.df.sort_values(by='id', ascending=True)

    def process_csv_files(self, input_path=None, most_recent=True):
        """
        Takes an input path and processes all files ending with a csv format into a concatenated dataframe.

        :param input_path: defaults to './OliveTest/input/'. Can optionally pass a different path to folder of csv files
        to process
        :param most_recent: bool whether to take the most recent id based on the timestamp, or the oldest based on the
        timestamp.
        :return: concatenated, sorted and de-duplicated dataframe
        """

        if input_path:
            self.__input_path = input_path

        self.__find_csv_files()
        self.__read_csv_files_into_df()
        self.__convert_timestamp_to_datetime()
        self.__sort_and_drop_duplicates(most_recent=most_recent)
        # can perform additional logic automatically on the data here, if needed.

        return self.df

    def to_csv(self, output_path=None, filename=''):
        """
        Writes the dataframe out to a csv flat file

        :param output_path: defaults to './OliveTest/input/'. Can optionally pass a different path to folder to write
        csv file to.
        :param filename: optional string to pass to name of the csv file. Defaults to 'output'
        """

        if output_path:
            self.__output_path = output_path

        if filename != '':
            self.__filename = filename

        # auto add '.csv' if it is not part of the passed file name.
        if self.__filename[-4:] != '.csv':
            self.__filename += '.csv'

        self.df.to_csv(self.__output_path + self.__filename)