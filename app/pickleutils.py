#!/usr/bin/env python

#Author: Donald Johnson <dj@codetestcode.io>

import pickle


class PickleUtils(object):

    def dict_to_pickle(self, dict_name, file_name, save_to_location):

        output = open( save_to_location + file_name + '.pkl', 'wb')
        pickle.dump(dict_name, output)
        output.close()

    def pickle_to_dict(self, pickle_location, pickle_name):

        pkl_file = open(pickle_location+pickle_name+'.pkl', 'rb')
        data = pickle.load(pkl_file)
        return dict(data)
