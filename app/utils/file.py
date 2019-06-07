import os, yaml


class File:
    @staticmethod
    def read(file):
        return open(file, 'r', encoding='utf-8')


class YamlFile:
    @staticmethod
    def read(file):
        return yaml.load(File.read(file))