from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")

        tomldata = toml.loads(content)
        name = tomldata['tool']['poetry']['name']
        description = tomldata['tool']['poetry']['description']
        dependencies = tomldata['tool']['poetry']['dependencies']
        devDependencies = tomldata['tool']['poetry']['dev-dependencies']
        
        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, description, dependencies, devDependencies)
