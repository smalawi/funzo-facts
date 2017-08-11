import pandas as pd
import markovify
import random
import pickle

class FactGenerator:
    def __init__(self):
        print "Loading facts..."
        # self.jeo_df = pd.read_csv('data/JEOPARDY_CSV.csv')

        ''' Pickling is worth considering for speeding this up when necessary '''
        # pd.read_csv('data/JEOPARDY_CSV.csv').to_pickle('jeo_df.pickle')
        self.jeo_df = pd.read_pickle('jeo_df.pickle')

    def get_fact(self, count=1):
        train_txt = ""
        indices = random.sample(range(len(self.jeo_df)), 4000)
        for i in indices:
            train_txt += self.jeo_df[' Question'][i] + ": " + self.jeo_df[' Answer'][i] + ". "
            
        text_model = markovify.Text(train_txt)

        facts = []

        for i in range(count):
            facts.append(text_model.make_short_sentence(100))

        return facts
