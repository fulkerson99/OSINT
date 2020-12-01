function generateReport(){
    alert("Button is working");
}

function collectData(){
    alert("This button is also working");
}

function loadHandlers(){
    //sec1
    document.getElementById("generateReport").addEventListener("click", generateReport);
    //sec2
    document.getElementById("collectData").addEventListener("click", collectData);
}

window.addEventListener("load", loadHandlers);