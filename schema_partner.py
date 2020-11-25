# schema.py
from graphene import List
from graphene import Field
from graphene import Float
from graphene import String
from graphene import InputObjectType
from graphene import Schema
from graphene import ID
from graphene import Mutation
from graphene.relay import Node
from graphene_mongo import  MongoengineObjectType
from models_partner import PartnerModel as PartnerModel


class CustomNode(Node):
    class Meta:
        name = 'Node'

    @staticmethod
    def to_global_id(type, id):
        return id


class PartnerAttributes:         
    id=ID()
    tradingName= String()
    ownerName= String()
    document= ID()
    address=List(Float)
    coverageArea=List(List(List(List(Float))))


class PartnerNode(MongoengineObjectType):
    class Meta:
        model = PartnerModel        
        interfaces = (CustomNode, ) 
                
class CreatePartnerInput(InputObjectType, PartnerAttributes):      
    pass 


class CreatePartner(Mutation): 
    partner = Field(lambda: PartnerNode)
    res = String()

    class Arguments:
        input = CreatePartnerInput(required=True)        
 
    def mutate(self, info, input):          
        partner = PartnerModel(**input)  
        res=PartnerModel.objects.filter(id=input.id)
        if res:
            res=False
            return CreatePartner(res='Error:Id is duplicated.') 
        else:
            partner.save()
            res=True
            return CreatePartner(partner=partner, res='ok') 
  


