#!/usr/bin/python3
"""Unit tests for AirBnB project's BaseModel class."""
import unittest
import datetime
import time
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    def setUp(self):
        self.obj1 = BaseModel()
        self.obj2 = BaseModel()

    def tearDown(self):
        del self.obj1
        del self.obj2

    def test_instance(self):
        self.assertIsInstance(self.obj1, BaseModel)

    def test_unique_id(self):
        self.assertNotEqual(self.obj1.id, self.obj2.id)

    def test_attrs_existence(self):
        self.obj1.name = "test name"
        self.assertEqual(self.obj1.name, "test name")
        self.obj1.number = 3
        self.assertEqual(self.obj1.number, 3)

    def test_to_dict_return_type(self):
        ret_dict = self.obj1.to_dict()
        self.assertEqual(type(ret_dict), dict)
        self.assertTrue('id' in ret_dict)

    def test_to_dict_method(self):
        """Validate dictionary representation"""
        obj = BaseModel()
        expec_dict = obj.__dict__.copy()
        expec_dict['__class__'] = type(obj).__name__
        expec_dict['created_at'] = obj.created_at.isoformat()
        expec_dict['updated_at'] = obj.updated_at.isoformat()
        self.assertDictEqual(expec_dict, obj.to_dict())

    def test_datetime_conversion(self):
        obj_dict = self.obj1.to_dict()
        self.assertEqual(type(obj_dict['created_at']), str)
        self.assertEqual(type(obj_dict['updated_at']), str)

    def test_time_update(self):
        """Ensure updated_at changes after save"""
        obj = BaseModel()
        time.sleep(1.5)
        obj.save()
        self.assertTrue(obj.created_at < obj.updated_at)

    def test_updated_at_datetime(self):
        """Test if it changes after save"""
        ori_time = self.obj1.updated_at
        self.obj1.save()
        new_time = self.obj1.updated_at
        self.assertNotEqual(ori_time, new_time)

    def test_str_representation(self):
        obj_type = type(self.obj1).__name__
        obj_str = f"[{obj_type}] ({self.obj1.id}) {self.obj1.__dict__}"
        self.assertEqual(str(self.obj1), obj_str)

    def test_class_attr(self):
        """Ensure __class__ isn't added as an instance attribute."""
        obj = BaseModel(__class__="test class")
        self.assertNotEqual(obj.__class__, "test class")

    def test_datetime_from_kwargs(self):
        """Ensure created_at is processed correctly from keyword arguments"""
        obj = BaseModel(created_at="2002-10-25T15:45:00.000001")
        self.assertEqual(type(obj.created_at), datetime.datetime)

    def test_init_with_kwargs(self):
        obj = BaseModel(
            id="unique_id",
            created_at="2002-10-25T15:45:00.000001",
            updated_at="2002-10-25T15:45:00.000001"
        )
        expected_dict = {
            "__class__": "BaseModel",
            "id": "unique_id",
            "created_at": "2002-10-25T15:45:00.000001",
            "updated_at": "2002-10-25T15:45:00.000001"
        }
        self.assertEqual(obj.to_dict(), expected_dict)
