import os
import glob
import subprocess
import sys

blenderExecutable = 'blender'

# allow override of blender executable (important for CI!)
if len(sys.argv) > 1:
    blenderExecutable = sys.argv[1]

# iterate over each *.test.blend file in the "tests" directory
# and open up blender with the .test.blend file and the corresponding .test.py python script
errors = []
for file in glob.glob('../tests/**/*.test.blend'):
    print("Starting test " + file)
    try:
        subprocess.check_call([blenderExecutable, '--factory-startup', '-noaudio', '-b', file, '--python', file.replace('.blend', '.py')])
    except:
        errors.append(file)

if errors:
    sys.exit(1)