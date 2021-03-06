import * as firebase from "firebase";
import "firebase/firestore";
import "firebase/storage";

const config = {
  apiKey: "AIzaSyCgrYOIYYrWwwVz6dzeMyEKDM5Tj50VLCk",
  authDomain: "the-chicago-machine.firebaseapp.com",
  databaseURL: "https://the-chicago-machine.firebaseio.com",
  storageBucket: "the-chicago-machine.appspot.com",
  projectId: "the-chicago-machine"
};

let firestore;
if (!firebase.apps.length) {
  firestore = firebase.initializeApp(config).firestore();
} else {
  firestore = firebase.app().firestore();
}

firestore.settings({ timestampsInSnapshots: true });

export default firebase;
