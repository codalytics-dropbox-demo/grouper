from fixtures import standard_graph, graph, users, groups, session, permissions  # noqa


def test_basic_metadata(standard_graph, session, users, groups, permissions):  # noqa
    """ Test basic metadata functionality. """

    graph = standard_graph  # noqa

    assert len(users["zorkian"].my_metadata()) == 0, "No metadata yet"

    # Test setting "foo" to 1 works, and we get "1" back (metadata is defined as strings)
    users["zorkian"].set_metadata("foo", 1)
    md = users["zorkian"].my_metadata()
    assert len(md) == 1, "One metadata item"
    assert [d.data_value for d in md if d.data_key == "foo"] == ["1"], "foo is 1"

    users["zorkian"].set_metadata("bar", "test string")
    md = users["zorkian"].my_metadata()
    assert len(md) == 2, "Two metadata items"
    assert [d.data_value for d in md if d.data_key == "bar"] == ["test string"], \
        "bar is test string"

    users["zorkian"].set_metadata("foo", "test2")
    md = users["zorkian"].my_metadata()
    assert len(md) == 2, "Two metadata items"
    assert [d.data_value for d in md if d.data_key == "foo"] == ["test2"], "foo is test2"

    users["zorkian"].set_metadata("foo", None)
    md = users["zorkian"].my_metadata()
    assert len(md) == 1, "One metadata item"
    assert [d.data_value for d in md if d.data_key == "foo"] == [], "foo is not found"

    users["zorkian"].set_metadata("baz", None)
    md = users["zorkian"].my_metadata()
    assert len(md) == 1, "One metadata item"
