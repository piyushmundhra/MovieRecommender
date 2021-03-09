import pandas as pd
import numpy as np
from optpkg.rpkg.recommender import Recommender
from optpkg.userOptions import userOptions

r = Recommender()
print(r.getRecommendation(r.imdbToMovie('0372784')))
