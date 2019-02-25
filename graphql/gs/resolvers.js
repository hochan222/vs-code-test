import { people, getById, getMovies, addMovie } from './db'

const resolvers = {
    Query: {
        people: () => people,
        person: (_,{ id }) => getById(id),
        movies: () => getMovies(),
        movie: (_,{ id }) => getById(id)
    },
    Mutation: {
        addMovie: (_, {name, score})=> addMovie(name, score)
    }
}

export default resolvers;