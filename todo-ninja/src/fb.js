import firebase from 'firebase/app'
import 'firebase/firestore'

// Initialize Firebase
var config = {
    apiKey: "AIzaSyAvtUW_jmBCqP1_xE3OfUrq7QqoHOjQIjs",
    authDomain: "todo-ninja-8cbc7.firebaseapp.com",
    databaseURL: "https://todo-ninja-8cbc7.firebaseio.com",
    projectId: "todo-ninja-8cbc7",
    storageBucket: "todo-ninja-8cbc7.appspot.com",
    messagingSenderId: "810632048096"
  };
  firebase.initializeApp(config);

  const db = firebase.firestore();

  db.settings({ timestampsInSnapshots: true });

  export default db;