import React from "react";
import Head from "next/head";
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
      height="378"
      width="620"
    />
  );
}

function CommentsFrame({ src }) {
  return (
    <iframe src={src} frameBorder="0" scrolling="no" height="500" width="100" />
  );
}

function App() {
  return (
    <div
      className="flex"
      style={{
        backgroundColor: "#bbdcf0",
        color: "#000",
        height: "100%",
        width: "100%",
        padding: "2%",
        position: "absolute"
      }}
    >
      <Head>
        <title>The Chicago Machine</title>
        <link
          href="https://cdn.jsdelivr.net/npm/picnic@6.5.0/picnic.min.css"
          rel="stylesheet"
        />
      </Head>
      <h1
        style={{
          textShadow:
            "3px 3px 0 #fff, -1px -1px 0 #fff, 1px -1px 0 #fff, -1px 1px 0 #fff, 1px 1px 0 #fff",
          fontSize: 48,
          color: "#eb3323"
        }}
      >
        <center>The Chicago Machine</center>
      </h1>
      <div className="flex two">
        <VideoFrame src="https://player.twitch.tv/?channel=slurpylizard" />
        <CommentsFrame src="https://www.twitch.tv/embed/slurpylizard/chat" />
      </div>
      <Voting />
    </div>
  );
}

export default () => (
  <FirestoreProvider firebase={firebase}>
    <App />
  </FirestoreProvider>
);
