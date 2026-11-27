import os

def test_existe_app():
    assert os.path.exists("app.py")

def test_existen_portadas():
    assert os.path.isdir("portadas")
    assert len(os.listdir("portadas")) >= 4
