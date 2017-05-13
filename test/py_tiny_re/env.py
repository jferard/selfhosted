# see http://stackoverflow.com/questions/61151/where-do-the-python-unit-tests-go
import sys
import os

# append module root directory to sys.path
test_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
root_dir = os.path.dirname(test_dir)
src_dir = os.path.join(root_dir, "src")

sys.path.append(src_dir)
