#!/usr/bin/env python
'''A Bioinformatics Algorithms script containing scoring matrices.'''


class BLOSUM62(object):
    """The BLOSUM62 scoring matrix class."""

    def __init__(self):
        """Initialize the scoring matrix."""
        import os
        import pandas as pd
        # Convert the scoring matrix text file to a data frame.
        self.scoring_matrix = pd.read_table(os.path.join(os.path.dirname(__file__), 'data/BLOSUM62.txt'), sep='  ')

    def __getitem__(self, pair):
        """Returns the score of item1 and item2."""
        return self.scoring_matrix[pair[0]][pair[1]]
