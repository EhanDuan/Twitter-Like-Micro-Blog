import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import {TweetsComponent} from './tweets'


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


// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
