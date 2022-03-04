import React, {useEffect, useState}from 'react'
import {apiTweetList} from './lookup'
import {Tweet} from './detail'

export function TweetsList(props){
    const [tweetsInit, setTweetsInit] = useState([])
    const [tweets, setTweets] = useState([])
    const [tweetsDidSet, setTweetsDidSet] = useState(false)
    useEffect(() => {
        const final = [...props.newTweets].concat(tweetsInit)
        if(final.length !== tweets.length){   
            setTweets(final)
        }
    }, [props.newTweets, tweets, tweetsInit])

    useEffect(() => {
        if(tweetsDidSet === false){
        const handleTweetListLookup = (response, status) => {
            // const tweetItems = [{"content": 123}, {"content" : "Hello World"}]
            if(status === 200){
                setTweetsInit(response)
                setTweetsDidSet(true)
            }
        }
        apiTweetList(props.username, handleTweetListLookup)
        }
    }, [tweetsInit, tweetsDidSet, setTweetsDidSet, props.username])

    const handleDidRetweet = (newTweet) => {
        const updatedTweetsInit = [...tweetsInit]
        updatedTweetsInit.unshift(newTweet)
        setTweetsInit(updatedTweetsInit)

        const finalTweets = [...tweets]
        finalTweets.unshift(newTweet)
        setTweetsInit(finalTweets)
    }
  
    return tweets.map((item,index) => {
      return <Tweet
             tweet={item} 
             didRetweet={handleDidRetweet}
             className='my-5 py-5 border bg-white text-dark' 
             key={`${index}-{item.id}`}

             />
    })
  }