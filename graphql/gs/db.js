export const people = [
    {
        id: 0,
        name: "hochan",
        age: 18,
        gender: "male"
    },
    {
        id: 1,
        name: "john",
        age: 28,
        gender: "male"
    },
    {
        id: 2,
        name: "min",
        age: 15,
        gender: "male"
    },
    {
        id: 3,
        name: "jun",
        age: 10,
        gender: "female"
    },
    {
        id: 4,
        name: "kei",
        age: 12,
        gender: "female"
    }
];

let movies = [
    {
        id: 0,
        name: "Star Wars - The new one",
        score: 1
    },
    {
        id: 1,
        name: "Avengers - The new one",
        score: 8
    },
    {
        id: 2,
        name: "The Godfather I",
        score: 99
    },
    {
        id: 3,
        name: "Logan",
        score: 2
    },
]

export const getMovies = () => movies;

export const getById = id => {
    const filteredPeople = people.filter(person => person.id === id);
    return filteredPeople[0];
}

export const deleteMovie = (id) => {
    const cleanedMovies = movies.filter(movie => movie.id !== id);
    if(movies.length > cleanedMovies.length) {
        movies = cleanedMovies;
        return true;
    } else {
        return false;
    }
}

export const addMovie = (name, score) => {
    const newMovie = {
        id: `${movies.length +1}`,
        name,
        score
    };
    movies.push(newMovie);
    return newMovie;
}