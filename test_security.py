import securityfun as sf
import os

def main():
    test_vpath()
    test_fkname()
    test_testrestore()

def test_vpath():
    assert sf.valid_path("cat") == False
    assert sf.valid_path("") == False
    assert sf.valid_path(os.path.join(os.getcwd(),"Test")) == True


def test_fkname():
    files = os.listdir(os.path.join(os.getcwd(),"Test"))
    assert sf.fake_names(files, os.path.join(os.getcwd(),"Test")) == "Fake names are given."

def test_testrestore():
    assert sf.testrestore() == "Done"

if __name__=="__main__":
    main()


