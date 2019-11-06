from irida.model import GraphStructure


class PersonTestNode(GraphStructure):

    def _collect_entity_properties(self):
        pass


class TestGraphStructure:

    # -------------------------------------------------------------------------
    # TEST CASE: LABEL NAME IS EXTRACTED FROM CHILD CLASS NAME
    # -------------------------------------------------------------------------
    def test_label_name_is_extracted_from_child_class_name(self):
        # Prepare
        node = PersonTestNode()
        expected = "PersonTestNode"

        # Act
        actual = node.label

        # Assert
        assert expected == actual
