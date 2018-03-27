import os
import shutil
import json
from unittest import TestCase
from simple_config import Config


test_dir = "test_configs"
test_file = "test_configs/{}.json"


class TestConfig(TestCase):

    def setUp(self):
        if not os.path.exists(test_dir):
            os.mkdir(test_dir)

    def tearDown(self):
        if os.path.exists(test_dir):
            shutil.rmtree(test_dir)

    def test__init__(self):
        file_name = test_file.format("test__init__.json")

        config = Config(file_name, defaults={"jjj": "kkk"})

        self.assertTrue(os.path.exists(file_name))
        self.assertEqual(config.jjj, "kkk")

        with open(file_name, "r") as fi:
            conf = json.loads(fi.read())

            self.assertTrue("jjj" in conf)
            self.assertEqual(conf["jjj"], "kkk")

    def test_update(self):
        # test that update actually saves config changes to the file
        file_name = test_file.format("test_update.json")
        config = Config(file_name, defaults={"jjj": "kkk"})

        ret = config.update(jjj="mmm")

        self.assertTrue(ret is not None)
        self.assertDictEqual(ret, {"jjj": "mmm"})
        self.assertEqual(config.jjj, "mmm")
