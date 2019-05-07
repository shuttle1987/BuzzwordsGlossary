import typing
from datetime import datetime

from gilbert.content import Templated, Content

class BuzzwordSummary(Templated, Content):
    term: str
    posted: datetime = datetime.now()
    template: str = "buzzword.html"
