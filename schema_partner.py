# schema.py
import graphene
from graphene_mongo import  MongoengineObjectType
from models_partner import PartnerModel as PartnerModel
from graphql_relay.node.node import from_global_id

from mongoengine import *

class CustomNode(graphene.Node):
    class Meta:
        name = 'Node'

    @staticmethod
    def to_global_id(type, id):
        return id

class PartnerAttributes:         
    id=graphene.String()
    tradingName= graphene.String()
    ownerName= graphene.String()
    document= graphene.String()
    address=graphene.List(graphene.Float)
    coverageArea=graphene.List(graphene.List(graphene.List(graphene.List(graphene.Float))))


class PartnerNode(MongoengineObjectType):
    class Meta:
        model = PartnerModel            
        interfaces = (CustomNode, ) 
                
class CreatePartnerInput(graphene.InputObjectType, PartnerAttributes):      
    pass 

class CreatePartner(graphene.Mutation): 
    partner = graphene.Field(lambda: PartnerNode)
 
    class Arguments:
        input = CreatePartnerInput(required=True)        
 
    def mutate(self, info, input):        
        partner = PartnerModel(**input)           
        partner.save()
        return f'ok'

    # def resolve_id(self, info):
    #     return self.partnerId  


