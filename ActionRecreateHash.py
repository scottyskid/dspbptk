

import os
from BaseAction import BaseAction
from Blueprint import Blueprint

class ActionRecreateHash(BaseAction):
	def run(self):
		if (not self._args.force) and os.path.exists(self._args.outfile):
			print("Refusing to overwrite: %s" % (self._args.outfile))
			return 1

		bp = Blueprint.read_from_file(self._args.file, validate_hash = False)
		bp.write_to_file(self._args.file)
