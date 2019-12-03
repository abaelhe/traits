# Copyright (c) 2019 by Enthought, Inc.
# All rights reserved.

import unittest

from traits.api import HasTraits, Int, TraitError
from traits.testing.optional_dependencies import requires_traitsui


@requires_traitsui
class TestViewElements(unittest.TestCase):
    def setUp(self):
        import traitsui.api

        self.toolkit = traitsui.api.toolkit()

    def tearDown(self):
        del self.toolkit

    def test_view_definition(self):
        from traitsui.api import View

        view = View('count')

        class Model(HasTraits):
            count = Int
            my_view = view

        view_elements = Model.class_trait_view_elements()

        self.assertEqual(view_elements.content, {'my_view': view})

    def test_view_definition_twice(self):
        from traitsui.api import View

        view = View('count')

        class Model(HasTraits):
            count = Int
            my_view = view

        view_elements = Model.class_trait_view_elements()
        view_elements2 = Model.class_trait_view_elements()

        self.assertEqual(view_elements.content, {'my_view': view})
        self.assertIs(view_elements, view_elements2)

    def test_view_elements_parents(self):
        from traitsui.api import View

        class Model(HasTraits):
            count = Int
            my_view = View('count')

        class ModelSubclass(Model):
            total = Int
            my_view = View('count', 'total')

        view_elements = ModelSubclass.class_trait_view_elements()
        parent_view_elements = Model.class_trait_view_elements()

        self.assertEqual(view_elements.parents[0], parent_view_elements)

    def test_instance_view_definition(self):
        from traitsui.api import View

        view = View('count')

        class Model(HasTraits):
            count = Int
            my_view = view

        m = Model()
        view_elements = m.trait_view_elements()

        self.assertEqual(view_elements.content, {'my_view': view})

    def test_trait_views(self):
        from traitsui.api import View

        view = View('count')

        class Model(HasTraits):
            count = Int
            my_view = view

        m = Model()
        views = m.trait_views()

        self.assertEqual(views, ['my_view'])

    def test_included_names(self):
        from traitsui.api import Group, Item, View

        item = Item('count', id='item_with_id')
        group = Group(item)
        view = View(Item('count'))

        class Model(HasTraits):
            count = Int
            my_group = group
            my_view = view

        view_elements = Model.class_trait_view_elements()

        self.assertEqual(
            view_elements.content,
            {'my_view': view, 'my_group': group, 'item_with_id': item}
        )

    def test_duplicate_names(self):
        from traitsui.api import Group, Item, View

        class Model(HasTraits):
            count = Int
            includable = Group(Item('count', id='name_conflict'))
            name_conflict = View(Item('count'))

        with self.assertRaises(TraitError):
            Model.class_trait_view_elements()