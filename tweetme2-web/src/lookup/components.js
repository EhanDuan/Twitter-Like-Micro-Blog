export function backendLookup(method, endpoint, callback, data){
  let jsonData;
  if(data){
    jsonData = JSON.stringify(data)
  }
  const xhr = new XMLHttpRequest()
  const url = `http://127.0.0.1:8000/api${endpoint}`
  const responseType = "json"

  xhr.responseType = responseType
  xhr.open(method, url)
  const csrftoken = getCookie('csrftoken')
  xhr.setRequestHeader("Content-Type", "application/json")

  if(csrftoken){
    xhr.setRequestHeader("X-CSRFToken", csrftoken)
    // xhr.setRequestHeader("HTTP_X_REQUESTED_WITH", "XMLHttpResquest")
    xhr.setRequestHeader("X-Requested_With", "XMLHttpRequest")
  }
  xhr.onload = function(){
    if(xhr.status === 403 && xhr.response){
      const detail = xhr.response.detail
      if(detail === "Authentication credentials were not provided."){
        if(window.location.href.indexOf("login") === -1){
          window.location.href="/login?showLoginRequired=true"
        }
        
      }
    }
    callback(xhr.response, xhr.status)
  } 
  xhr.onerror = function (e) {
    console.log("error", r)
    callback({"message" : "The request was an error"}, 400)
  }
  xhr.send(jsonData)
}

function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie !== '') {
      var cookies = document.cookie.split(';');
      for (var i = 0; i < cookies.length; i++) {
          var cookie = cookies[i].trim();
          // Does this cookie string begin with the name we want?
          if (cookie.substring(0, name.length + 1) === (name + '=')) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
          }
      }
  }
  return cookieValue;
}



