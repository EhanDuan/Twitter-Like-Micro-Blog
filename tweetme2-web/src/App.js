import React, {useEffect, userState} from 'react'
import logo from './logo.svg';
import './App.css';
import {Tweet} from './tweets'



function TweetsList(props){
  const [tweets, setTweets] = useState([])
  
  useEffect(() => {
    
    const myCallBack = (response, status) => {
      // const tweetItems = [{"content": 123}, {"content" : "Hello World"}]
      if(status === 200){
        setTweets(tweetItems)
      }
    }
    loadTweets(myCallBack)
  }, [])

  return tweets.map((item,index) => {
    return <Tweet tweet={item} className='my-5 py-5 border bg-white text-dark' key={`${index}-{item.id}`}/>
  })
}


function App() {
 

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <div>
          <TweetsList/>
        </div>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
