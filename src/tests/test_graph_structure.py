from irida.model import GraphStructure


class PersonTestNode(GraphStructure):

    def dict_ax(self):
        pass

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class TestGraphStructure:

    # -------------------------------------------------------------------------
    # TEST CASE: LABEL NAME IS EXTRACTED FROM CHILD CLASS NAME
    # -------------------------------------------------------------------------
    def test_label_name_is_extracted_from_child_class_name(self):
        node = PersonTestNode()
        expected = "PersonTestNode"
        actual = node.label
        assert expected == actual

    def test_constructor_kwargs_map_into_object_attributes(self):
        node = PersonTestNode(name="John", last_name="Doe", age=45)
        expected = {
            "name": "John",
            "last_name": "Doe",
            "age": 45
        }
        actual = node.dict
        assert sorted(expected) == sorted(actual)

    def test_attach_property_attaches_a_new_property_correctly(self):
        node = PersonTestNode()
        node._attach_properties(**{"prop": "test"})
        assert "prop" in node.__dict__

    def test_attach_property_attaches_a_new_property_with_correct_value(self):
        node = PersonTestNode()
        node._attach_properties(**{"prop": "test"})
        assert node.__dict__["prop"] == "test"

