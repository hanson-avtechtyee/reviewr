import logging
import datetime
import calendar

from flask import render_template
from flask.ext.appbuilder.models.sqla.interface import SQLAInterface
from flask.ext.appbuilder import ModelView
from app import appbuilder, db
from .models import Document, Checklist, Baseline

log = logging.getLogger(__name__)

def month_year(value):
    return calendar.month_name[value.month] + ' ' + str(value.year)

"""
    Create your Views::


    class MyModelView(ModelView):
        datamodel = SQLAInterface(MyModel)


    Next, register your Views::


    appbuilder.add_view(MyModelView, "My View", icon="fa-folder-open-o", category="My Category", category_icon='fa-envelope')
"""
class DocumentModelView(ModelView):
    datamodel = SQLAInterface(Document)
    add_columns = ['name']
    edit_columns = ['name','url']

class BaselineModelView(ModelView):
    datamodel = SQLAInterface(Baseline)
    add_columns = ['name']
    edit_columns = ['name','url']

class ChecklistModelView(ModelView):
    datamodel = SQLAInterface(Checklist)
    add_columns = ['name']
    edit_columns = ['name','url']

db.create_all()
appbuilder.add_view(DocumentModelView, "Documents", icon="fa-folder-open-o")
appbuilder.add_view(ChecklistModelView, "Checklist", icon="fa-folder-open-o")
appbuilder.add_view(BaselineModelView, "Baseline", icon="fa-folder-open-o")

"""
    Application wide 404 error handler
"""
@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', base_template=appbuilder.base_template, appbuilder=appbuilder), 404

db.create_all()


