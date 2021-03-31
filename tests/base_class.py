""" This is class the base class that all PyTest test will inherit from.
The base class currently takes BROWSER fixture from the confest - any test class that uses the base class
 can use the 'init_driver' fixture in their test """

import pytest


@pytest.mark.usefixtures("init_driver")
class BaseClass:
    pass
