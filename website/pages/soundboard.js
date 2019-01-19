import firebase from "../lib/firebase";
import { FirestoreProvider } from "react-firestore";
import FileUploader from "react-firebase-file-uploader";
import firebaseui from "firebaseui";

function Soundboard() {
  return (
    <>
      <h1>Soundboard</h1>
      <FileUploader
        accept="audio/*"
        name="audio"
        randomizeFilename
        storageRef={firebase
          .storage()
          .ref()
          .child("audio")}
        onUploadError={error => console.error(error)}
        onUploadSuccess={filename => console.log(`\'${filename}\' uploaded!`)}
        onProgress={progress => console.info(progress)}
      />
    </>
  );
}

export default () => (
  <FirestoreProvider firebase={firebase}>
    <Soundboard />
  </FirestoreProvider>
);
