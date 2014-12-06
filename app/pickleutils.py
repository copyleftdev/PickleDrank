#!/usr/bin/env python

#Author: Donald Johnson <dj@codetestcode.io>
# A Set of convertion functions to assist in the conversion of pickle,ini,dictionary
import pprint, pickle


class PickelUtils(object):

    def dict_to_pickle(dict_name, file_name, save_to_location):

        output = open( save_to_location + file_name + '.pkl', 'wb')
        pickle.dump(dict_name, output)
        output.close()

    def read_pickle(pickle_location, pickle_name):

        pkl_file = open(pickle_location+pickle_name+'.pkl', 'rb')
        data = pickle.load(pkl_file)
        pprint.pprint(data)
        pkl_file.close()

