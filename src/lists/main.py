#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from lists.crew import Lists

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': 'AI LLMs',
        'current_year': str(datetime.now().year)
    }
    
    try:
        Lists().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


