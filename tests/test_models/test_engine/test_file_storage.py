#!/usr/bin/python3
"""Module for testing FileStorage methods"""
import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from unittest.mock import patch, mock_open
import json


class TestFileStorage(unittest.TestCase):
    """FileStorage test cases"""

    def setUp(self):
        """Initial setup for tests"""
        self.f_stor = FileStorage()
        self.b_model = BaseModel()
        self.json_f = "testFile.json"
        FileStorage._FileStorage__file_path = self.json_f

    def tearDown(self):
        """Cleanup after tests"""
        if os.path.isfile(self.json_f):
            os.remove(self.json_f)

    def test_all_returns_dict(self):
        """Checking if all returns dictionary"""
        output = self.f_stor.all()
        self.assertIsInstance(output, dict)
        self.assertIs(output, self.f_stor._FileStorage__objects)

    def test_storage_objects_exist(self):
        """Check existence of __objects dictionary in FileStorage"""
        self.assertTrue(hasattr(self.f_stor, '_FileStorage__objects'))

    def test_file_path_type_and_value(self):
        """Checks for file path private nature and default value"""
        self.assertEqual(type(self.f_stor._FileStorage__file_path), str)
        self.assertEqual(self.f_stor._FileStorage__file_path, 'testFile.json')

    def test_key_pattern(self):
        """Validating key format as clsname.id"""
        inst_k = f"{type(self.b_model).__name__}.{self.b_model.id}"
        self.assertEqual(inst_k, f"BaseModel.{self.b_model.id}")

    def test_new_method(self):
        """Checking new method of FileStorage adds the object correctly"""
        obj = BaseModel()
        self.f_stor.new(obj)
        inst_k = f"{type(obj).__name__}.{obj.id}"
        self.assertIn(inst_k, self.f_stor._FileStorage__objects)

    def test_save_method(self):
        """Checking save method of FileStorage"""
        with patch("builtins.open", new_callable=mock_open) as m_file:
            self.f_stor.save()
            print(m_file().write.call_args_list)
            c_list = [call[0][0] for call in m_file().write.call_args_list]
            f_cont = "".join(c_list)
            inst_k = f"{type(self.b_model).__name__}.{self.b_model.id}"
            expec_obj = {
                inst_k: {
                    "id": self.b_model.id,
                    "created_at": self.b_model.created_at.isoformat(),
                    "updated_at": self.b_model.updated_at.isoformat(),
                    "__class__": "BaseModel"
                }
            }
            self.assertDictEqual(json.loads(f_cont), expec_obj)

    def test_reload_method(self):
        """Ensuring reload deserialises only if file exists"""
        if os.path.isfile(self.json_f):
            os.remove(self.json_f)
        self.f_stor._FileStorage__objects.clear()
        self.f_stor.reload()
        self.assertEqual(len(self.f_stor._FileStorage__objects), 0)

    def test_base_model_file_update(self):
        """Checking updates in models/base_model.py with storage"""
        with open('models/base_model.py', 'r') as base_f:
            f_content = base_f.read()
            self.assertIn("from models import storage", f_content)

    def test_inst_creation(self):
        """Checking BaseModel __init__ for new instance"""
        inst_k = f"{type(self.b_model).__name__}.{self.b_model.id}"
        self.assertIn(inst_k, self.f_stor.all())

    def test_stor_entry(self):
        """Testing new method of FileStorage"""
        self.f_stor.new(self.b_model)
        inst_k = f"{type(self.b_model).__name__}.{self.b_model.id}"
        self.assertIn(inst_k, self.f_stor.all())

    def test_stor_reload_functionality(self):
        """Checking reload method of FileStorage"""
        self.f_stor.new(self.b_model)
        self.f_stor.save()
        fresh_stor = FileStorage()
        fresh_stor.reload()
        inst_k = f"{self.b_model.__class__.__name__}.{self.b_model.id}"
        self.assertIn(inst_k, fresh_stor.all())

    def test_documentation(self):
        """Checks for class and method documentation in FileStorage"""
        self.assertTrue(len(FileStorage.__doc__) > 0)
        for attr in dir(FileStorage):
            attr_obj = getattr(FileStorage, attr)
            if callable(attr_obj):
                has_d = len(attr_obj.__doc__) > 0
                self.assertTrue(has_d, f"No documentation for {attr} method.")

    def test_permissions(self):
        """Testing r-w-e permissions for file_storage module"""
        f_path = 'models/engine/file_storage.py'
        self.assertTrue(os.access(f_path, os.R_OK))
        self.assertTrue(os.access(f_path, os.W_OK))
        self.assertTrue(os.access(f_path, os.X_OK))
