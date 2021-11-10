import graphene
from graphene_django import DjangoObjectType, DjangoListField 
from .models import PartyMembers


class PartyMemberType(DjangoObjectType):
    class Meta:
        model = PartyMembers
        fields = '__all__'

class PartyMemberInput(graphene.InputObjectType):
        full_name = graphene.String(required=True)
        email = graphene.String(required=True)
        phone_number = graphene.String(required=True)
        qualification = graphene.String(required=True)
        no_of_position = graphene.String(required=True)
        attendance = graphene.String(required=True)
        performance = graphene.String(required=True)
        contribution = graphene.String(required=True)
        duration = graphene.String(required=True)
        loyalty = graphene.String(required=True)
        partyName = graphene.String(required=True)
        partyCode = graphene.String(required=True)
        wardCode = graphene.String(required=True)


class CreatePartyMember(graphene.Mutation):
    class Arguments:
        party_data = PartyMemberInput()

    partyMember = graphene.Field(PartyMemberType)

    @staticmethod
    def mutate(root, info, party_data=None):
        party_instance = PartyMembers( 
            full_name = party_data.full_name,
            email = party_data.email,
            phone_number = party_data.phone_number,
            qualification = party_data.qualification,
            no_of_position = party_data.no_of_position,
            attendance = party_data.attendance,
            performance = party_data.performance,
            contribution = party_data.contribution,
            duration = party_data.duration,
            loyalty = party_data.loyalty,
            partyName = party_data.partyName,
            partyCode = party_data.partyCode,
            wardCode = party_data.wardCode
        )
        party_instance.save()
        return CreatePartyMember(partyMember=party_instance)
         
class Mutation(graphene.ObjectType):
    create_partyMember = CreatePartyMember.Field()


class Query(graphene.ObjectType):
    all_partyMembers = graphene.List(PartyMemberType)

    def resolve_all_books(self, info, **kwargs):
        return PartyMemberType.objects.all()






schema = graphene.Schema(query=Query, mutation=Mutation)

