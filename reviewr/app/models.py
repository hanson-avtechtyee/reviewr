from flask.ext.appbuilder import Model
from flask.ext.appbuilder.models.mixins import AuditMixin, FileColumn, ImageColumn
from sqlalchemy import Column, Integer, String, ForeignKey 
from sqlalchemy.orm import relationship
"""

AuditMixin will add automatic:
    created_on
    changed_on
    created_by
    changed_by

"""

class Document(Model, AuditMixin):
    id = Column(Integer, primary_key=True)
    name = Column(String(12), unique=True, nullable=False)
    url = Column(String(600))
    revision = Column(String(4))

    def __repr__(self):
        return self.name

class Checklist(Model, AuditMixin):
    id = Column(Integer, primary_key=True)
    name = Column(String(12), unique=True, nullable=False)
    url = Column(String(600))
    revision = Column(String(4))

    def __repr__(self):
        return self.name

class Baseline(Model, AuditMixin):
    id = Column(Integer, primary_key=True)
    name = Column(String(12), unique=True, nullable=False)
    url = Column(String(600))
    revision = Column(String(4))

    def __repr__(self):
        return self.name

class Review(Model, AuditMixin):
    id = Column(Integer, primary_key=True)
    baseline_id = Column(Integer, ForeignKey('baseline.id'), nullable=False)
    baseline = relationship("Baseline")
    document_id = Column(Integer, ForeignKey('document.id'), nullable=False)
    document = relationship("Document")

    def __repr__(self):
        return "{0}:{1}:{2}".format(self.baseline, self.document, self.id)

    def month_year(self):
        return datetime.datetime(self.stat_date, year, self.stat_date.month, 1)

