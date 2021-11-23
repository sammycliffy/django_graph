import graphene
from graphene_django import DjangoObjectType, DjangoListField 
from .models import *
from graphql_auth.schema import UserQuery, MeQuery


class PartyMemberType(DjangoObjectType):
    class Meta:
        model = PartyMembers
        fields = '__all__'

class PredictionType(DjangoObjectType):
    class Meta:
        model = RandomForest
        fields = '__all__'


class PartyMemberInput(graphene.InputObjectType):
        username = graphene.String(required=True)
        full_name = graphene.String(required=True)
        email = graphene.String(required=True)
        phone_number = graphene.String(required=True)
        dateOfBirth = graphene.String(required=True)
        sex = graphene.String(required=True)
        maritalStatus =graphene.String(required=True)
        qualification = graphene.String(required=True)
        noOfPosition = graphene.String(required=True)
        attendance = graphene.String(required=True)
        performance = graphene.String(required=True)
        contribution = graphene.String(required=True)
        duration = graphene.String(required=True)
        partyName = graphene.String(required=True)
        partyCode = graphene.String(required=True)
        wardCode = graphene.String(required=True)
        votersPin = graphene.String(required=True)
        position = graphene.String(required=True)

class RandomForestInput(graphene.InputObjectType):
     attendance = graphene.String(required=True)
     loyalty = graphene.String(required=True)
     contribution = graphene.String(required=True)
     noOfPosition = graphene.String(required=True)
     classification = graphene.String()
     duration = graphene.String(required=True)

    
     

class PerformRandomForest(graphene.Mutation):
    class Arguments:
        test_data = RandomForestInput()
    test_class = graphene.Field(PredictionType)

    @staticmethod
    def mutate(root, info, test_data=None):
        print(test_data.attendance, test_data.loyalty, test_data.contribution,
        test_data.noOfPosition, test_data.duration
        )

        classification = 0
        if int(test_data.attendance) >= 50 and int(test_data.loyalty) >= 5 and int(test_data.contribution) >= 40 and int(test_data.noOfPosition) >= 1 and int(test_data.duration) >= 2:
         classification = 1
        party_instance = RandomForest(
    
    attendance = test_data.attendance,
     loyalty = test_data.loyalty,
     contribution = test_data.contribution,
     noOfPosition=test_data.noOfPosition,
     duration = test_data.duration,
     classification = classification
        )
        party_instance.save()
        return PerformRandomForest(test_class = party_instance )


class CreatePartyMember(graphene.Mutation):
    class Arguments:
        party_data = PartyMemberInput()
    partyMember = graphene.Field(PartyMemberType)

    @staticmethod
    def mutate(root, info, party_data=None):
        username = party_data.username
        PartyMembers.objects.filter
        party_instance = PartyMembers(
            username = party_data.username,
            full_name = party_data.full_name,
            email = party_data.email,
            phone_number=party_data.phone_number,
            dateOfBirth=party_data.dateOfBirth,
            sex=party_data.sex,
            maritalStatus =party_data.maritalStatus,
            qualification = party_data.qualification,
            noOfPosition = party_data.noOfPosition,
            attendance = party_data.attendance,
            performance = party_data.performance,
            contribution = party_data.contribution,
            duration = party_data.duration,
            partyName = party_data.partyName,
            partyCode = party_data.partyCode,
            wardCode=party_data.wardCode,
            votersPin = party_data.votersPin,
            position = party_data.position
        )
        party_instance.save()
        return CreatePartyMember(partyMember=party_instance)
         
class Mutation(graphene.ObjectType):
    create_partyMember = CreatePartyMember.Field()
    random_mutation  =  PerformRandomForest.Field()


class Query(UserQuery, MeQuery, graphene.ObjectType):
    all_partyMembers = DjangoListField(PartyMemberType)
    partymember = graphene.Field(PartyMemberType, username=graphene.String())

    def resolve_all_partyMembers(self, info, **kwargs):
        return PartyMembers.objects.all()
    
    def resolve_partymember(root, info, username):
        return PartyMembers.objects.get(username=username)

    


schema = graphene.Schema(query=Query, mutation=Mutation)

