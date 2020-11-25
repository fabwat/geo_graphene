# schema_partner.py
from graphene import List
from graphene import Field
from graphene import Float
from graphene import String
from graphene import ObjectType
from graphene import Schema
from graphene.relay import Node

from mongoengine import (
    MultiPolygonField, PointField, StringField,IntField,ListField,Document )
from models_partner import PartnerModel as PartnerModel
from graphql import GraphQLError
import schema_partner

class Query(ObjectType): 
    load_partner_by_id = Field(schema_partner.PartnerNode, id=String(required=True))
    def resolve_load_partner_by_id(self,info,id):
        return schema_partner.PartnerModel.objects.get(id=id)

    search_partner = Field(schema_partner.PartnerNode, required=True, point=List(Float))
    def resolve_search_partner(self, info, point=None):
        if point:            
            coordinates = PointField()    
            coordinates.point = point              
            #result = schema_partner.PartnerModel.objects(point__geo_within=[20,20])
            nearest = PartnerModel.objects( address__near=coordinates.point)
            covered=PartnerModel.objects( coverageArea__geo_intersects=coordinates.point)
            for item in nearest:
                if item in covered:
                    return item
        raise GraphQLError('No data found')
 
    
class Mutation(ObjectType):
    create_partner=schema_partner.CreatePartner.Field()
    

schema = Schema(query=Query,mutation=Mutation)