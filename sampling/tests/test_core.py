from sampling import jackknife, shuffle, Reservoir


def test_jacknife():
    assert tuple(tuple(x) for x in jackknife([1, 2, 3])) == (
        (2, 3), (1, 3), (1, 2))
    assert tuple(tuple(x) for x in jackknife(iter([1, 2, 3]))) == (
        (2, 3), (1, 3), (1, 2))
    assert tuple(tuple(x) for x in jackknife([1, 2, 3], replace=0)) == (
        (0, 2, 3), (1, 0, 3), (1, 2, 0))
    assert tuple(tuple(x) for x in jackknife([])) == ()
    assert tuple(tuple(x) for x in jackknife([1], replace=0)) == ((0,),)


def test_shuffle():
    assert set(shuffle((1, 2, 3))) == set((1, 2, 3))


def test_Reservoir():
    r = Reservoir(2)
    r.add(1)
    assert r.count == 1
    assert r.size == 2
    assert set(r) == set([1])

    r.add(2)
    assert r.count == 2
    assert r.size == 2
    print set(r)
    assert set(r) == set([1, 2])

    r.add(3)
    assert r.count == 3
    assert r.size == 2
    assert tuple(sorted(r)) in ((1, 2), (1, 3), (2, 3))
