import graphene
from . import queries, mutations

schema = graphene.Schema(query=queries.Query, mutation=mutations.Mutation, auto_camelcase=False)

