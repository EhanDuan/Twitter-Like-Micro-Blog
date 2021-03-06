import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import { ProfileBadgeComponent } from './profiles';
import reportWebVitals from './reportWebVitals';
import {FeedComponent, TweetsComponent, TweetDetailComponent} from './tweets'


const appEl = document.getElementById('root')

if(appEl){
  ReactDOM.render(
    <React.StrictMode>
      <App />appEl
    </React.StrictMode>,
  );
}

const tweetsEl = document.getElementById("tweetme-2")
const e = React.createElement
if(tweetsEl){
  ReactDOM.render(e(TweetsComponent, tweetsEl.dataset), tweetsEl);
}

const tweeFeedEl = document.getElementById("tweetme-2-feed")
if(tweeFeedEl){
  ReactDOM.render(e(FeedComponent, tweetsEl.dataset), tweeFeedEl);
}

const tweetDetailElements = document.querySelectorAll(".tweetme-2-detail")

tweetDetailElements.forEach(container => {
  ReactDOM.render(e(TweetDetailComponent, container.dataset), container);

})

const userProfileBadgeElements = document.querySelectorAll(".tweetme-2-profile-badge")

userProfileBadgeElements.forEach(container => {
  ReactDOM.render(e(ProfileBadgeComponent, container.dataset), container);

})


// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
