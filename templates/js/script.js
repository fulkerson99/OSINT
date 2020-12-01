function igGenerateReport(){
    var igUser = document.getElementById("igUser").value;
    alert("Scanning " + igUser);
}

function igCollectData(){
    alert("This button is also working");
}




function twGenerateReport(){
    var twUser = document.getElementById("twUser").value;
    alert("Scanning " + twUser);
}

function twCollectData(){
    alert("This button is also working");
}

function loadHandlers(){
    //sec1
    document.getElementById("IGgenerateReport").addEventListener("click", igGenerateReport);
    document.getElementById("IGcollectData").addEventListener("click", igCollectData);

    document.getElementById("TWgenerateReport").addEventListener("click", twGenerateReport);
    document.getElementById("TWcollectData").addEventListener("click", twCollectData);
}

window.addEventListener("load", loadHandlers);