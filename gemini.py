import pandas as pd
import numpy as np
from google import genai
import os
from my_gemini import gm_call

answer = gm_call("안녕")
print(answer)