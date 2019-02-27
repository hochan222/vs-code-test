import React from "react";
import {Query} from "react-apollo"
import {HOME_PAGE} from "./queries.js"

const Home = () => <Query query={HOME_PAGE}>{ ({loading,data,error}) => {
    if(loading) return 'loading';
    if(error) return 'something happen';
    if(data) {
        return data.movies.map( movie => (<h2 key={movie.id}>{movie.rating} / {movie.title}</h2>));
    }
}}</Query>

export default Home;