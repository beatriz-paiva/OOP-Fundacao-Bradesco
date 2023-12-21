function send_data(){
    // console.log("Entrei")
    var name_input = document.getElementById('name').value;
    pywebview.api.sayHelloTo(name_input).then(function showResponse(response) {
        document.getElementById('result').innerHTML = "oi"
    });
}



