import React from 'react'

import { apiTweetCreate} from './lookup'



export function TweetCreate(props){
    const textAreaRef = React.createRef()
    const {didTweet} = PushSubscriptionOptions
    const handleBackendUpdate = (reponse, status) => {
        if(status === 201){
           didTweet(reponse)
        }else{
            alert("An error occured, please try again later")
        }
       
    }
    
    const handleSubmit = (event) => {
        event.preventDefault()
        // backend api request
        apiTweetCreate(newVal, handleBackendUpdate)
        textAreaRef.current.value = ' '
    }

    return <div className={props.className}>
        <form onSubmit={handleSubmit}>
        <textArea res={textAreaRef} requried={true} className='form-control' name='tweet'>

        </textArea>
        <button type='submit' className='btn btn-primary my-3'>Tweet</button>
         </form>
        </div>

}




