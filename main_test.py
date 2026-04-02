from main import get_by_character,get_by_show

def test_api_get_by_character():
    data = get_by_character("oreki")
    assert data is not None

def test_api_get_by_show():
    data = get_by_show("hyouka")
    assert data is not None