from app.lib.objects import Store
import pytest
import msgpack


@pytest.fixture
def store(tmpdir):
    return Store(tmpdir)


def test_initialize(tmpdir, store):
    assert isinstance(store, Store)
    assert store.path == tmpdir.join('store.skppt')


def test_store(tmpdir, store):
    # store.persist('foo', 'bar')
    store.foo = 'bar'

    data_path = tmpdir.join('store.skppt')
    assert store.path == data_path

    with open(data_path, 'rb') as f:
        raw = msgpack.load(f, use_list=False, encoding='utf-8')

        assert store.foo == 'bar'
        assert raw.get('foo') == 'bar'
        assert raw.get('foo') == store.foo
