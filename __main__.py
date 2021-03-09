import pandas as pd
import numpy as np
from optpkg.rpkg.recommender import Recommender
from optpkg.userOptions import userOptions
from optpkg.options1 import Options1
from optpkg.Options2 import Options2

op = Options2()
op.getUserOptions()
op.getUserTaste()
op.giveUserRecs()
op.giveUserRecs()

op = Options1()
op.getUserOptions()
op.getUserTaste()
op.giveUserRecs()
op.giveUserRecs()