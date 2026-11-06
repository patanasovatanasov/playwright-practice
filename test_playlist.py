import pytest
from _pytest import raises

from playlist import Playlist

def test_adding_songs():
    rock = Playlist("Рок")
    assert rock.pl == "Рок"
    assert rock.count() == 0

def test_dif_playlists_song_count():
    rock = Playlist("Рок")
    jazz = Playlist("Джаз")
    rock.add_song("Песен 1")
    rock.add_song("Песен 2")

    assert rock.count() == 2
    assert jazz.count() == 0

def test_max_3_songs():
    rock = Playlist("Рок")

    rock.add_song("Песен 1")
    rock.add_song("Песен 2")
    rock.add_song("Песен 3")

    assert rock.count() == 3
    with pytest.raises(ValueError):
        rock.add_song("Песен 4")
    assert rock.count() == 3