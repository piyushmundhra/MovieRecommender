import pandas as pd
import numpy as np
from rpkg.recommender import Recommender

r = Recommender()
print(r.getRecommendation(r.imdbToMovie('0372784')))
