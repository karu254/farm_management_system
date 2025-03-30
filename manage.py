#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


# openai.api_key = "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"  # Replace with your actual API key



def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'farm_management_system.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
