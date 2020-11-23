#models_partner.py
from mongoengine import (
    MultiPolygonField, PointField, StringField,IntField,ListField,Document
)

class PartnerModel(Document):
    meta = {'collection': 'partner_location'}    
    id = StringField(primary_key=True)
    tradingName=StringField()
    ownerName=StringField()
    document=StringField(unique=True)
    address=PointField()
    coverageArea=MultiPolygonField()   

    


