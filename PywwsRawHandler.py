"""
    Pypi class
    This object (sic) of this class is to read the raw data created by pywws
"""
__author__ = 'johnburrin'
import string


class PywwsRawHandler:
    def __init__(self):
        """

        :rtype : object
        """
        self.fo = None
        self.data = []

    def open_raw_file(self, f):
        """
        Open a raw file and return file object
        :param f: string
        """

        self.fo = open(str(f), "r")

    def read_raw_line(self):
        """
        :type self: object
        
        Reads the next line form the file object
        """
        line_read = self.fo.readline()
        self.data = string.split(line_read, ",")

    def dump_data(self):
        """
        Plain Old Dump
        """
        print self.data

