import pytest

def test_empty_playlist(rock):
    assert rock.count() == 0

def test_full_count(full_rock):
    assert full_rock.count() == 3

def test_4th_song(full_rock):
    with pytest.raises(ValueError):
        full_rock.add_song("song4")

def test_two_fixtures(rock, full_rock):
    assert rock.count() == 3
    assert full_rock.count() == 3