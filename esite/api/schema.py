import graphene

import esite.kisy.schema


class Query(esite.kisy.schema.Query, graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass

schema = graphene.Schema(query=Query)
