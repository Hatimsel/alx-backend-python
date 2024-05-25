#!/usr/bin/python3

import os
import inspect
from utils import get_json


function_path = inspect.getfile(get_json)

absolute_function_path = os.path.abspath(function_path)
print(f"Absolute path: {absolute_function_path}")
