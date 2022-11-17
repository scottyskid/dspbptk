

import os
from pathlib import Path

from BaseAction import BaseAction
from Blueprint import Blueprint

class ActionEditsOverride(BaseAction):
    def run(self):

        suffix = '--edit'
        file_extention = 'txt'

        rootdir = Path(self._args.directory)
        file_list = [f for f in rootdir.glob(f'**/*{suffix}.{file_extention}') if f.is_file()]
        print(file_list)

        for file in file_list:
            blueprint_edited = Blueprint.read_from_file(file, validate_hash = True)

            file_to_update = file.parent / (file.name.removesuffix(f'{suffix}.{file_extention}') + '.' + file_extention)
            if file_to_update.is_file():
                blueprint = Blueprint.read_from_file(file_to_update, validate_hash = True)
                blueprint._data = blueprint_edited._data
                blueprint.write_to_file(file_to_update)
                print(f'INFO: updated file {file_to_update}')
            else:
                blueprint_edited.write_to_file(file_to_update)
                print(f'WARN: original file {file_to_update} not found')

            file.unlink()            
