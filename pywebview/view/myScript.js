function send_data(){
    var name_input = document.getElementById('name_input').value;
        pywebview.api.sayHelloTo(name_input).then(showResponse)
}

function showResponse(response) {
    var container = document.getElementById('response-container')

    container.innerText = response.message
    container.style.display = 'block'
}

