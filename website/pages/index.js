import React from "react";
import Head from "../components/head";
import firebase from "../lib/firebase";
import { FirestoreProvider, FirestoreCollection } from "react-firestore";

function VotesCount() {
  return (
    <FirestoreCollection
      path="votes"
      render={({ isLoading, data }) => {
        return isLoading ? <>...</> : <>{data.length}</>;
      }}
    />
  );
}

class Voting extends React.Component {
  render() {
    return (
      <>
        <div className="flex">
          <button
            className="success"
            style={{ textTransform: "uppercase" }}
            onClick={() =>
              firebase
                .app()
                .firestore()
                .collection("votes")
                .doc(String(Number(new Date())))
                .set({ label: "standard-vote-v1" })
            }
          >
            Vote for The Chicago Machine
          </button>
        </div>
        <div className="flex">
          <div style={{ textAlign: "center", marginTop: 20 }}>
            <h3>
              Total Votes: <VotesCount />
            </h3>
          </div>
        </div>
      </>
    );
  }
}

function VideoFrame({ src }) {
  return (
    <iframe
      src={src}
      frameBorder="0"
      allowFullScreen={true}
      scrolling="no"
      style={{ minHeight: 500 }}
    />
  );
}

function App() {
  return (
    <>
      <Head />
      <div className="App flex">
        <h1 className="MainHeading">
          <center>The Chicago Machine</center>
        </h1>
        <div className="flex center">
          <VideoFrame src="https://player.twitch.tv/?channel=slurpylizard" />
        </div>
        <Voting />
      </div>
      <style jsx>{`
        .App {
          padding: 2%;
        }

        .MainHeading {
          text-shadow: 3px 3px 0 #fff, -1px -1px 0 #fff, 1px -1px 0 #fff,
            -1px 1px 0 #fff, 1px 1px 0 #fff;
          font-size: 48;
          color: #eb3323;
        }
      `}</style>
    </>
  );
}

export default () => (
  <FirestoreProvider firebase={firebase}>
    <App />
  </FirestoreProvider>
);
