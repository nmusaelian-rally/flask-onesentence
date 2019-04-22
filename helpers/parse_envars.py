'''
take an file argument which represents the name of a yaml file;
if such a file exists in the current directory
open the file, look for the env_variables section
and load the environment with the elements under that section
'''
import os
import yaml

class AppSettings:
    @staticmethod
    def loadEnvironment(filename):
        if os.path.exists(filename):
            with open(filename, "r") as f:
                try:
                    d = yaml.load(f.read())
                    if 'env_variables' in d:
                        for name, value in d['env_variables'].items():
                            #print("%s    %s" % (name, value))
                            os.environ[name] =  str(value)
                except Exception as ex:
                    print(ex)
                    pass
        else:
            pass
            #print("no such file named '%s' in the cwd" % filename)