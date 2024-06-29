import unittest


class TestValidators(unittest.TestCase):

    def test_validate_bool(self):
        from validators.validators import validate_is_bool
        assert validate_is_bool("True")
        assert validate_is_bool("False")
        assert not validate_is_bool("custom")

    def test_validate_other(self):
        from validators.validators import validate_is_other
        assert validate_is_other(str, "string")
        assert validate_is_other(int, "1234")
        assert validate_is_other(bool, "True")
        assert not validate_is_other(int, "aaa")

    def test_validate_property(self):
        from validators.validators import validate_property
        from model.employee import Employee
        assert validate_property(Employee, "surname", "Smith")
        assert validate_property(Employee, "name", "John")
        assert validate_property(Employee, "age", 123)
        assert validate_property(Employee, "profession", "plumber")
        assert not validate_property(Employee, "hired", "custom")
        assert not validate_property(Employee, "age", "custom")
        assert not validate_property(Employee, "year_of_birth", 1234)
