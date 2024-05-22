from marshmallow import fields, validate, validates, ValidationError
from models.entry import Entry
from app_setup import ma
# from schemas.journal_schema import JournalSchema


class EntrySchema(ma.SQLAlchemySchema):
    class Meta:
        model = Entry
        load_instance = True
        fields = ["id", "entry", "date", "journal_id"]

    # journal = fields.Nested(JournalSchema)
    entry = fields.String(validate=validate.Length(min=3, max=3000))
    date = fields.Date(format="%Y-%m-%d")
