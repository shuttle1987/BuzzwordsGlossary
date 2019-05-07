import typing
from datetime import datetime

from gilbert.content import Templated, Content

class BuzzwordSummary(Templated, Content):
    term: str
    posted: typing.Union[None, datetime]
    template: str = "buzzword.html"
