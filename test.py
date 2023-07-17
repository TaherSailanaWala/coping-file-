import pytest
import os
from FirstScript import copy_file_with_progress

def test_case(tmpdir):
    sourcefile=tmpdir.join("source.txt")
    destinationfile=tmpdir.join("destination.txt")

    sourcefile.write("this is a test file")

    source_path=str(sourcefile)
    destination_path=str(destinationfile)

    assert copy_file_with_progress(source_path,destination_path)==True
    assert os.path.exists(destination_path)




