# allows tests to import from code in sibling directory
# (by adding code directory to import path)
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import pidemic
