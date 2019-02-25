import { GraphQLServer } from 'graphql-yoga';
import resolvers from "./gs/resolvers";

const server = new GraphQLServer({
    typeDefs: "gs/schema.graphql",
    resolvers 
})

server.start(() => console.log("Grapjqlserver Running"))