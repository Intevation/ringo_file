from sqlalchemy.ext.declarative import declared_attr
import sqlalchemy as sa
from ringo.lib.alchemy import get_relations_from_clazz
from ringo.model import Base
from ringo.model.base import BaseItem, BaseFactory
from ringo.model.mixins import Owned


class FileFactory(BaseFactory):

    def create(self, user=None, values=None):
        new_item = BaseFactory.create(self, user, values)
        return new_item


class File(BaseItem, Owned, Base):
    """Docstring for file extension"""

    __tablename__ = 'files'
    """Name of the table in the database for this modul. Do not
    change!"""
    _modul_id = None
    """Will be set dynamically. See include me of this modul"""

    # Define columns of the table in the database
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column('name', sa.Text, nullable=True, default=None)
    data = sa.Column('data', sa.LargeBinary, nullable=True, default=None)
    description = sa.Column('description', sa.Text,
                            nullable=True, default=None)
    size = sa.Column('size', sa.Integer, nullable=True, default=None)
    mime = sa.Column('mime', sa.Text, nullable=True, default=None)

    custom_1 = sa.Column('custom_1', sa.Integer, nullable=True, default=None)
    """Additional field to the file. Is not used on default but can be
    used by other application if needed. In this case the application
    should overwrite the file form to include the formelement with the
    needed options."""

    @classmethod
    def get_item_factory(cls):
        return FileFactory(cls)

    @property
    def linked(self):
        """Will return a list of all items which are linked to this file
        instance."""
        linked = []
        for relation in get_relations_from_clazz(File):
            if relation.endswith("_items"):
                linked.extend(getattr(self, relation, []))
        return linked


class Filed(object):
    """Mixin to make items of other modules fileable. This means the
    will get a relation named files linked to files attached to the item."""

    @declared_attr
    def files(cls):
        clsname = cls.__name__.lower()
        tbl_name = "nm_%s_files" % clsname
        nm_table = sa.Table(tbl_name, Base.metadata,
                            sa.Column('%s_id' % clsname, sa.Integer,
                                      sa.ForeignKey(cls.id)),
                            sa.Column('file_id', sa.Integer,
                                      sa.ForeignKey("files.id")))
        files = sa.orm.relationship(File, secondary=nm_table,
                                    single_parent=True,
                                    backref="%s_items" % clsname)
        return files
