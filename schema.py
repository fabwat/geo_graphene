# schema_partner.py
from graphene import List
from graphene import Field
from graphene import Float
from graphene import String
from graphene import ObjectType
from graphene import Schema

from mongoengine import *
    
from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType
from mongoengine import (
    MultiPolygonField, PointField, StringField,IntField,ListField,Document )
#from mongoengine import *
from models_partner import PartnerModel as PartnerModel


import schema_partner

class Query(ObjectType): 
    load_all = List(schema_partner.PartnerNode)
    def resolve_load_all(self,info,id):
        return schema_partner.PartnerModel.objects.get.all()

    load_partner_by_id = Field(schema_partner.PartnerNode, id=String(required=True))
    def resolve_load_partner_by_id(self,info,id):
        return schema_partner.PartnerModel.objects.get(id=id)

    search_partner_near = List(schema_partner.PartnerNode, required=True, ids=List(Float))
    def resolve_search_partner_near(self, info, ids=None):
        if ids:
            coordinates = PointField()    
            coordinates.point = ids       
            #result = schema_partner.PartnerModel.objects(point__geo_within=[20,20])
        result2 = PartnerModel.objects(address__near=coordinates.point,address__max_distance=100)              
        return result2.all()

    search_partner = List(schema_partner.PartnerNode, required=True, ids=List(Float))
    def resolve_search_partner(self, info, ids=None):
        if ids:            
            coordinates = PointField()    
            coordinates.point = ids              
            #result = schema_partner.PartnerModel.objects(point__geo_within=[20,20])
            result2 = PartnerModel.objects(coverageArea__geo_intersects=coordinates.point)                      
            return result2.all()    
        return []       
    
class Mutation(ObjectType):
    create_partner=schema_partner.CreatePartner.Field()    
    

schema = Schema(query=Query,mutation=Mutation)