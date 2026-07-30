#!/usr/bin/env python3
"""Probe script for the test-lab plugin.

Prints where it is running from, so an operator can tell whether a plugin's bundled
scripts execute and whether CLAUDE_PLUGIN_ROOT points at the installed plugin.
"""

import hashlib
import os
import sys

DEFAULT_TEXT = "plugin-test"


def fingerprint(text):
    """Short, deterministic digest, so the caller can verify the output was computed."""
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:16]


def report(argv, env):
    root = env.get("CLAUDE_PLUGIN_ROOT") or "(unset)"
    text = " ".join(argv) or DEFAULT_TEXT
    return "\n".join([
        "plugin root: %s" % root,
        "root exists: %s" % (os.path.isdir(root) if root != "(unset)" else False),
        "script:      %s" % os.path.abspath(__file__),
        "python:      %s" % sys.version.split()[0],
        "input:       %s" % text,
        "fingerprint: %s" % fingerprint(text),
    ])


def selftest():
    assert fingerprint(DEFAULT_TEXT) == "725e6e6bda9f333e", "fingerprint changed"
    assert "plugin root: (unset)" in report([], {}), "unset root not reported"
    assert "input:       hola" in report(["hola"], {}), "argv not used"
    print("selftest ok")


if __name__ == "__main__":
    if "--selftest" in sys.argv[1:]:
        selftest()
    else:
        print(report(sys.argv[1:], os.environ))
