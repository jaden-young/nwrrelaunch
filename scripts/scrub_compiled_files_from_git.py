#!/usr/bin/env python3
"""Run git rm --cached $f for each *_c compiled file"""

import subprocess

from pathlib import Path


repo_root = Path(__file__).parent.parent

compiled_formats = [
    ".vmat_c",
    ".vagrp_c",
    ".vmesh_c",
    ".vmdl_c",
    ".vtex_c",
    ".vsnd_c",
    ".vsndevts_c",
    ".vpcf_c",
    ".vanim_c",
    ".vxml_c",
    ".vcss_c",
]

maybe_compiled_paths = repo_root.glob("**/*_c")
compiled_paths = [p for p in maybe_compiled_paths if p.suffix in compiled_formats]
for p in compiled_paths:
    # slow but this script should only need to be run once
    subprocess.run(["git", "rm", "--cached", p])
