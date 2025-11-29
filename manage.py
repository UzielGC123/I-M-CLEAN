#!/usr/bin/env python
import os
import sys

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'IM_CLEAN.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError('Django is required to run this project. Install with: pip install -r requirements.txt') from exc
    execute_from_command_line(sys.argv)
